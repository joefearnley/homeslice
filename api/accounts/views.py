from rest_framework import views, viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import AccountSerializer, SignUpSerializer
from .models import Account


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


class LoginAPIView(views.APIView):
    """
    API for handling application login and token generation
    """
    


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
