import json
from django.dispatch import receiver
from django.db.models.signals import post_save
from django_celery_beat.models import CrontabSchedule, PeriodicTask
from datetime import timedelta

from products.models import Story
from products.tasks import create_story_expire_time


@receiver(post_save, sender=Story)
def story_post_save(sender, instance, created, **kwargs):
    print("Signal is working!")
    if created:
        expire_time = instance.created_at + timedelta(minutes=1)
        args = [instance.id]
        print(expire_time, args)
        start_crontab, created = CrontabSchedule.objects.get_or_create(
            minute=str(expire_time.minute),
            hour=str(expire_time.hour),
            day_of_month=str(expire_time.day),
            month_of_year=str(expire_time.month),
            timezone=str(expire_time.tzinfo)
        )
        PeriodicTask.objects.create(
            crontab=start_crontab,
            name=f"expire_story_{instance.id}",
            task="products.tasks.create_story_expire_time",
            args=json.dumps(args),
            one_off=True
        )