from django.urls import path
from .views import TransactionCreateView, TransactionDetailView, TransactionUpdateView, TransactionDeleteView, CPJTransactionListView, CRJTransactionListView

urlpatterns = [
    path('create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('update/<int:pk>/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('delete/<int:pk>/', TransactionDeleteView.as_view(), name='transaction_delete'),
    path('cpj/', CPJTransactionListView.as_view(), name='cpj_transactions'),
    path('crj/', CRJTransactionListView.as_view(), name='crj_transactions'),
]
