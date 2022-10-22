from rest_framework import views, viewsets, permissions, status
from rest_framework.response import Response
from .serializers import AccountSerializer, SignUpSerializer
from .models import Account


class AccountSignUpView(views.APIView):
    """
    API for handling registration, login, and logout
    """
    # queryset = Account.objects.all()
    serializer_class = SignUpSerializer
    permissions_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows accounts to be viewed or edited.
    """
    queryset = Account.objects.all().order_by('-date_joined')
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]
