import uuid

from django.db import models
from datetime import datetime
from enum import Enum

# Create your models here.
class Rating(models.Model):
	id = models.UUIDField(primary_key=True, null=False, unique=True, default=uuid.uuid4(), verbose_name="Id")
	average = models.DecimalField(null=False, decimal_places=2,max_digits=3, verbose_name="Average")
	createdAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="CreatedAt")
	updatedAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="UpdatedAt")
	isDeleted = models.BooleanField(default=False)
	class Meta:
		db_table = "rating"


class Movie(models.Model):
	id = models.UUIDField(primary_key=True, null=False, unique=True, default=uuid.uuid4(),verbose_name="Id")
	name = models.CharField(max_length=200, null=False, verbose_name="Name")
	isDeleted = models.BooleanField(default=False)
	url = models.TextField(null=True, blank=True, verbose_name="URL")
	image = models.TextField(null=True, blank=True, verbose_name="Image")
	createdAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="CreatedAt")
	updatedAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="UpdatedAt")
	language = models.CharField(max_length=200, null=False, verbose_name="Language")
	summary = models.TextField(null=True, blank=True, verbose_name="Summary")
	#ratingId = models.ForeignKey(Rating,blank=True,null=True,on_delete=models.CASCADE)
	class Meta:
		db_table = "movie"

class Comment:
	id = models.UUIDField(primary_key=True, null=False, unique=True, default=uuid.uuid4(), verbose_name="Id")
	isDeleted = models.BooleanField(default=False)
	username = models.CharField(max_length=200, null=False, verbose_name="UserName")
	description = models.CharField(max_length=200, null=False, verbose_name="Description")
	createdAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="CreatedAt")
	updatedAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="UpdatedAt")
	comment = models.TextField(null=True, blank=True, verbose_name="Comment")
	movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)

class ReactionType(Enum):

    LIKE = 'like'

    LOVE = 'love'

    CARE = 'Care'

class Reaction:
	id = models.UUIDField(primary_key=True, null=False, unique=True, default=uuid.uuid4(), verbose_name="Id")
	isDeleted = models.BooleanField(default=False)
	type = models.CharField(max_length=200, null=False, verbose_name="Type")
	createdAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="CreatedAt")
	updatedAt = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name="UpdatedAt")
	movieId = models.ForeignKey(Movie, on_delete=models.CASCADE)


