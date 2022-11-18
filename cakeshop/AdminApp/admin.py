from django.contrib import admin

# Register your models here.
from .models import Category,Product
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name')

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','pname','price','description','size','quantity','image','cat')


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)