from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import gettext_lazy as _


# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    profile_photo = models.ImageField(verbose_name=_('user profilr photo'), upload_to='profile_photos/', null=True, blank=True)
    bio = models.TextField(verbose_name=_('user bio'), max_length=500, blank=True)
    interests = models.ManyToManyField('Interest', verbose_name=_('user interests'), related_name='users', blank=True)
    skills = models.ManyToManyField('Skill', verbose_name=_('user skills'), related_name='users', blank=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        db_table = 'User'

    def __str__(self):
        if self.first_name and self.last_name:
            full_name = '%s %s' % (self.first_name, self.last_name)
            return full_name.strip()
        else:
            username = '%s' % self.username
            return username.strip()

class Interest(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_('interest name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _("Interest")
        verbose_name_plural = _("Interests")
        db_table = 'Interest'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Interest, self).save(*args, **kwargs)

class Skill(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_('skill name'), max_length=255, unique=True)

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")
        db_table = 'Skill'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(Skill, self).save(*args, **kwargs)