from userprofile.views import UserUpdateView
from . import views
from django.urls import path

app_name = 'userprofile'
urlpatterns = [
    path('', views.profile, name='profile'),
    path('update/<int:id>', views.update_ad, name='update_ad'),
    path('delete/<int:id>', views.delete_ad, name='delete_ad'),
    path('settings/<int:pk>', UserUpdateView.as_view(), name='settings'),
    path('settings/change-password/', views.change_password, name='change_password')
]
