from django.urls import path

from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.sign_up, name='signup'),
    path('login/', views.log_in, name='login'),
    path('home/', views.home, name='home'),
    path('home/book/', views.book, name='book'),
    path('home/success/', views.success, name='success'),
    path('invalid-login/', views.invalid_login, name='invalid_login')
]
