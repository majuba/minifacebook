from django.contrib import admin

from .models import Nutzer
from django.contrib import admin

class MyAdminSite(admin.AdminSite):
    site_header='Minifacebook Admin'
admin_site = MyAdminSite(name='myadmin')

#admin_site.register(Nutzer)
@admin.register(Nutzer, site=admin_site)
class NutzerAdmin(admin.ModelAdmin):
    #fields = ('n_name', 'anzeigename', 'id')
    list_display = ('n_name', 'anzeigename', 'id', 'einkommen', 'alter')

#Register your models here.
