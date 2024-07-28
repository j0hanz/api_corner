from rest_framework import generics, throttling
from .models import Contact
from .serializers import ContactSerializer
from api_blog.permissions import IsOwnerOrReadOnly


class ContactListCreateView(generics.CreateAPIView):
    """
    View for creating contact messages.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ContactSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ContactListRetrieveView(generics.ListAPIView):
    """
    View for listing contact messages.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ContactSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user).order_by(
            '-created_at'
        )


class ContactRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    View for retrieving and updating a contact message.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ContactSerializer
    throttle_classes = [throttling.UserRateThrottle]

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user).order_by('id')
