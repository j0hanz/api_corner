from django.urls import path
from .views import LikeListCreateView, LikeDetail

urlpatterns = [
    path('', LikeListCreateView.as_view()),
    path('<int:pk>/', LikeDetail.as_view()),
]
