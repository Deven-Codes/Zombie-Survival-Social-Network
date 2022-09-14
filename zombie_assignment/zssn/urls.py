from django.urls import path
from zssn import views

urlpatterns = [
    path('survivors', views.survivors, name='survivors'),
    path('survivors/<int:pk>', views.survivors_update_location, name='survivors_update_location'),
    path('survivors/reports', views.survivors_reports, name='survivors_reports'),
]