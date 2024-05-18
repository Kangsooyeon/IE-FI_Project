from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    # 일반 user 생성
    def create_user(self, email, id_name, nickname, birth, sex, main_bank, salary, asset, desired_asset, password=None):
        if not id_name:
            raise ValueError('must have user name')
        if not email:
            raise ValueError('must have user email')
        if not nickname:
            raise ValueError('must have user nickname')
        user = self.model(
            id_name = id_name,
            email = self.normalize_email(email),
            nickname = nickname,
            birth = birth,
            sex = sex,
            main_bank = main_bank,
            salary = salary,
            asset = asset,
            desired_asset = desired_asset,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 관리자 user 생성
    def create_superuser(self, email, id_name, nickname, birth, sex, main_bank, salary, asset, desired_asset, password=None):
        user = self.create_user(
            email,
            id_name = id_name,
            password = password,
            nickname = nickname,
            birth = birth,
            sex = sex,
            main_bank = main_bank,
            salary = salary,
            asset = asset,
            desired_asset = desired_asset,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    id_name = models.CharField(default='', max_length=30, null=False, blank=False, unique=True)
    email = models.EmailField(default='', max_length=30, null=False, blank=False, unique=True)
    nickname = models.CharField(default='', max_length=30, null=False, blank=False, unique=True)
    birth = models.IntegerField(null=True, blank=True)
    sex = models.IntegerField(null=True, blank=True)
    main_bank = models.CharField(max_length=30, null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    asset = models.IntegerField(null=True, blank=True)
    desired_asset = models.IntegerField(null=True, blank=True)


    
    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)
    
    # 헬퍼 클래스 사용
    objects = UserManager()

    # 사용자의 username field는 id_name으로 설정
    USERNAME_FIELD = 'id_name'
    # 필수로 작성해야하는 field
    REQUIRED_FIELDS = ['email', 'nickname']

    def __str__(self):
        return self.id_name