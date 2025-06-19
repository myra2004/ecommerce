from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from accounts.models import User, Cart, CartItem


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ("id", "email", "phone_number", "first_name", "last_name", "is_active", "is_staff")
    list_display_links = ("id", "email", "phone_number", "first_name", "last_name", 'is_confirmed')
    search_fields = ("email", "phone_number", "first_name", "last_name")
    list_filter = ("is_active", "is_staff")

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal_info'), {'fields': ('first_name', 'last_name', 'phone_number', 'avatar', 'bio')}),
        (_('Permissions'), {'fields': ('is_active', 'is_confirmed', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone_number', 'first_name', 'last_name', 'password1', 'password2', 'is_staff',
                       'is_active'),
        }),
    )

    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user")
    list_display_links = ("id",)
    search_fields = ("user",)
    list_editable = ("user",)

    inlines = [CartItemInline]