from django.urls import path
from .views import FollowerListCreateView, FollowerRetrieveDestroyView

urlpatterns = [
    path('', FollowerListCreateView.as_view(), name='follower-list-create'),
    path(
        '<int:pk>/',
        FollowerRetrieveDestroyView.as_view(),
        name='follower-detail',
    ),
]
