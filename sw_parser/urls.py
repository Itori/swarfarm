from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^import/', include([
        url(r'^pcap/$', views.import_pcap, name='import_pcap'),
        url(r'^swparser/$', views.import_sw_json, name='import_swparser'),
        url(r'^optimizer/$', views.import_rune_optimizer, name='import_optimizer'),
    ])),
    url(r'^export/', include([
        url(r'^optimizer/$', views.export_rune_optimizer, name='export_optimizer'),
    ])),
]
