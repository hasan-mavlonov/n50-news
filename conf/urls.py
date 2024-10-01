from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from forms.views import create_user_info_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', include('forms.urls', namespace="form")),
    path('', include('news.urls', namespace="news")),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
