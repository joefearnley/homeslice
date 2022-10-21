from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import AccountSerializer, SignupSerializer
from .models import Account


class AccountSignupView(APIView):
    """
    API for handling registration, login, and logout
    """
    queryset = Account.objects.all()
    serializer_class = SignupSerializer

    def post(self, ):
        serializer = SignupSerializer(data=self.request.data)
        serializer.signup()


class AccountViewSet(ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
