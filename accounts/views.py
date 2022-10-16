from rest_framework import viewsets
from rest_framework import permissions
from .serializers import AccountSerializer
from .models import Account


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
