from django.db import models
from django.utils import timezone
from core import models as core_models

# Create your models here.


class Reservation(core_models.TimeStampedModel):

    """ Reservation Model Definition """

    STATUS_PENDING = "pending"
    STATUS_CONFIRMED = "confirmed"
    STATUS_CANCELLED = "cancelled"

    STATUS_CHOICES = (
        (STATUS_PENDING, "Pending"),
        (STATUS_CONFIRMED, "Confirmed"),
        (STATUS_CANCELLED, "Cancelled"),
    )

    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default=STATUS_PENDING
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guest = models.ForeignKey("users.User", on_delete=models.CASCADE)
    room = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)
    # rooms.Room에 "" --> ???
    # "users.User" --> ???

    def __str__(self):
        return f"{self.room} - {self.check_in}"

    # 이건 근데, 어디서 어떻게 보이는 거?

    def in_progress(self):
        now = timezone.now().date()
        return now > self.check_in and now < self.check_out

    # in_progress.boolean = True --> ???

    def is_finished(self):
        now = timezone.now().date()
        return now > self.check_out

    # is_finished.boolean = True --> ???

