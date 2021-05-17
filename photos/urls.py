from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$', views.index, name='homepage'),
    re_path(r'^image/(\d+)', views.view_image, name='image'),
    re_path(r'^categories/', views.search_categories, name='categories'),
    re_path(r'^cities/', views.search_locations, name='locations'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)