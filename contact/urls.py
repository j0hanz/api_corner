from django.urls import path
from .views import ContactCreateView, ContactListView

urlpatterns = [
    path('create/', ContactCreateView.as_view()),
    path('', ContactListView.as_view()),
]
