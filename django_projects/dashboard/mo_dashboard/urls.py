from django.urls import path
from mo_dashboard import views

urlpatterns = [
    path('see', views.todolist,name='todolist'),
    path('curam', views.curam,name='curampath'),
    path('ua', views.ua,name='uapath'),
    
]