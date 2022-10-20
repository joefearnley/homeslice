from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AccountSerializer, SignupSerializer
from .models import Account


class AccountSignupView(APIView):
    """
    API for handling registration, login, and logout
    """
    queryset = Account.objects.all()
    serializer = SignupSerializer(data=request.data)


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
