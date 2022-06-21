from django.urls import path
from . import views

urlpatterns=[
    path('login/', views.UserApiView.as_view()),
    path('', views.UserView.as_view()),

]