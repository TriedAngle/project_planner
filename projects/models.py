from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Project(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    lead = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    member_ids = ArrayField(models.IntegerField(), null=True, blank=True)
    members_count = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        mem_or_mems = ""
        if self.member_ids.__len__() <= 1:
            mem_or_mems = "member"
        else:
            mem_or_mems = "members"

        return f'{self.name + " with "+ str(self.member_ids.__len__()) + " " + mem_or_mems}'

    def get_lead(self):
        return self.lead_id


def set_member_count(sender, instance, **kwargs):
    instance.members_count = instance.member_ids.__len__()


post_save.connect(set_member_count, sender=Project)
