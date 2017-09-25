from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ExampleAppThreeView.as_view(), name='example_app_three'),
]
