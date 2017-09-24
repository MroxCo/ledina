from django.conf.urls import  include, url
from django.contrib import admin
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static

from ledina.authentication import views as auth_views
from ledina.core import views as core_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.index, name='index'),
    url(r'^profil/(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^registracija/$', auth_views.register, name="register"),
    url(r'^noscript/$', core_views.noscript, name='noscript'),
    url(r'^prijava/$', auth_views.login_user, name="login_user"),
    url(r'^odjava/$', auth_views.logout_user, name="logout_user"),
    url(r'^testi/', include('ledina.exams.urls'), name="exams"),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    