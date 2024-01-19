from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dash/', include('app.urls')),
    path('', include('addUser.urls')),
]


urlpatterns += static(settings.MEDIA_URL, documnent_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, documnent_root=settings.STATIC_ROOT)
