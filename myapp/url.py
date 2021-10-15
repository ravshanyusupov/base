from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base', views.Data, name='data'),
    path('delete', views.delete, name='delete')
]