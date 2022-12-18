from django.db import models
from django.conf import settings
from django.utils import timezone


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField(blank=True, null=True)

    # age = models.IntegerField
    # birth_year = models.IntegerField
    #
    # def get_year(self):
    #     self.birth_year = self.birth_date.strftime('%Y')
    #     self.save()
    #
    # def age_calc(self):
    #     self.age = 2022 - self.birth_year
#

