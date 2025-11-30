from django.contrib import admin
from.models import Profile,Category, Destination,ContactMessage,About,TeamMember, Service, GalleryCategory,GalleryImage,Blog,Package,Booking

admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Destination)
admin.site.register(ContactMessage)
admin.site.register(About)
admin.site.register(TeamMember)
admin.site.register(Service)
admin.site.register(GalleryCategory)
admin.site.register(GalleryImage)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created_at')
admin.site.register(Package)    
admin.site.register(Booking)
