from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from products.models import ProductVariant, Product, Brand, Category, Size, Color, Review, Comment, Story, Contact


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category', 'is_active')
    list_display_links = ('id', 'name', 'brand')
    list_filter = ('is_active', 'brand', 'category')
    search_fields = ('name', 'brand', 'category')
    list_editable = ('is_active',)

    fieldsets = (
        (_("Main"), {
            'fields': ("brand", "category", "is_active")
        }),
        (_("Uzbek"), {
            'fields': ('name_uz', 'description_uz',)
        }),
        (_("English"), {
            'fields': ('name_en', 'description_en',)
        }),
        (_("Russian"), {
            'fields': ('name_ru', 'description_ru',)
        })
    )

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


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'user__email', 'product__name')
    list_display_links = ('id', 'rating', 'user__email')
    search_fields = ('user__email',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__email', 'product__name', 'text')
    list_display_links = ('id', 'user__email')
    search_fields = ('user__email',)


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product', 'is_active')
    list_display_links = ('id', 'title', 'product')
    search_fields = ('title',)

    fieldsets = (
        (_("Main"), {"fields": ("title", "product", "image")}),
    )


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('name', 'email')

    fieldsets = (
    (_("Main"), {
        'fields': ("name", "email", "message",)
    }),
    )