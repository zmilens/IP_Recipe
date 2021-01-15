from django.contrib import admin
from .models import Recipe, Сategorie, Author, Ingredient, Сategory_product

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'description', 'published', 'author')
    list_display_links = ('title', 'category')
    list_filter = ("category", )
    search_fields = ("title__startswith",)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('ingredient', 'category')
    list_filter = ("category", )
    search_fields = ("ingredient__startswith",)


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Сategorie)
admin.site.register(Сategory_product)
admin.site.register(Author)
