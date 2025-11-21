from .models import Category

def category_dropdown(request):
    return {
        'categories_for_nav': Category.objects.all()
    }
