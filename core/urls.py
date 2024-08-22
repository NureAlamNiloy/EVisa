from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('interview/', include('interview.urls')),
    path('notification/', include('notification.urls')),
    path('payment/', include('payment.urls')),
    path('report/', include('report.urls')),
    path('visa/', include('visaprocess.urls')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
