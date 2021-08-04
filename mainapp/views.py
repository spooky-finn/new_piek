from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse
from django.views.decorators.http import require_POST
from django.conf import settings
from mainapp.models import *
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse
from multiselectfield import MultiSelectField


def main_def(request):
    categories = Group.objects.only('title', 'slug', 'img')
    context={'categories' : categories,
             'in_cart_counter': cart_counter(request),}
    return render(request, 'mainapp/index.html', context)

def SubgroupDetailView(request, slug):
    subgroup_info = get_object_or_404(Group, slug=slug)
    product_list  = Product.objects.filter(parent__slug=slug)
    return render(
    request,
    'mainapp/SubgroupDetailView.html',
    context = {
    'subgroup_info' : subgroup_info,
    'product_list'  : product_list,
    'in_cart_counter': cart_counter(request),
    })


def ProductDetailView(request, slug_product, slug):
    session_id = request.session._get_or_create_session_key()
    group    = Group.objects.only('groups_content').get(slug=slug)
    product  = Product.objects.get(parent__slug=slug, slug_product=slug_product)
    photos   = ProductImage.objects.filter(page = product)
    docs     = ProductDocs.objects.filter(page = product)
    mod_list = Modification.objects.only('title', 'slug_mod','id').filter(parent__parent__slug=slug, parent__slug_product=slug_product)

    available_sensors = []
    for i, sensor in enumerate(product.sensors):
        available_sensors.append(product.sensors[i])
    print('Все датчики: ', available_sensors)
    sensors_list = Sensor.objects.filter(character__in=available_sensors)

    context = {
    'product' : product,
    'group' : group,
    'photos': photos,
    'docs': docs,
    'mod_list' : mod_list,
    'sensors_list': sensors_list,
    'in_cart_counter': cart_counter(request),
    }
    return render(request, 'mainapp/ProductDetailView.html', context)


def ModificationDetailView(request, slug, slug_product, slug_mod):
    product_pk      = Product.objects.filter(parent__slug=slug, slug_product=slug_product).values('pk')
    product         = Product.objects.only('content', 'href_title', 'h1_mod').get(pk__in = product_pk)
    group           = Group.objects.only('groups_content').get(slug=slug)
    photos          = ProductImage.objects.filter(page__pk__in=product_pk)
    docs            = ProductDocs.objects.filter(page__pk__in=product_pk)
    mod             = get_object_or_404(Modification, slug_mod=slug_mod, parent__pk__in=product_pk)

    available_sensors = []
    for i, sensor in enumerate(product.sensors):
        available_sensors.append(product.sensors[i])
    print('Все датчики: ', available_sensors)
    sensors_list = Sensor.objects.filter(character__in=available_sensors)

    context = {
    'mod' : mod,
    'photos': photos,
    'group': group,
    'product' : product,
    'sensors_list': sensors_list,
    'docs' : docs,
    'in_cart_counter': cart_counter(request),}
    return render(request, 'mainapp/ModificationDetailView.html', context)



def cart(request):
    product_list = None
    if 'piek_cart' in request.session:
        product_list = request.session['piek_cart']
    context = {"product_list": product_list, 'in_cart_counter': cart_counter(request),}
    return render(request, 'mainapp/cart.html', context)

def checkout(request):
    product_list = None
    if 'piek_cart' in request.session:
        product_list = request.session['piek_cart']
    context = {"product_list": product_list, "in_cart_counter": cart_counter(request)}
    return render(request, 'mainapp/checkout.html', context)

def remove_from_cart(request, pk):
    if 'piek_cart' in request.session:
        for i in range(0, len(request.session['piek_cart'])):
            if pk == int(request.session['piek_cart'][i].get('id')):
                request.session['piek_cart'].pop(i)
                request.session.modified = True
                break
    data = {'in_cart_counter': cart_counter(request)}
    return JsonResponse(data)

@require_POST
def update_quantity(request, pk):
    if 'piek_cart' in request.session:
        for i in range(0, len(request.session['piek_cart'])):
            if pk == int(request.session['piek_cart'][i].get('id')):
                quantity = request.session['piek_cart'][i].get('quantity')
                quantity = int(quantity)

                if 'plus' in request.POST.get('name'):
                    request.session['piek_cart'][i].update({'quantity': quantity + 1 })

                if 'minus' in request.POST.get('name') and request.session['piek_cart'][i].get('quantity') > 1:
                    request.session['piek_cart'][i].update({'quantity': quantity - 1 })

                if 'integer' in request.POST.get('name'):
                    request.session['piek_cart'][i].update({'quantity': request.POST.get('quantity') })
                request.session.modified = True
                break

    data = {'in_cart_counter': cart_counter(request),
            'quantity': request.session['piek_cart'][i].get('quantity'), }
    return JsonResponse(data)

