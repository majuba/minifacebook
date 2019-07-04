from django.contrib import admin

from .models import Nutzer, Hobby
from django.contrib import admin

class MyAdminSite(admin.AdminSite):
    site_header='Minifacebook Admin'
admin_site = MyAdminSite(name='myadmin')


@admin.register(Hobby, site=admin_site)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ('h_name',)

@admin.register(Nutzer, site=admin_site)
class NutzerAdmin(admin.ModelAdmin):
    #fields = ('n_name', 'anzeigename', 'id')
    list_display = ('n_name', 'anzeigename', 'id', 'einkommen', 'alter')

#Register your models here.
