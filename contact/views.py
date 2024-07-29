from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class ContactCreateView(generics.CreateAPIView):
    """
    View for creating a new contact.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactListView(generics.ListAPIView):
    """
    View for listing all contacts.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ContactSerializer

    def get_queryset(self):
        """
        Filter the queryset by the current user.
        """
        return Contact.objects.filter(owner=self.request.user)
