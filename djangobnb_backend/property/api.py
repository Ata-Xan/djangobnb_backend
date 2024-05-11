from django.http import JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Property
from .serializers import PropertiesListSerializer

@api_view(['GET'])
# the following means that the endpoint is public and no authentication is required
@authentication_classes([])
# the following means that the endpoint is public and no permission is required
@ permission_classes([])
# difference between authentication and permission is that the authentication is about who you are and the permission is about what you can do
def properties_list(request):
    properties = Property.objects.all()
    serializer = PropertiesListSerializer(properties, many=True)
    return JsonResponse(
        {'data':serializer.data}, safe=False)