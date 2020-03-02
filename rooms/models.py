from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

# from users import models as user_models

# host랑 연결하기 위해

# Create your models here.


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    """ RoomType Model Definition """

    pass

    class Meta:
        verbose_name = "Room Type"
        ordering = ["name"]
        # 근데, 왜 이걸 models.py에 씀? admin.py는 그냥 등록용? 패널을 구성하고 디자인하는데만?


class Amenity(AbstractItem):

    """ Amenity Model Definition """

    pass

    class Meta:
        verbose_name_plural = "Amenities"


class Facility(AbstractItem):

    """ Facility Model Definition """

    pass

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    pass

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimeStampedModel):

    # 원래 class Room(models.Model):
    # created = models.DateTimeField()
    # updated = models.DateTimeField()
    # 이들을 계속 복사해서 다른 곳에 넣지 않기 위해 core 이용
    # core_models.가 더 좁은 것 같은데, 이를 상속받음? 쉽게 생각하면 그냥 ()안의 클래스 메소드를 직접 가져와서 쓰겠다는 것?

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # room_type = models.ManyToManyField(RoomType, blank=True)
    # 근데, 이들이 어떻게 바로 admin 패널에 나옴? 지금 admin.py에 뭐를 하기 전인데...
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)
    # 강의 4.5 코드 살펴볼 것

    def __str__(self):
        return self.name

    # 근데 name은 이미 문자열 아닌가...? 당최 이 의미는...?
    # 이걸 안 쓰면 Room1(?), 이런 식으로 뜨는데, 위에 클래스 이름을 받는 것이 디폴트 값인가?
    # 근데, 이걸 안 써도 입력한 이름으로 나오는데?

    """
    def total_rating(self):
        all_reviews = self.reviews.all()
        # self.name = name 이랑 순서가 반대? 이거 물어봐야 할 듯
        # 근데 reviews은 당최 어디에?
        all_ratings = 0
        for review in all_reviews:
            all_ratings.append(review.rating_average())
        return 0
    """
    # 8.0, 8,1 수업 + 코드 확인
