from django.urls import path

from .views import ProfileDetail, ProfileList

urlpatterns = [
    path('', ProfileList.as_view(), name='profile-list'),
    path('<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
]
