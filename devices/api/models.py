# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import random

from django.db import models
from .utils import get_mac_48


class Devices(models.Model):
    DEV_TYPE_CHOICES = (('emeter', 'emeter'), ('zigbee', 'zigbee'), ('lora', 'lora'), ('gsm', 'gsm'))

    dev_id = models.CharField(max_length=200, default=get_mac_48())
    dev_type = models.CharField(max_length=120, choices=DEV_TYPE_CHOICES)

    class Meta:
        db_table = 'devices'

    def __str__(self):
        return f'ID : {self.pk} ; DEV_ID: {self.dev_id} ; DEV_TYPE: {self.dev_type}'


class Endpoints(models.Model):
    device = models.ForeignKey(Devices, on_delete=models.CASCADE, blank=True, null=True, related_name='endpoints')
    comment = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'endpoints'
