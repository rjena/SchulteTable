from django.conf.urls import url
from . import views

app_name = 'SchulteTable'
urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'api/users', views.users_api),
    url(r'api/tests', views.tests_api),
    url(r'reset_password', views.reset_password),
    url(r'confirm_email', views.confirm_email)
]
