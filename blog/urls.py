
from django.urls import path
from blog import views

urlpatterns = [
    path('article/', views.ArticleView.as_view()),
]