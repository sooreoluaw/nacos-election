from django.db import models

# Create your models here.


class Voter(models.Model):
    name = models.TextField()
    # TODO: Confirm actual max length
    identifier = models.CharField(max_length=15, verbose_name="Matric No.")
    photo = models.ImageField(verbose_name="Picture", null=True)
    has_voted = models.BooleanField(default=False)


class Poll(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)


class Nominee(models.Model):
    name = models.TextField()
    nickname = models.CharField(max_length=100)
    photo = models.ImageField()
    level = models.IntegerField(
        choices=((1, '100'), (2, '200'), (3, '300'), (4, '400'), (5, '500')))
    poll = models.ForeignKey(Poll, models.CASCADE, 'nominees')
    votes = models.IntegerField(default=0)
