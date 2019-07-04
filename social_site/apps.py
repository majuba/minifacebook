from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class MyAdminConfig(AdminConfig):
    default_site = 'social_site.admin.MyAdminSite'

class SocialSiteConfig(AppConfig):
    name = 'social_site'
