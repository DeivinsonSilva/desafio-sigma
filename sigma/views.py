from rest_framework import viewsets
from sigma.models import Quote
from sigma.serializer import QuoteSerealizer

class QuotesViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerealizer

    
