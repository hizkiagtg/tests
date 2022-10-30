from django.db import models
from django.contrib.auth.models import AbstractUser, User, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password):
        if not email:
            raise ValueError('The given email must be set')
        
        email = self.normalize_email(email)
        user = self.model(
			email=email,
		)
        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_superuser(self, email, password):
        email = self.normalize_email(email)
        
        user = self.create_user(
			email=email,
			password=password,
		)

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    username = models.CharField(max_length = 20, blank = True, null = True, unique = True)
    email = models.EmailField(verbose_name="email", max_length=50, unique=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    address = models.TextField(null=True)
    score = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)

    is_regular = models.BooleanField(default=False)
    is_bank = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    user = UserManager()

    def add_score(self,score):
        self.score += score

    def add_weight(self,weight):
        self.weight += weight

    def __str__(self):
        return "{}".format(self.email)
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    
# class Regular(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

#     def __str__(self):
#         return str(self.username)

# class Bank(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
#     add_fieldsets = (
#             (None, {'fields': ('email', 'username', 'city',)}),
#     )

#     def __str__(self):
#         return str(self.institute_name)
