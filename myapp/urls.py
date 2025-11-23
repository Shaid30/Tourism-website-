from django.urls import path
from.import views
from .views import about_view
from .views import contact_view
urlpatterns = [
    path('',views.base, name = 'home'),
    path('register/', views.register, name='register'),
    path('profile/', views.Profile, name='profile'),
    path('destinations/', views.destination_categories, name='destination_categories'),
    path('destinations/<int:category_id>/', views.category_destinations, name= 'category_destinations'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
]

