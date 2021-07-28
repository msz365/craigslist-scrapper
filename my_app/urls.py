from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new_search/', views.NewSearchView.as_view(), name='new_search'),
]