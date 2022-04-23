from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import  (home_views)
app_name='tumordetection'
urlpatterns = [
    path('',home_views,name='HOME')
]