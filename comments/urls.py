from django.urls import path
from .views import CommentListCreateView, CommentRetrieveUpdateDestroyView

urlpatterns = [
    path('', CommentListCreateView.as_view()),
    path('<int:pk>/', CommentRetrieveUpdateDestroyView.as_view()),
]
