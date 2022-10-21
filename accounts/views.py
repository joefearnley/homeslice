from rest_framework import views, viewsets, permissions
from .serializers import AccountSerializer, SignupSerializer
from .models import Account


class AccountSignUpView(views.APIView):
    """
    API for handling registration, login, and logout
    """
    queryset = Account.objects.all()
    serializer_class = SignUpSerializer

    def post(self):
        serializer = self.serializer_class(data=self.request.data)
        serializer.signup()


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
