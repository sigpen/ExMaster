from django.conf.urls import url

from expenses import views

urlpatterns = [
    url(r'^$', views.list_expenses),
]