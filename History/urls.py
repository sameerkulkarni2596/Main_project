from django.conf.urls import url
from History import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
url(r'^history/$', views.historyAPI),

]
