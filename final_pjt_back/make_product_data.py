import os
import random
from faker import Faker
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_pjt.settings')
application = get_wsgi_application()

from accounts.models import User
from products.models import DepositOptions, SavingOptions, SubscribedDepositProducts, SubscribedSavingProducts

fake = Faker()

def create_subscribed():
    deposit_options = list(DepositOptions.objects.all())
    saving_options = list(SavingOptions.objects.all())

    for user in User.objects.all():
        user_deposit_options = deposit_options.copy()
        user_saving_options = saving_options.copy()

        for _ in range(random.randint(1, 5)):  # Each user can have up to 5 SubscribedDepositProducts
            if not user_deposit_options:  # If the user has already subscribed to all deposit options, break
                break
            chosen_deposit_option = random.choice(user_deposit_options)
            SubscribedDepositProducts.objects.create(
                user=user,
                deposit_option=chosen_deposit_option,
                sign_money=random.randrange(10000, 50000000, 10000),
                mtrt_money=random.randrange(10000, 50000000, 10000),
            )
            user_deposit_options.remove(chosen_deposit_option)  # Remove the chosen option from the user's available options

        for _ in range(random.randint(1, 5)):  # Each user can have up to 5 SubscribedSavingProducts
            if not user_saving_options:  # If the user has already subscribed to all saving options, break
                break
            chosen_saving_option = random.choice(user_saving_options)
            SubscribedSavingProducts.objects.create(
                user=user,
                saving_option=chosen_saving_option,
                sign_money=random.randrange(10000, 50000000, 10000),
                mtrt_money=random.randrange(10000, 50000000, 10000),
            )
            user_saving_options.remove(chosen_saving_option)  # Remove the chosen option from the user's available options

create_subscribed()