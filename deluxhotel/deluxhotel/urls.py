from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('pages/', include('pages.urls')),
    path('reservation/', include('reservation.urls')),
    path('rooms/', include('rooms.urls')),
    path('blog/', include('blog.urls')),
    path('captcha/', include('captcha.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
