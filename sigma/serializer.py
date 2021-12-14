from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from sigma.models import Quote

class QuoteSerealizer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'author', 'author_quote']