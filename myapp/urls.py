from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'myapp'


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.login, name='login'),
    path('about/', views.about, name='about'),
    path('details/', views.details, name='details'),
    path('home/', views.home, name='home'),
    path('searchproperty/', views.searchproperty, name='searchproperty'),
    path('advertiseproperty/', views.advertiseproperty, name='advertiseproperty'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)