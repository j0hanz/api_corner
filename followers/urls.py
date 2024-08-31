from django.urls import path

from .views import FollowerDetail, FollowerList

urlpatterns = [
    path('', FollowerList.as_view()),
    path('<int:pk>/', FollowerDetail.as_view()),
]
