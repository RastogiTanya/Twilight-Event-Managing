from django.urls import path
from . import views
urlpatterns = [
    path('', views.Abc.hp),
    path('homepage', views.Abc.hp),
    path('everegis',views.Abc.everegis),
    path('eventlist', views.Abc.eventlist),
    path('eventdash',views.Abc.eventdash)
]