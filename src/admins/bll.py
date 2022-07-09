from dateutil.relativedelta import relativedelta
from django.db.models import Q, Sum, Count
from notifications.signals import notify

from src.accounts.models import User, UserStatistics
from datetime import date
import calendar
import datetime
from django.utils import timezone


def calculate_statistics(context):
    """"
    1 tasks [today]
    2 registrations [year, month, today, free, premium]
    3 subscriptions [year, month, today, pending, applied, approved]
    4 withdrawals [year, month, today, pending, approved]
    5 Payments status [cash_in, cash_out]
    """
    return context


def get_month_days():
    now = datetime.datetime.now()
    days = calendar.monthrange(now.year, now.month)[1]
    return days


def calculate_charges_on_order(amount):
    # CHECKS PAYMENT METHOD CHECK HERE
    # --------------------------------

    payable = ((5 / 100) * amount) + amount
    tax = ((5 / 100) * amount)
    charges = ((5 / 100) * amount)

    return payable, tax, charges

