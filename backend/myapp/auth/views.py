from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import UserRegistrationSerializer
from rest_framework_simplejwt.tokens import RefreshToken


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'POST /register/',
    ]
    return Response(routes)


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            # Generate JWT tokens
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            return Response({
                'message': 'Account created successfully',
                'username': user.username,
                'email': user.email,
                'tokens': tokens
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
