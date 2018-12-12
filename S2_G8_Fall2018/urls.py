"""S2_G8_Fall2018 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from myapp import views
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns= [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', views.loginView, name='login'),
    path('about/', views.about, name='about'),
    path('details/', views.details, name='details'),
    path('home/', views.home, name='home'),
    path('searchproperty/', views.searchproperty, name='searchproperty'),
    path('advertiseproperty/', views.advertiseproperty, name='advertiseproperty'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('signup/', views.signup, name='signup'),
    path('loggedin/', views.loggedin, name='loggedin'),
    path('logout/', auth_views.LogoutView.as_view(),  name='logout'),
    path('forgetpassword/', views.forgetpassword, name='forgetpassword'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('quicksearch/', views.quicksearch, name='quicksearch'),
    path('advancesearch/', views.advancesearch, name='advancesearch'),
    path('moredetails/<int:property_id>', views.moredetails, name='moredetails'),
    path('editproperty/<int:property_id>', views.editproperty, name='editproperty'),
    path('updateproperty/<int:property_id>', views.updateproperty, name='updateproperty'),
    path('delete/<int:property_id>', views.delete, name='delete'),
    path('advertise_property/', views.advertise_property, name='advertise_property'),
    path('advertise/', views.advertise, name='advertise'),







] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

""""
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^$', include('myapp.urls')),
]"""


