from django.shortcuts import render, redirect
from django.db.models import Q
from app.models import *
from .form import *

def home(request):
    slider = Property.objects.filter(Q(active=True)).order_by('-id')[:3]
    recent_property = Property.objects.filter(Q(active=True)).order_by('-id')[:6]
    top = Property.objects.filter(Q(active=True)).order_by('id')[:3]
    agent = UserExtra.objects.all()[:9]
    blog = Blog.objects.all().order_by('-date')[:3]
    ####search form
    prop_type = PropertyType.objects.all()
    city = City.objects.all()
    context = {
        'slider': slider,
        'recent_property': recent_property,
        'top': top,
        'agent': agent,
        'blog': blog,
        'prop_type': prop_type,
        'city': city,
    }
    return render(request, 'index.html', context)

def blog(request):
    page = 1
    per_page = 6
    blog_count = Blog.objects.all().count()
    count_page = int(blog_count / per_page) + 1
    # start_page = (page - 1) * per_page
    blog = Blog.objects.order_by('-date')[:per_page]
    context = {
        'page': page,
        'count_page': range(count_page),
        'blog': blog,
    }
    return render(request, 'blog.html', context)

def blog_page(request, page):
    per_page = 6
    blog_count = Blog.objects.all().count()
    count_page = int(blog_count / per_page) + 1
    start_page = (page - 1) * per_page
    blog = Blog.objects.order_by('-date')[start_page:per_page]
    context = {
        'page': page,
        'count_page': range(count_page),
        'blog': blog,
    }
    return render(request, 'blog.html', context)

def blog_detail(request, url):
    blog = Blog.objects.filter(url=url).count()
    if blog == 0:
        return redirect('/')
    else:
        blog = Blog.objects.filter(url=url)
        for i in blog:
            tag = i.tag
        tag = tag.split('--')
        some = Blog.objects.order_by('date')[:2]
        context = {
            'blog': blog,
            'some': some,
            'tag': tag,
        }
        return render(request, 'blog-details.html', context)

def property(request):
    page = 1
    per_page = 6
    prop_count = Property.objects.filter(Q(active=True)).count()
    count_page = int(prop_count / per_page) + 1
    #start_page = (page - 1) * per_page
    prop = Property.objects.filter(Q(active=True)).order_by('-id')[:per_page]
    ####search form
    prop_type = PropertyType.objects.all()
    city = City.objects.all()
    context = {
        'prop': prop,
        'count_page': range(count_page),
        'page': page,
        'prop_type': prop_type,
        'city': city,
    }
    return render(request, 'property.html', context)

def property_page(request, page):
    per_page = 6
    prop_count = Property.objects.filter(Q(active=True)).count()
    count_page = int(prop_count / per_page) + 1
    start_page = (page - 1) * per_page
    prop = Property.objects.filter(Q(active=True)).order_by('-id')[start_page:per_page]
    ####search form
    prop_type = PropertyType.objects.all()
    city = City.objects.all()
    context = {
        'prop': prop,
        'count_page': range(count_page),
        'page': page,
        'prop_type': prop_type,
        'city': city,
    }
    return render(request, 'property.html', context)

def property_detail(request, id):
    property = Property.objects.filter(Q(id=id) & Q(active=True)).count()
    if property == 0:
        return redirect('/')
    else:
        property = Property.objects.filter(id=id)
        for i in property:
            agent = UserExtra.objects.filter(id=i.agent.id)
        context = {
            'prop': property,
            'agent': agent,
        }
        return render(request, 'property-details.html', context)

def agent(request):
    agents = UserExtra.objects.all()
    context = {
        'agent': agents,
    }
    return render(request, 'about-us.html', context)

def contact(request):
    flag = 0
    form = ContactForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            message = form.cleaned_data.get('message')
            if phone == '':
                phone = 'No phone'
            contact = Contact(name=name, email=email, phone=phone, message=message, status=False)
            contact.save()
            flag = 1
    context = {
        'form': form,
        'flag': flag,
    }
    return render(request, 'contact.html', context)

#########################
def search(request):
    if request.method == 'POST':
        status = request.POST.get('status')
        type = request.POST.get('type')
        city = request.POST.get('city')
        bed = int(request.POST.get('bed'))
        bath = int(request.POST.get('bath'))

        price = request.POST.get('price')
        price = price.replace('$', '')
        price = price.replace('[', '')
        price = price.replace(']', '')
        price = price.split('-')

        area = request.POST.get('area')
        area = area.replace('m2', '')
        area = area.replace('[', '')
        area = area.replace(']', '')
        area = area.split('-')

        prop = Property.objects.filter(Q(active=True) & Q(status=status) & Q(property_type=type) & Q(city=city) & Q(bed_room=bed) & Q(baths=bath) & Q(price__gte=int(price[0]), price__lte=int(price[1])) & Q(home_area__gte=int(area[0]), home_area__lte=int(area[1])))
        ####search form
        prop_type = PropertyType.objects.all()
        city = City.objects.all()
        context = {
            'prop': prop,
            'prop_type': prop_type,
            'city': city,
        }
        return render(request, 'property_search.html', context)
    else:
        return redirect('/')
    return redirect('/')

def agent_contact(request, id, prop_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        prop_exist = Property.objects.filter(Q(active=True) & Q(id=prop_id) & Q(agent=id)).count()
        if prop_exist == 0:
            return redirect('/')
        else:
            property = Property.objects.get(id=prop_id)
            agent = UserExtra.objects.get(id=id)
            agent_contact = AgentContact(name=name, email=email, phone=phone, property=property, agent=agent, status=False)
            agent_contact.save()
            return redirect('/property/')
    else:
        return redirect('/')
    return redirect('/')