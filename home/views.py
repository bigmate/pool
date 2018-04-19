from django.shortcuts import render
from .models import Ad, Category, Region
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import Post
from django.utils.text import capfirst
from django.conf import settings
# Create your views here.
def home(request):
    ads_list = Ad.objects.all().order_by('-pub_date')
    return listing(request, ads_list)

def listing(request, items, q_data=''):
    categories = Category.objects.all()
    regions = Region.objects.all()
    paginator = Paginator(items, 1)  # Show 25 contacts per page
    page = request.GET.get('page')
    try:
        ads = paginator.get_page(page)
    except PageNotAnInteger:
        ads = paginator.get_page(1)
    except EmptyPage:
        ads = paginator.get_page(paginator.num_pages)
    context = {'ads': ads, 'categories': categories, 'regions': regions, 'q_data':q_data}
    return render(request, 'home/index.html', context=context)

def search(request):
    q = request.GET.get('query')
    if q:
        ads_list = Ad.objects.filter(
            Q(title__icontains=q)|
            Q(desc__icontains=q)
        ).distinct().order_by('-pub_date')
        return listing(request, ads_list, q_data=q)
    else:
        return home(request)

def detail(request, id):
    ad = Ad.objects.get(pk=id)
    ad.lookups+=1
    ad.save()
    return render(request,'detail/detail.html',{'ad':ad})

def category(request, category):
    ads_list = Ad.objects.filter(category__name=category).order_by('-pub_date')
    return listing(request, ads_list, q_data=category)

def post(request):
    if request.method == 'POST':
        form = Post(request.POST, request.FILES or None)
        if request.user.is_authenticated:
            if form.is_valid():
                Ad.objects.create(
                    user=request.user,
                    region=form.cleaned_data['region'],
                    metro=form.cleaned_data['metro'],
                    category=form.cleaned_data['category'],
                    title=capfirst(form.cleaned_data['title'].lower()),
                    desc=capfirst(form.cleaned_data['desc'].lower()),
                    is_paid=form.cleaned_data['is_paid'],
                    image=form.cleaned_data['image']
                )
                return HttpResponseRedirect(reverse('home:home', current_app='home'))
            else:
                error = 'Жарнаманы жайгаштыруу ийгиликсиз аяктады/something went wrong'
                return render(request, 'post/post.html', {'form': form,'error':error})
        else:
            return HttpResponseRedirect(reverse('accounts:signup', current_app='accounts'))
    else:
        if request.user.is_authenticated:
            if len(Ad.objects.filter(user=request.user)) < settings.AD_NUM_PER_USER:
                form = Post()
                return render(request, 'post/post.html', {'form':form})
            else:
                return render(request,'post/limitover.html',{'limit':settings.AD_NUM_PER_USER})
        else:
            return HttpResponseRedirect(reverse('accounts:signup', current_app='accounts'))
