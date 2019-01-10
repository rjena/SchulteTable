from django.contrib import admin
from .models import UserST, Test

class UserSTAdmin(admin.ModelAdmin):
    fields = ('login', 'name', 'email', 'bday', 'password')
    list_display = ('id', 'login', 'name', 'email', 'bday', 'password', 'tokenToConfirmEmail', 'tokenToResetPassword')
    list_filter = ['bday']

class TestAdmin(admin.ModelAdmin):
    fields = ('stWU', 'stWE', 'stPS', 'age', 'date', 'user_id')
    list_display = ('id', 'user_id', 'age', 'stWU', 'stWE', 'stPS', 'date')
    list_filter = ['user_id', 'age', 'date']

admin.site.register(UserST, UserSTAdmin)
admin.site.register(Test, TestAdmin)
