from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Costumer

# mostra o campo endereço no painel de admin
class CostumerInLine(admin.StackedInline):
    model = Costumer
    can_delete = False
    verbose_name_plural = 'costumer'

class UserAdmin(BaseUserAdmin):
    inlines = (CostumerInLine,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
