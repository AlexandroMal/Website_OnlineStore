from django.contrib import admin
from .models import product_data, Category

class product_dataAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'quantity', 'img_full', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('price', 'category', 'quantity')
    prepopulated_fields = {'slug':('title',)}
        
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    prepopulated_fields = {'slug':('name',)}

admin.site.register(product_data, product_dataAdmin)
admin.site.register(Category, CategoryAdmin)

