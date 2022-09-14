from django.urls import path
from zssn import views

urlpatterns = [
    path('survivors', views.survivors, name='survivors'),
]