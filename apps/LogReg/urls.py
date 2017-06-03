#LogReg
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register$', views.log_reg, name="register"),
    url(r'^login$', views.log_reg, name="login"),
    url(r'^logout$', views.logout, name="logout"),
]

#if we have the same views.method do we use the same name?
#what is the difference between using a regex with the $ at the end and not?
