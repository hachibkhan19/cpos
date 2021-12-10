from django.db import models
from django.contrib.auth.models import User

SUPER_ADMIN = 1
ORG_ADMIN = 2

USER_TYPE = (
    (SUPER_ADMIN, 'Super admin'),
    (ORG_ADMIN, 'Organization admin')
)

# Create your models here.
class Division(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    division = models.ForeignKey(Division, related_name='cities', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Area(models.Model):
    city =models.ForeignKey(City, related_name='areas', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_full_location(self):
        division = self.city.division.name
        city = self.city.name
        # return f'{self.division} {self.city} {self.name}'        
        return '{}, {}, {}'.format(division, city, self.name)

class UserInformation(models.Model):
    user = models.OneToOneField(User, related_name='user_informaton', on_delete=models.CASCADE)    
    org_name = models.CharField(max_length=50, null=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE, default=ORG_ADMIN)
    phone_number = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)


    def __str__(self):
        return self.org_name

