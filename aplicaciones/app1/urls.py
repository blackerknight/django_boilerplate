from django.conf.urls import url
from aplicaciones.app1 import views

urlpatterns = [
    url(r'^app1/$', views.test, name='home')
]
