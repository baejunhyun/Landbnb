from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_KOREAN = "kr"
    LANGUAGE_FINNISH = "fi"
    LANGUAGE_ENGLISH = "en"

    LANGUAGE_CHOICES = (
        (LANGUAGE_KOREAN, "Korean"),
        (LANGUAGE_FINNISH, "Finnish"),
        (LANGUAGE_ENGLISH, "English"),
    )

    CURRENCY_KRW = "krw"
    CURRENCY_EUR = "eur"
    CURRENCY_USD = "usd"

    CURRENCY_CHOICES = (
        (CURRENCY_KRW, "KRW"),
        (CURRENCY_EUR, "EUR"),
        (CURRENCY_USD, "USD"),
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)

    # def __str__(self):
    #    return self.username
    # 그러니까 여기서 username이 어디에서 나온 거임?

