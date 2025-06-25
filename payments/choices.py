from django.db.models import TextChoices


class TransactionStatus(TextChoices):
    PENDING = 'pending', "Pending"
    SUCCESS = 'success', "Success"
    FAILED = 'failed', "Failed"
