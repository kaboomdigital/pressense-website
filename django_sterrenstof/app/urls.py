from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^programma/$', views.programma, name='programma'),
    url(r'^programma/(?P<programma_url>\D+)$', views.programma_details, name='programma_details'),
    url(r'^festival-info/$', views.festival_info, name='festival_info'),
    url(r'^time-table/$', views.time_table, name='time_table'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
