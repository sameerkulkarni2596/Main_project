from django.conf.urls import url
from Movies import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
url(r'^movies/$', views.movieAPI),
    url(r'^movies/([0-9]+)$', views.movieAPI),

]
