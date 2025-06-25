from rest_framework import serializers

from payments.models import Transaction
from payments.choices import TransactionStatus


class WooPayPerformSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(required=True)
    remote_id = serializers.CharField(required=True)
    status = serializers.ChoiceField(choices=TransactionStatus.choices, required=True)