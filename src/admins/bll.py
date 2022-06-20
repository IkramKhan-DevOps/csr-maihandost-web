from dateutil.relativedelta import relativedelta
from django.db.models import Q, Sum, Count
from notifications.signals import notify

from src.accounts.models import User, UserStatistics
from datetime import date
from src.api.models import Subscription, Withdrawal, Profit
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


def customer_subscription():
    pass


def subscription_check(request):
    response_error = True
    response_message = "something wrong with this request"

    return response_error, response_message


def calculate_profit_today(user):
    response_error = True
    response_message = "something wrong with this request"

    return response_error, response_message
