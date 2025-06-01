from django.contrib import admin

from products.models import ProductVariant, Product, Brand, Category, Size, Color


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category', 'is_active')
    list_display_links = ('id', 'name', 'brand')
    list_filter = ('is_active', 'brand', 'category')
    search_fields = ('name', 'brand', 'category')
    list_editable = ('is_active',)

    inlines = [ProductVariantInline]


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'color', 'size', 'color')
    list_display_links = ('id', 'product')
    search_fields = ('product', 'size', 'color')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)