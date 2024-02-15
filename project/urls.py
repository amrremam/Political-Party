from django.urls import path, include, reverse_lazy
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

import debug_toolbar


urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('app:dashboard'))),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('addUser/', include('addUser.urls')),
    path('guest/', include('guest.urls')),
    path('__debug__/', include(debug_toolbar.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, documnent_root=settings.STATIC_ROOT)
