from django.contrib import admin
from .models import Category, Volunteer, Slide, Blog,Testimonial
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('blog_title', 'created_at', 'created_by')
    fields = ('blog_title', 'blog_image', 'content_with_images', 'categories')  # Specify the fields you want to display in the admin form

    def save_model(self, request, obj, form, change):
        # Set the created_by field to the currently logged-in user
        if not obj.created_by_id:
            obj.created_by = request.user
        obj.save()
        
    def get_queryset(self, request):
        # Only show the blogs created by the currently logged-in user
        qs = super().get_queryset(request)
        return qs.filter(created_by=request.user)

admin.site.register(Category)
admin.site.register(Volunteer)
admin.site.register(Slide)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Testimonial)