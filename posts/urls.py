from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView

urlpatterns = [
    path('', PostListCreateView.as_view()),
    path('<int:pk>/', PostRetrieveUpdateDestroyView.as_view()),
]
