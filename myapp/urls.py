from django.urls import path
from.import views
urlpatterns = [
    path('',views.base, name = 'base'),
    path('register/', views.register, name='register'),
    path('profile/', views.Profile, name='profile'),
    path('destinations/', views.destination_categories, name='destination_categories'),
    path('destinations/<int:category_id>/', views.category_destinations, name= 'category_destinations')

   
]
