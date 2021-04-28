from django.conf.urls import url
from Rental import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^rental/$', views.rentalAPI),
    url(r'^rental/([0-9]+)$', views.rentalAPI)

]
