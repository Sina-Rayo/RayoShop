from django.contrib import admin
from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

app_name = "rayo"

urlpatterns = [
    path('penhoon/', admin.site.urls),
    # path('' , views.home),
    path('' , include("shop.urls")),
    path('users/', include("users.urls"))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)