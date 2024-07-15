from rest_framework import generics, permissions
from .models import Contact
from .serializers import ContactSerializer


class ContactListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating contact messages.
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Contact.objects.all().order_by('-created_at')
    serializer_class = ContactSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
