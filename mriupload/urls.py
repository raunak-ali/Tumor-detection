from django.urls import path,include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from tumordetection_version_OnE import settings
from .views import  (
 
   result_views
)
app_name='mriupload'
urlpatterns = [
    path('upload',result_views, name='upload'),
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
    
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)