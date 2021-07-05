from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserTodo
# Register your models here.

class UserTodoAdmin(admin.ModelAdmin):
	readonly_fields = ('date_created','last_edited')

admin.site.register(UserTodo,UserTodoAdmin)
