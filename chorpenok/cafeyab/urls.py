from django.conf.urls import url


from cafeyab.views import HomeView


urlpatterns = [
    url(r'^$', HomeView, name='Home'),
]