@require_POST
def update_conventional_designation(request, pk):
    if 'piek_cart' in request.session:
        for i in range(0, len(request.session['piek_cart'])):
            if pk == int(request.session['piek_cart'][i].get('id')):
                context = {'conventional_designation': request.POST.get('conventional_designation')}
                request.session['piek_cart'][i].update(context)
                request.session.modified = True
                break
    data = {'in_cart_counter': cart_counter(request),
            'conventional_designation': request.session['piek_cart'][i].get('conventional_designation'), }
    return JsonResponse(data)

@require_POST
def product(request, pk):
    print("hello ajax on add to cart")
    form_quantity = 1
    if request.POST.get('quantity') != None:
        form_quantity = int(request.POST.get('quantity'))
        print('form_quantity: '+ str(form_quantity))

    product_title = Modification.objects.only('title').get(id=pk)
    if 'piek_cart' not in request.session:
        request.session['piek_cart']= []
    existance_in_cart = True
    #Проверка на то есть ли в корзину уже данный pk(id)
    for i in range(0, len(request.session['piek_cart'])):
        if  pk == request.session['piek_cart'][i].get('id'):
            quantity = request.session['piek_cart'][i].get('quantity')
            quantity = int(quantity)
            request.session['piek_cart'][i].update({'quantity': quantity + form_quantity })
            request.session.modified = True
            existance_in_cart = False
            break
    #Если после проверки его там нет то existance_in_cart останется как True и он добавится
    if existance_in_cart:
        context={'title': str(product_title),
                 'quantity': form_quantity,
                 'id': pk,
                }
        request.session['piek_cart'].append(context)
        request.session.modified = True
    # next = request.POST.get('next', '/')
    # return HttpResponseRedirect(next)
    data = {'in_cart_counter': cart_counter(request)}
    return JsonResponse(data)



@require_POST
def sent_mail(request):
    product_list = request.session['piek_cart']

    subject = "Заказ c сайта"
    html_template = 'mainapp/html_message.html'
    from_email = "pr@piek.ru"
    admin_email = "loseev@piek.ru"


    to_email = request.POST['email']
    name = request.POST['firstname']
    address = request.POST['address']
    phone = request.POST['phone']
    company = request.POST['company']
    email = request.POST['email']
    description = request.POST['description']
    orderstring = ''




    for product in product_list:
        if product.get('conventional_designation') != '' and product.get('conventional_designation') != None:
            outputordertitle = product.get('conventional_designation')
        else:
            outputordertitle = product.get('title')

        orderstring = orderstring + outputordertitle + ' ' + str(product.get('quantity')) + 'шт.' + '\n'


    html_message = render_to_string(html_template, { 'product_list': product_list, 'name' : name, })

    message = EmailMessage(subject, html_message, from_email, [to_email])
    message.content_subtype = 'html'
    message.send()

    message2text = name + '\n' + phone + '\n' + email + '\n' + 'Адрес: ' + address + '\n' + 'Компания: ' + company + '\n' + 'Пожелания: ' + description + '\n' + 'Заказ: '+ '\n' + orderstring
    message2 = EmailMessage(subject, message2text, from_email, [admin_email])
    message2.send()

    request.session['piek_cart'].clear()
    request.session.modified = True
    return render(request, 'mainapp/minor/sent_mail.html')


def cart_counter(request):
    counter = 0
    if 'piek_cart' in request.session:
        for i in range(0, len(request.session['piek_cart'])):
            counter += int(request.session['piek_cart'][i].get('quantity'))
    return counter



def contacts(request):
    return render(request,'mainapp/contacts.html', context={'in_cart_counter': cart_counter(request)})

def about(request):
    imgs = FactoryPhotos.objects.all()
    return render(request, 'mainapp/about.html', {'in_cart_counter': cart_counter(request), 'imgs': imgs})

def certificate(request):
    certificate = Certificate.objects.all()
    return render(request, 'mainapp/certificate.html', {'in_cart_counter': cart_counter(request),
                                                        'cert' : certificate,
                                                        })

def docs(request):
    return render(request, 'mainapp/docs/operation-manuals.html', {'in_cart_counter': cart_counter(request),})

def general_industrial_design(request):
    docs = Documentation.objects.all()
    return render(request, 'mainapp/docs/general_industrial_design.html', {'in_cart_counter': cart_counter(request), 'docs': docs, })
def explosion_proof_design(request):
    docs = Documentation.objects.all()
    return render(request, 'mainapp/docs/explosion_proof_design.html', {'in_cart_counter': cart_counter(request), 'docs': docs, })
def sensors_and_controllers(request):
    docs = Documentation.objects.all()
    return render(request, 'mainapp/docs/sensors_and_controllers.html', {'in_cart_counter': cart_counter(request), 'docs': docs, })
def starting_and_control_devices(request):
    docs = Documentation.objects.all()
    return render(request, 'mainapp/docs/starting_and_control_devices.html', {'in_cart_counter': cart_counter(request), 'docs': docs, })
def barriers(request):
    docs = Documentation.objects.all()
    return render(request, 'mainapp/docs/barriers.html', {'in_cart_counter': cart_counter(request), 'docs': docs, })
