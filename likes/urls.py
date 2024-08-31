from django.urls import path

from .views import LikeDetail, LikeList

urlpatterns = [
    path('', LikeList.as_view()),
    path('<int:pk>/', LikeDetail.as_view()),
]
