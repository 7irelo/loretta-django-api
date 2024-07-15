from django.urls import path
from .views import AccountListView, AccountDetailView, AccountUpdateView, AccountDeleteView, AccountQueryView

urlpatterns = [
    path('', AccountListView.as_view(), name='account_list'),
    path('<int:pk>/', AccountDetailView.as_view(), name='account_detail'),
    path('update/<int:pk>/', AccountUpdateView.as_view(), name='account_update'),
    path('delete/<int:pk>/', AccountDeleteView.as_view(), name='account_delete'),
    path('query/', AccountQueryView.as_view(), name='account_query'),
]
