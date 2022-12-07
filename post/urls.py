from django.urls import path
from post import views


urlpatterns = [
    path('post/', views.PostList.as_view()),
]
