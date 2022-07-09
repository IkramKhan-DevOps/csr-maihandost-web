import uuid

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from src.accounts.models import User


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
    commission = models.FloatField(default=1.1, help_text="Commission for maihandost services")
    description = models.TextField(default='No information provided for this gift')
    price = models.FloatField(default=100)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = 'Gift Cards'

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)
    charges = models.FloatField(default=0)
    description = models.CharField(max_length=100, default='Description not provided yet.')

    is_figure = models.BooleanField(default=False, help_text="Figure means not in %")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS_CHOICES = (
        ('unp', 'Un Paid'),
        ('pai', 'Paid'),
        ('fai', 'Failed'),
        ('pen', 'Pending'),
        ('com', 'Completed'),
        ('can', 'Cancelled'),
    )

    # TODO: generate a unique id for identification
    transaction_id = models.CharField(max_length=2000, null=False, blank=False, default=uuid.uuid4)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=False)

    # RECEIVER
    receiver_first_name = models.CharField(max_length=10, null=False, blank=False)
    receiver_last_name = models.CharField(max_length=10, null=False, blank=False)
    receiver_phone_number = PhoneNumberField()
    receiver_email = models.EmailField(null=False, blank=False)
    receiver_country = models.ForeignKey(
        Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='receiver_country'
    )

    # CALCULATIONS
    total_amount = models.FloatField(default=0)
    tax_charges = models.FloatField(default=0)
    fees_charges = models.FloatField(default=0)
    payable_amount = models.FloatField(default=0)

    # MISC
    stripe_pay_id = models.CharField(max_length=2000, null=True, blank=True)

    # CHOICES AND KEYS
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='unp')
    payment_method = models.ForeignKey(PaymentMethod, null=True, blank=True, on_delete=models.SET_NULL)
    gift_card = models.ForeignKey(GiftCard, on_delete=models.SET_NULL, null=True, blank=True)

    # STATUS
    is_customized = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    # IMPORTANT DATES
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    closed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff')
    closed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['created_on', 'status']
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.pk)
