from django.urls import path
from . import views
urlpatterns = [
    path('', views.showLogin),
    path('home', views.showHome),
    path('logout',views.showLogout),
    path('list', views.check),
    path('new', views.showNew),
    path('one/<str:id>',views.showReadOne),
    path('remove/<str:id>',views.showDelete),
    path('shortlist',views.showShort)
]