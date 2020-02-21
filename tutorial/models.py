from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

from . import choices


class Junta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='junta')
    profile_pic = models.ImageField(blank=True)
    role = models.CharField(max_length=32, choices=choices.ROLES_CHOICES, default=choices.VOTER)

    def image_tag(self):
        from django.utils.html import escape, format_html
        try:
            return format_html('<img src="%s" width="150" height="150"/>' % escape(self.profile_pic.url))
        except ValueError:
            return format_html('No profile pic')

    image_tag.short_description = user
    image_tag.allow_tags = True

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)
