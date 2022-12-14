# Generated by Django 4.1.2 on 2022-11-02 21:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('test_movies', '0002_movie_ratingid_alter_movie_id_alter_rating_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c75e5145-c630-4649-80e9-46ae77e9e642'), primary_key=True, serialize=False, unique=True, verbose_name='Id'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.TextField(blank=True, null=True, verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.TextField(blank=True, null=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3aad699c-54f7-482b-8e08-cd7fba2d2789'), primary_key=True, serialize=False, unique=True, verbose_name='Id'),
        ),
    ]
