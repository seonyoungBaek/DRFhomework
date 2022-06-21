from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise ValueError('Users must have an username')
        user = self.model(
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, password=None):
        user = self.create_user(
            username=username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField("사용자 계정", max_length=20, unique=True)
    email = models.EmailField("이메일 주소", max_length=100)
    password = models.CharField("비밀번호", max_length=128)
    fullname = models.CharField("이름", max_length=20)
    join_date = models.DateTimeField("가입일", auto_now_add=True)

    is_active = models.BooleanField(default=True) 

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = []
    
    objects = UserManager() 
    
    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label): 
        return True
    
    @property
    def is_staff(self): 
        return self.is_admin

class Hobby(models.Model):
    hobby=models.CharField("취미 이름", max_length=20, default='')

#user의 프로필을 저장하는 모델. 보안적인 이유 때문에 user모델과는 분리해 준다.
class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name="사용자", on_delete=models.CASCADE)
    #user는 하나밖에 없는 값이기 때문에 1대1 관계이다. 
    introduction = models.TextField("소개")
    birthday = models.DateField("생일")
    age = models.IntegerField("나이")
    hobby = models.ForeignKey(Hobby, verbose_name="취미", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username} 님의 프로필"