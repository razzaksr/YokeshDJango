from django.urls import path
from . import views

urlpatterns = [
    path('', views.haiThere),
    path('page',views.tempAccess),
    path('send/<int:mynum>',views.gotInput),
    path('media',views.showImg)
]