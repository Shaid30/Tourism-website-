from django.urls import path
from.import views
from .views import about_view
from .views import contact_view
urlpatterns = [
    path('',views.base, name = 'home'),
    path('destinations/', views.destination_categories, name='destination_categories'),
    path('destinations/<int:category_id>/', views.category_destinations, name= 'category_destinations'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path("gallery/", views.gallery, name="gallery"),
    path("gallery/upload/", views.upload_image, name="upload_image"),
    path('blog/', views.blog_list, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('packages/', views.package_list, name='package_list'),
    path('packages/book/<int:package_id>/', views.book_package, name='book_package'),
    path('success/', views.success_page, name='success_page'),
    path('search/', views.search_packages, name='search_packages'),
    path('destination/<int:destination_id>/packages/', views.destination_packages, name='destination_packages'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('account/', views.user_dashboard, name='user_dashboard'),
    path("search/", views.search, name="search"),
    path('book/coxsbazar/', views.book_cox, name='book_cox'),
    path('book/sajek/', views.book_sajek, name='book_sajek'),
    path('book/sundarban/', views.book_sundarban, name='book_sundarban'),






]





    


