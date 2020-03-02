from django.db import models
from core import models as core_models

# Create your models here.


class Conversation(core_models.TimeStampedModel):

    """ Conversation Model Definition """

    participants = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        return str(self.created)

    # self.created --> list로... 근데 왜? 이 부분이 몇강이었지???
    # 이 created 어디서부터 이끌어져 나온 것?

    # 한 개의 대화안에 많은 메세지들

    """
    8.2 코드
    """


class Message(core_models.TimeStampedModel):

    """ Message Model Definition """

    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says: {self.message}"

