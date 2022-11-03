import uuid

from django.db import models
from datetime import datetime
from enum import Enum
import array


# Create your models here.
class Rating(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True, default=uuid.uuid4(), verbose_name="Id")
    average = models.DecimalField(null=False, decimal_places=2, max_digits=3, verbose_name="Average")
    createdAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="CreatedAt")
    updatedAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="UpdatedAt")
    isDeleted = models.BooleanField(default=False)

    class Meta:
        db_table = "rating"


class Movie(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True, default=uuid.uuid4(), verbose_name="Id")
    name = models.CharField(max_length=200, null=False, verbose_name="Name")
    isDeleted = models.BooleanField(default=False)
    url = models.TextField(null=True, blank=True, verbose_name="URL")
    image = models.TextField(null=True, blank=True, verbose_name="Image")
    createdAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="CreatedAt")
    updatedAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="UpdatedAt")
    language = models.CharField(max_length=200, null=False, verbose_name="Language")
    summary = models.TextField(null=True, blank=True, verbose_name="Summary")
    ratingId = models.UUIDField(null=False, )
    class Meta:
        db_table = "movie"

    def getLikes(self):
        movie_reactions = Reaction.objects.filter(movieId=self.id)
        count=0
        for reaction in movie_reactions:
            if reaction.type=='like':
                count=count+1
        return count

    def getRating(self):
        rating = Rating.objects.get(id=self.ratingId)
        return rating.average

    def getLoves(self):
        movie_reactions = Reaction.objects.filter(movieId=self.id)
        count=0
        for reaction in movie_reactions:
            if reaction.type=='love':
                count=count+1
        return count

    def getCare(self):
        movie_reactions = Reaction.objects.filter(movieId=self.id)
        count=0
        for reaction in movie_reactions:
            if reaction.type=='care':
                count=count+1
        return count

    def getSad(self):
        movie_reactions = Reaction.objects.filter(movieId=self.id)
        count=0
        for reaction in movie_reactions:
            if reaction.type=='sad':
                count=count+1
        return count

    def getHaha(self):
        movie_reactions = Reaction.objects.filter(movieId=self.id)
        count=0
        for reaction in movie_reactions:
            if reaction.type=='haha':
                count=count+1
        return count

    def getAngry(self):
        movie_reactions = Reaction.objects.filter(movieId=self.id)
        count=0
        for reaction in movie_reactions:
            if reaction.type=='angry':
                count=count+1
        return count

    def getWow(self):
        movie_reactions = Reaction.objects.filter(movieId=self.id)
        count=0
        for reaction in movie_reactions:
            if reaction.type=='wow':
                count=count+1
        return count

class ReactionType(Enum):
    LIKE = 'like'
    LOVE = 'love'
    CARE = 'care'
    HAHA = 'haha'
    WOW = 'wow'
    SAD = 'sad'
    ANGRY = 'angry'


class Reaction(models.Model):
    id = models.UUIDField(primary_key=True, null=False, unique=True, default=uuid.uuid4(), verbose_name="Id")
    isDeleted = models.BooleanField(default=False)
    type = models.CharField(max_length=200, null=False, verbose_name="Type")
    createdAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="CreatedAt")
    updatedAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="UpdatedAt")
    movieId = models.UUIDField(null=False, )

    class Meta:
        db_table = "reaction"
