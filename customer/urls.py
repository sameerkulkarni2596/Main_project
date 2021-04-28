from django.conf.urls import url
from customer import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
        url(r'^customer/$',views.customerApi),
        url(r'^customer/([0-9]+)$', views.customerApi),
        url(r'^customercred/$',views.customercredApi),

]
