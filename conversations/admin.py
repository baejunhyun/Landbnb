from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """ Message Admin Definition """

    list_display = ("__str__", "created")
    # __str__ --> 'MESSAGE'라고 뜸, 근데 이렇게 "__str__"라고 쓰는 것이 정해졌음?
    # 만약 다른 이름으로 하고 싶으면 어떻게 정함?


@admin.register(models.Conversation)
class ConversationAdmin(admin.ModelAdmin):

    """ Conversation Admin Definition """

    # list_display = ("__str__", "count_messages", "count_participants")
    # 이는 또 왜 이럼?
