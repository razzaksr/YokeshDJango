from django.urls import path
from . import views
urlpatterns = [
    path('', views.showHome),
    path('list', views.check),
    path('new', views.showNew),
    path('one/<str:id>',views.showReadOne),
    path('remove/<str:id>',views.showDelete)
]