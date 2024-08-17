from rest_framework.decorators import api_view
from rest_framework.response import Response
from eth_transactions.models import Transaction

@api_view(['GET'])
def get_eth_transactions(request):
    return Response(Transaction.objects.all().values())
