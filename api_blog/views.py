from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def root_route(request):
    """
    Root API view to display a welcome message and API details.
    """
    api_details = {
        "message": "Welcome to the API for Corner!",
        "description": "This is the backend API. Please create an account from the official website.",
        "endpoints": {
            "Authentication": "/dj-rest-auth/",
            "Users": "/users/",
            "Posts": "/posts/",
            "Comments": "/comments/",
            "Likes": "/likes/",
            "Bookmarks": "/bookmarks/",
            "Followers": "/followers/",
            "Reports": "/reports/",
            "Contact": "/contact/",
            "News": "/news/",
        },
    }
    return Response(api_details)
