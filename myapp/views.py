from django.shortcuts import render, redirect
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Property, PropertyImage, PropertyCategory, PropertyFacing, PropertySector, Country, Province, City, Advertisement
from django.contrib.auth.models import User


# Create your views here.
def loggedin(request):
    return render(request, 'testlogin.html')


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        users = User.objects.filter(username=username)
        print(users)
        if users.count() != 0:
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                properties = Property.objects.filter(propertyUser__username=username)
                login(request, user)
                return render(request, 'testlogin.html', {'properties': properties} )
            else:
                message = "Password Incorrect"
                print(message)
                context = {'message': message}
                return render(request, 'login.html', context)
        else:
            return redirect('signup')

    return render(request, 'login.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def contact(request):
    form = contactForm(request.POST or None)
    title = 'Contact Us'
    context = {'title': title, 'form': form}
    if form.is_valid():
        name = form.cleaned_data['name']
        subject = 'email from mysite'
        comment = form.cleaned_data['comment']
        message = '%s %s' % (comment, name)
        emailTo = [settings.EMAIL_HOST_USER]
        emailFrom = form.cleaned_data['email']
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
    
    template = 'contact.html'
    return render(request, template, context)


def register(request):
    return render(request, 'register.html')


def about(request):
    return render(request, 'about.html')


def details(request):
    return render(request, 'details.html')


def home(request):
    properties = Advertisement.objects.all()
    context = {'properties': properties}
    return render(request, 'homepage.html', context)


def searchproperty(request):
    template_name = 'searchproperty.html'
    properties = Property.objects.all()
    property_images = PropertyImage.objects.all()
    context = {'properties': properties, 'property_images': property_images}
    return render(request, template_name, context)


def advertiseproperty(request):
    return render(request, 'advertiseproperty.html')


def forgetpassword(request):
    return render(request, 'forgetpassword.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def quicksearch(request):
    template_name = 'quicksearch.html'
    if request.method == 'POST':
        category = request.POST['searchbar']
        minPrice = request.POST['minPrice']
        maxPrice = request.POST['maxPrice']
        properties = Property.objects.filter(propertyCategory__propertyCategory=category,
                                             propertyAskingPrice__gte=minPrice, propertyAskingPrice__lte=maxPrice)
        if properties.count() != 0:
            context = {'properties': properties, 'category': category}
        else:
            message = "No property with search criteria found"
            context = {'message': message, 'category': category}

    return render(request, template_name, context)


def advancesearch(request):
    template_name = 'advancesearch.html'
    if request.method == 'POST':
        category = request.POST['category']
        rooms = request.POST['rooms']
        propertyTotalArea = request.POST['propertyTotalArea']
        facing = request.POST['facing']
        propertyCountry = request.POST['propertyCountry']
        propertyCity = request.POST['propertyCity']
        sector = request.POST['sector']
        properties = Property.objects.filter(propertyCategory__propertyCategory=category,
                                             propertyFacing__propertyFacing=facing,
                                             propertyNumberOfRooms=rooms, propertyTotalArea=propertyTotalArea,
                                             propertyCity__cityName=propertyCity,
                                             propertyCountry__countryName=propertyCountry,
                                             propertySector__propertySector=sector,
                                             )
        if properties.count() != 0:
            context_object = {'properties': properties, 'category': category}
        else:
            message = "No property with search criteria found"
            context_object = {'message': message, 'category': category}
    else:
        context_object = {}

    return render(request, template_name, context_object)


def moredetails(request, property_id):
    property = Property.objects.filter(id=property_id)
    getImage = PropertyImage.objects.filter(property_id=property_id)
    if getImage.count() != 0:
        context = {'property': property, 'propertyimage': getImage}
    else:
        error_message = "Image not available"
        context = {'property': property, 'error_message': error_message}

    return render(request, 'moredetails.html', context)


def editproperty(request, property_id):
    property = Property.objects.filter(id=property_id)
    for propert in property:
        print(propert.propertyTitle)
    if property.count() != 0:
        context = {'property': property}
    else:
        error_message = "No Properties available"
        context = {'property': property, 'error_message': error_message}
    return render(request,'editproperty.html', context)


def updateproperty(request, property_id):
    if request.method == 'POST':
        title = request.POST['title']
        category = request.POST['Category']
        sector = request.POST['Sector']
        facing = request.POST['Facing']
        country = request.POST['Country']
        province = request.POST['Province']
        city = request.POST['City']
        street = request.POST['Street']
        postalcode = request.POST['Postal Code']
        noofhalls = request.POST['Number of Halls']
        noofrooms = request.POST['Number of Rooms']
        noofbathrooms = request.POST['Number Of Bathrooms']
        nooffloors = request.POST['Number Of Floors']
        totalarea = request.POST['Total Area']
        askprice = request.POST['Asking Price']
        #print(PropertyCategory.objects.all())
        f = PropertyCategory.objects.filter(propertyCategory=category)
        #print(f.values())
        for f in f:
            print(f.propertyCategory)
        #c = Country.objects.all()
        s = PropertySector.objects.filter(propertySector=sector)
        for s in s:
            print(s.propertySector)
        fa = PropertyFacing.objects.filter(propertyFacing=facing)
        for fa in fa:
            print(fa.propertyFacing)
        p = Province.objects.filter(provinceName=province)
        for p in p:
            print(p.provinceName)
        ci = City.objects.filter(cityName=city)
        for ci in ci:
            print(ci.cityName)
        c = Country.objects.filter(countryName=country)
        #print(c.values())
        for c in c:
            print(c.countryName)
        entries = Property.objects.filter(id=property_id).update(propertyTitle=title, propertyCategory_id=f,
                                                                 propertySector=s, propertyFacing=fa,
                                                                 propertyCountry=c, propertyProvince=p,
                                                                 propertyCity=ci, propertyStreet=street,
                                                                 propertyPostalCode=postalcode, propertyStreetNumber=street,
                                                                 propertyNumberOfHalls=noofhalls, propertyNumberOfRooms=noofrooms,
                                                                 propertyNumberOfBathrooms=noofbathrooms,
                                                                 propertyNumberOfFloors=nooffloors,
                                                                 propertyTotalArea=totalarea, propertyAskingPrice=askprice,
                                                                 )
        property = Property.objects.filter(id=property_id)
        for property in property:
            property_user_id = property.propertyUser_id
            user= User.objects.filter(id=property_user_id)
        for user in user:
            print(user.username)

        properties= Property.objects.filter(propertyUser__username=user)
    return render(request,'testlogin.html', {'properties':properties})


def delete(request, property_id):
    Property.objects.filter(id=property_id).delete()
    return redirect("home")


def advertise_property(request):
    property = Property.objects.all()
    if property.count()!=0:
        context= {'properties':property}
    else:
        error_message = "No Properties available"
        context = {'properties': property, 'error_message': error_message}

    return render(request,'advertiseproperty.html',context)


def advertise(request):
    if request.method=="POST":
        start = request.POST['start']
        end = request.POST['end']
        description = request.POST['description']
        prop = request.POST['prop']
        data = Advertisement(advStartDate=start, advEndDate=end, advDescription=description, advProp=prop)
        data.save()
        return render(request, "advertiseproperty.html")








