from src.accounts.models import User, AdminWallet
from faker import Faker
import datetime
from django.utils import timezone
from dateutil.relativedelta import relativedelta
from src.api.models import AlertMessage, Subscription

fake = Faker()


def initialization(init=True, mid=True, end=True):

    if init:
        create_users()

    if mid:
        create_basics()

    if end:
        create_others()


def create_users():
    print()
    print("----- BUILDING USERS STARTED  ------")

    user_names = [
        'u1', 'u2', 'u3', 'user1', 'user2', 'user3', 'user4', 'user5',
        'user6', 'user7', 'user8', 'user9', 'user10'
    ]

    for name in user_names:
        if not User.objects.filter(username=name):
            user = User.objects.create_user(username=name, email=f'{name}@exarth.com', password='poiuyt098765',
                                            phone_number='03000000000')
            user.first_name = fake.first_name()
            user.last_name = fake.last_name()
            user.phone_number = fake.phone_number()
            user.save()

            print(f"  -- User {user.username} Created")
        else:
            print(f"  -- User {name} already exists.")

    print("----- BUILDING USERS FINISHED ------")


def create_basics():
    print()
    print("----- BUILDING WAL/MES STARTED  ------")

    wallets = ['Binance', 'Trust Wallet']
    messages = ['Message 1 is first test message', 'Message 2 is second test message']

    if not AdminWallet.objects.count() > 0:
        for wallet in wallets:
            admin_wallet = AdminWallet.objects.create(name=wallet, description='*', detailed_description='*',
                                                      address=fake.unique.random_int())
            print(f"  -- Wallet {wallet} Created")

        for message in messages:
            alert_message = AlertMessage.objects.create(title='Message!', description=message)
            print(f"  -- Message Created")
    else:
        print(f"  -- Wallets and Messages already exists")

    print("----- BUILDING USERS FINISHED ------")


def create_others():
    print()
    print("----- BUILDING SUBSCRIPTION STARTED  ------")

    for user in User.objects.filter(is_staff=False):
        print(f"  -- User {user} subscriptions.")

        for index in range(2):
            subscription = Subscription.objects.create(
                wallet_type=AdminWallet.objects.order_by('?')[0], user=user,
                tx_id=fake.unique.random_int(), amount=200, subscription_status='pen',
                expires_on=timezone.now() + relativedelta(months=4)
            )
            print(f"    -- Subscription of {subscription.amount} created.")

    print("----- BUILDING SUBSCRIPTION FINISHED ------")