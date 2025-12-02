from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Category, Destination, About,TeamMember, Service,GalleryImage,GalleryCategory,Blog,Package,Booking
from .forms import ContactForm,GalleryUploadForm
from django.contrib import messages
from django.db.models import Q
def base(request):
    return render(request,'myapp/base.html')

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


def gallery(request, category_id=None):
    categories = Category.objects.all()
    selected_category = request.GET.get("category")

    if selected_category:
        images = GalleryImage.objects.filter(category_id=selected_category)
    else:
        images = GalleryImage.objects.all()

    return render(request, 'myapp/gallery.html', {
        'categories': categories,
        'images': images,
        'selected_category': selected_category,
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


def book_package(request,package_id):
    package = Package.objects.get(id=package_id)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phonenumber')
        payment_method = request.POST.get('payment_method')
        transaction_id = request.POST.get('transaction_id')

        Booking.objects.create(
            package=package,
            name=name,
            email=email,
            phone=phone,
            payment_method=payment_method,
            transaction_id=transaction_id
        )

        return redirect('success_page')  

    return render(request, 'myapp/booking.html', {"package": package})


def success_page(request):
    return render(request, 'myapp/success.html')


def search_packages(request):
    query = request.GET.get('q')
    if query:
        try:
        
            destination = Destination.objects.get(name__iexact=query)
            return redirect('destination_packages', destination_id=destination.id)
        except Destination.DoesNotExist:
            return render(request, 'myapp/search_results.html', {'query': query, 'destinations': []})
    else:
        return render(request, 'myapp/search_results.html', {'query': '', 'destinations': []})

def destination_packages(request, destination_id):
    destination = get_object_or_404(Destination, id=destination_id)
    packages = destination.packages.all()
    return render(request, 'myapp/destination_packages.html', {'destination': destination, 'packages': packages})


def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')
    return render(request, 'myapp/register.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('user_dashboard')
    return render(request, 'myapp/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

@login_required
def user_dashboard(request):
    user = request.user
    return render(request, 'myapp/dashboard.html', {"user": user})


def search(request):
    query = request.GET.get("q", "")
    keywords = query.split()  # split: ['Rangamati', 'Lake', 'Tour']



    package_q = Q()
    gallery_q = Q()
    blog_q = Q()

    for word in keywords:
        package_q |= Q(name__icontains=word) | Q(description__icontains=word)
        gallery_q |= Q(title__icontains=word)
        blog_q |= Q(title__icontains=word) | Q(content__icontains=word)

    package_results = Package.objects.filter(package_q)
    gallery_results = GalleryImage.objects.filter(gallery_q)
    blog_results = Blog.objects.filter(blog_q)

    return render(request, "search_results.html", {
        "query": query,
        "package_results": package_results,
        "gallery_results": gallery_results,
        "blog_results": blog_results,
    })
