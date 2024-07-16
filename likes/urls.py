from django.urls import path
from .views import LikeListCreateView, LikeRetrieveDestroyView

urlpatterns = [
    path('', LikeListCreateView.as_view()),
    path('<int:pk>/', LikeRetrieveDestroyView.as_view()),
]
