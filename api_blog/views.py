from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def root_route(request):
    return Response(
        {"message": "This Is the API for the private blog project!"}
    )
