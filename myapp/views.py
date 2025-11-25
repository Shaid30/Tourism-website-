from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm
from.models import Profile
from django.shortcuts import render, get_object_or_404
from .models import Category, Destination, About,TeamMember, Service,GalleryImage,GalleryCategory,Blog,Package
from .forms import ContactForm,GalleryUploadForm
from django.contrib import messages
def base(request):
    return render(request,'myapp/base.html')
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )

            photo = form.cleaned_data.get('photo')
            Profile.objects.create(user=user, photo=photo)

            login(request, user)
            return redirect('base')
    else:
        form = RegisterForm()

    return render(request, 'myapp/register.html', {'form': form})

def destination_categories(request):
    categories= Category.objects.all()
    return render(request, 'myapp/destination_categories.html', {'categories':categories})

def category_destinations(request, category_id):
    category = get_object_or_404(Category, id= category_id)
    destinations = Destination.objects.filter(category=category)
    return render(request, 'myapp/category_destinations.html',{
        'category':category,
        'destinations':destinations
    })

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})

def about_view(request):
    about = About.objects.first()   
    team = TeamMember.objects.all()
    services = Service.objects.all()
    return render(request, 'myapp/about.html', {'about': about, 'team': team, 'services': services})


def gallery(request):
    category_name = request.GET.get('category')
    categories = GalleryCategory.objects.all()

    if category_name :
        images = GalleryImage.objects.filter(category_name=category_name)
    else:
        images = GalleryImage.objects.all()

    return render(request, "gallery.html",{
        "categories": categories,
        "images": images,
    })

def upload_image(request):
    if request.method =="POST":
        form =GalleryUploadForm(request.POST, request.FILES)
        if form .is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = GalleryUploadForm()

        return render (request, "upload.html",{"form":form})



def blog_list(request):
    posts = Blog.objects.all()
    return render(request, 'myapp/blog_list.html', {'posts':posts})

def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render(request, 'myapp/blog_detail.html', {'post':post})

def package_list(request):
    packages = Package.objects.all()
    return render(request, 'myapp/package_list.html', {'packages': packages})


def book_package(request, package_id):
    package = Package.objects.get(id=package_id)
    return render(request, 'myapp/booking.html', {"package": package})
