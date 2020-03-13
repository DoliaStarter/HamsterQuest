from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
# If no primary key doesn't specified in model,
# it means, that this field was added b default by django
# with name 'id' and type Serial.


class UserProfile(models.Model):

    author_rating = models.IntegerField(default=0,
                                        validators=[MinValueValidator(0)],
                                        help_text="Rating of user based on quests he authored")

    player_rating = models.IntegerField(default=0,
                                        validators=[MinValueValidator(0)],
                                        help_text="Rating of user based on quests he played")

    user = models.OneToOneField(User, models.CASCADE)


class Quests(models.Model):

    author_id = models.ForeignKey(to=UserProfile,
                                  on_delete=models.SET_NULL,
                                  to_field='id',
                                  null=True)
    description = models.TextField(blank=True,
                                   help_text='Describe current quest')


class Sessions(models.Model):
    player_id = models.ForeignKey(to=UserProfile,
                                  on_delete=models.CASCADE,
                                  to_field='id')
    quest_id = models.ForeignKey(to=Quests,
                                 on_delete=models.CASCADE,
                                 to_field='id')

    start_time = models.DateTimeField()
    is_active = models.BooleanField(default=False,
                                    help_text='Shows if session is currently running')
    # Hack to create compound primary key.
    # Used because Django doesn't support them by default

    class Meta:
        unique_together = ('player_id', 'quest_id')


# Create your models here.
class Stages(models.Model):
    quest_id = models.ForeignKey(to=Quests,
                                 on_delete=models.CASCADE,
                                 to_field='id')
    previous_stage = models.ForeignKey(to='Stages',
                                       on_delete=models.SET_NULL,
                                       to_field='id',
                                       null=True)
    latitude = models.DecimalField(max_digits=15,
                                   decimal_places=12)

    longitude = models.DecimalField(max_digits=15,
                                    decimal_places=12)

    type_of_answer = models.CharField(max_length=100,
                                      blank=False)

    answer = models.CharField(max_length=255,
                              blank=False)

    description = models.TextField(blank=False)


class Tags(models.Model):
    quest_id = models.ForeignKey(to=Quests,
                                 on_delete=models.CASCADE,
                                 to_field='id')
    tag_name = models.CharField(max_length=100,
                                blank=False)
