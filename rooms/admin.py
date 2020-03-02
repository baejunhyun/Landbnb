from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass
    # 이걸로 더 추가할 수 있음
    # 이걸 추가하면 예를 들어, RoomType admin panel에서 '+' 표시가 뜨고 그걸 눌러서 Entire Room부터 입력 시작

    # def used_by(self, obj):
    #    return obj.rooms.count()


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    # fieldsets, list_display, list_filter, search_fields, filter_horizontal --> 전부 메소드? ex) ModelAdmin.search_fields

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "city", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "city",
        "country",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
        # "count_photos",
        # "total_rating",
    )

    list_filter = (
        "instant_book",
        "host__superhost",  # 이건 정해진 거? 'host__'
        # "host__gender",  # 'gender'는 다른 데서 불러온 거?
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country",
    )

    search_fields = ("=city", "^host__username")  # 이 두 개 뜻???-->6.0강의에서

    filter_horizontal = ("amenities", "facilities", "house_rules")

    def count_amenities(self, obj):
        return obj.amenities.count()

    # 이거 왜 admin panel에 안 나옴? --> list_display에 넣어야 --> 함수이름이랑 같이 할 수 있음?


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):

    """ Photo Admin Definition """

    pass
