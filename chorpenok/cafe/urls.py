from django.conf.urls import url

from .views import CafeListView, CafeDetailView

urlpatterns = [
    url(r'^$', CafeListView.as_view(), name='Home'),
    url(r'^cafe/(?P<pk>)$', CafeDetailView.as_view(), name='cafe-detail'),
]