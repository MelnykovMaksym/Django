from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('flow_statistics', views.flow_statistics, name='flow_statistics'),
    path('add_spending', views.add_spending, name='add_spending'),
    path('add_incoming', views.add_incoming, name='add_incoming'),
]