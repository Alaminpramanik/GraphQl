from django.contrib import admin

# Register your models here.
from accounts.models import Right, User, Role

admin.site.register(User)
admin.site.register(Right)
admin.site.register(Role)
