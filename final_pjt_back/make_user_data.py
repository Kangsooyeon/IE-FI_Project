import os
import random
from faker import Faker
from django.core.wsgi import get_wsgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_pjt.settings')
application = get_wsgi_application()

from accounts.models import User

fake = Faker()

banks = [
    '우리은행',
    '한국스탠다드차타드은행',
    '대구은행',
    '부산은행',
    '광주은행',
    '제주은행',
    '전북은행',
    '경남은행',
    '중소기업은행',
    '한국산업은행',
    '국민은행',
    '신한은행',
    '농협은행주식회사',
    '하나은행',
    '주식회사 케이뱅크',
    '수협은행',
    '주식회사 카카오뱅크',
    '토스뱅크 주식회사',    
  ]

def create_users(n):
    for _ in range(n):
        id_name = fake.unique.user_name()
        email = fake.unique.email()
        nickname = fake.unique.first_name()
        birth = fake.date_of_birth(minimum_age=17, maximum_age=80).strftime("%y%m%d")
        sex = random.choice([1,2])
        main_bank = random.choice(banks)
        salary = random.randrange(0, 200000000, 1000000)
        asset = random.randrange(0, 1000000000, 100000)
        desired_asset = random.randrange(0, 10000000000, 10000000)
        password = 'test1234!'
        
        User.objects.create_user(
            email=email,
            id_name=id_name,
            nickname=nickname,
            birth=birth,
            sex=sex,
            main_bank=main_bank,
            salary=salary,
            asset=asset,
            desired_asset=desired_asset,
            password=password
        )

create_users(100)