from django.db import models, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

class Item(models.Model):
    name = models.CharField(max_length=50)

@receiver(post_save, sender=Item)
def signal_receiver(sender, instance, **kwargs):
    Item.objects.create(name="From signal")

with transaction.atomic():
    Item.objects.create(name="Main object")
    raise Exception("Rollback everything")



