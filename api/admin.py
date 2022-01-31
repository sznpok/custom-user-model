from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User 
from django.contrib.auth.forms import UserChangeForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
									'groups', 'user_permissions')}),
                                    (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
                                    (_('user_info'), {'fields': ('phone_no',)}),
)
    add_fieldsets = (
        (None, {
		'classes': ('wide', ),
		'fields': ('username', 'password1', 'password2',),
	}),
)
    list_display = ['email', 'first_name', 'last_name', 'is_staff', 'phone_no',]
    search_fields = ('username', 'first_name', 'last_name',)
    ordering = ('username', )
admin.site.register(User, UserAdmin)
