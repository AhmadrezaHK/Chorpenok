from django.conf.urls import url

from .views import CafeListView

urlpatterns = [
    url(r'^$', CafeListView.as_view(), name='Home'),
]