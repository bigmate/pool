from django.shortcuts import render
from django.views.generic import UpdateView

from home.models import Ad
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import update_session_auth_hash
# Create your views here.
from userprofile.forms import *
from .models import MyUser


def profile(request):
    if request.user.is_authenticated:
        user = request.user
        ads = Ad.objects.filter(user=user).order_by('-pub_date')
        return render(request, 'profile/profile.html', {'user': user, 'ads': ads})
    return HttpResponseRedirect(reverse('accounts:signup', current_app='accounts'))


def update_ad(request, id):
    if request.user.is_authenticated:
        user = request.user
        ads = Ad.objects.filter(user=user).order_by('-pub_date')
        ad = ads.get(pk=id)
        ad.pub_date = timezone.now()
        ad.save()
        return render(request, 'profile/profile.html', {'user': user, 'ads': ads})


def delete_ad(request, id):
    if request.user.is_authenticated:
        user = request.user
        ads = Ad.objects.filter(user=user).order_by('-pub_date')
        ad = ads.get(pk=id)
        ad.delete()
        return render(request, 'profile/profile.html', {'user': user, 'ads': ads})


class UserUpdateView(UpdateView):
    model = MyUser
    form_class = UserSettingsForm
    template_name = 'profile/settings.html'

    def get_success_url(self):
        return self.request.path

    def form_invalid(self, form):
        message = ''
        for error in form.errors:
            message+=error
        return JsonResponse(dict(success=False, message=message))

def settings(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UserSettingsForm(data=request.POST)
            if form.is_valid():
                user = request.user
                user.first_name = form.cleaned_data['first_name']
                user.avatar = request.FILES['avatar']
                user.save()
                # user = MyUser.objects.get(email=request.user)
                # user.first_name = form.cleaned_data['first_name']
                # user.avatar = form.cleaned_data['avatar']
                # user.save()
        form = UserSettingsForm()
        return render(request, 'profile/settings.html', locals())
    return HttpResponseRedirect(reverse('accounts:signup', current_app='accounts'))


def change_password(request):
    return HttpResponseRedirect(reverse('home:home', current_app='home'))
