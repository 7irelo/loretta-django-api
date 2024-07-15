from rest_framework import generics, status
from rest_framework.response import Response
from .models import Account
from .serializers import AccountSerializer

class AccountListView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountUpdateView(generics.UpdateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDeleteView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountQueryView(generics.ListAPIView):
    serializer_class = AccountSerializer

    def get_queryset(self):
        queryset = Account.objects.all()
        search = self.request.query_params.get('search', None)
        limit = self.request.query_params.get('limit', None)
        if search:
            queryset = queryset.filter(name__startswith=search)
        if limit:
            queryset = queryset[:int(limit)]
        return queryset
