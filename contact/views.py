from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class ContactCreateView(generics.CreateAPIView):
    """
    View for creating a new contact.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactListView(generics.ListAPIView):
    """
    View for listing all contacts.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
