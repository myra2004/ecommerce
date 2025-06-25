from django.db import models
from rest_framework import serializers

from payments.models import Transaction
from payments.choices import TransactionStatus
from common.choices import OrderStatus


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'id',
            'order',
            'user',
            'remote_id',
            'amount',
        )

        # read_only_fields = ['id', 'user', 'remote_id']

    def validate(self, attrs):
        user = self.context['user']
        order = attrs['order']
        amount = attrs['amount']

        # Check if the order is cancelled
        if order.status == OrderStatus.CANCELLED:
            raise serializers.ValidationError('Cannot pay for a cancelled order')

        # Check if the user is the owner of the order
        if user != order.user:
            raise serializers.ValidationError('You cant buy someones order')

        # Check if the amount is above the minimum
        if amount <= 1000 * 100:
            raise serializers.ValidationError('Amount must be more 1000')

        # Calculate the total amount already paid for this order
        successful_transactions = Transaction.objects.filter(
            order=order,
            status=TransactionStatus.SUCCESS
        )
        total_paid = successful_transactions.aggregate(
            total=models.Sum('amount')
        )['total'] or 0

        # Check if adding this payment would exceed the order's total price
        if total_paid + amount > order.total_price:
            raise serializers.ValidationError('Total paid amount would exceed the order total price')

        return attrs

    def create(self, validated_data):
        new_transaction = Transaction.objects.create(
            order = validated_data['order'],
            user = self.context['user'],
            remote_id='-',
            amount=validated_data['amount'],
            status=TransactionStatus.PENDING,
        )

        return new_transaction
