from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/<int:page>', views.search, name='search'),
    path('user/<int:user_id>', views.user, name='user')
]