from rest_framework import generics, throttling
from .models import Contact
from .serializers import ContactSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class ContactListCreateView(generics.ListCreateAPIView):
    """
    View for listing and creating contact messages.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ContactSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user).order_by(
            '-created_at'
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    View for retrieving and updating a contact message.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ContactSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)
