from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import Textarea

from apps.user.models import MyUser


class MyUserAdmin(UserAdmin):
	list_display = ('email', 'user_name', 'first_name', 'id', 'is_active', 'is_staff')
	ordering = ('-start_date',)
	search_fields = ('email', 'user_name', 'first_name',)
	fieldsets = (
		(None, {'fields': ('email', 'user_name', 'first_name', 'id')}),
		('Personal', {'fields': ('about',)}),
		('Permissions', {'fields': ('is_staff', 'is_active')}),
	)
	readonly_fields = ('email', 'id')
	formfield_overrides = {
		models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
	}
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff')}
		 ),
	)


admin.site.register(MyUser, MyUserAdmin)
