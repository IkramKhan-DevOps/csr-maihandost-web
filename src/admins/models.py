import uuid

from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='No information provided for this country')
    is_available_for_sender = models.BooleanField(default=False)
    is_available_for_receiver = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class GiftCard(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/gifts/', null=True, blank=True)
    description = models.TextField(default='No information provided for this gift')
    price = models.FloatField(default=100)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Gift Cards'

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS_CHOICES = (
        ('unp', 'Un Paid'),
        ('pai', 'Paid'),
        ('fai', 'Failed'),
        ('com', 'Completed'),
        ('can', 'Cancelled'),
    )

    # TODO: generate a unique id for identification
    transaction_id = models.CharField(max_length=2000, null=False, blank=False, default=uuid.uuid4)
    sender_first_name = models.CharField(max_length=10, null=False, blank=False)
    sender_last_name = models.CharField(max_length=10, null=False, blank=False)
    sender_phone_number = models.CharField(max_length=10, null=False, blank=False)
    sender_email = models.CharField(max_length=10, null=False, blank=False)
    sender_country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='sender_country'
    )

    receiver_first_name = models.CharField(max_length=10, null=False, blank=False)
    receiver_last_name = models.CharField(max_length=10, null=False, blank=False)
    receiver_phone_number = models.CharField(max_length=10, null=False, blank=False)
    receiver_email = models.CharField(max_length=10, null=False, blank=False)
    receiver_country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='receiver_country'
    )

    total_amount = models.FloatField(default=0)
    tax_charges = models.FloatField(default=0)
    fees_charges = models.FloatField(default=0)
    payable_amount = models.FloatField(default=0)

    gift_card = models.ForeignKey(GiftCard, on_delete=models.SET_NULL, null=True, blank=True)
    stripe_pay_id = models.CharField(max_length=2000, null=True, blank=True)

    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='unp')
    is_active = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on', 'status']
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.pk)
