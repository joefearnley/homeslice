from rest_framework import views, viewsets, permissions, status, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import AccountSerializer, SignUpSerializer, UpdatePasswordSerializer
from accounts.models import Account


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountSignUpAPIView(views.APIView):
    """
    API for handling registration
    """
    serializer_class = SignUpSerializer
    permissions_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            token = Token.objects.create(user=account)
            return Response({
                'user': serializer.data,
                'token' : token.key
                }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(views.APIView):
    """
    API for handling application logout
    """
    def get(self, request, format=None):
        if request.user.is_anonymous:
            errors = {
                'message': 'Unauthenticated request.'
            }
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)

        request.user.auth_token.delete()

        success_message = {
            'message': 'Account successfully logged out.'
        }

        return Response(success_message, status=status.HTTP_200_OK)


class UpdatePasswordAPIView(generics.UpdateAPIView):
    """
    API for handling password updates
    """
    serializer_class = UpdatePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()

        current_token = Token.objects.filter(user=account)

        if current_token.exists():
            current_token.delete()

        token, created = Token.objects.get_or_create(user=account)

        response_data = {
            'message': 'Password successfully updated.',
            'token': token.key
        }

        return Response(response_data, status=status.HTTP_200_OK)
