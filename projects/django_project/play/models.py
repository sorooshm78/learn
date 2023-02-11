from django.db import models
from django.db.models import Q


class RoomManager(models.Manager):
    def active(self):
        return super().get_queryset().filter(is_active=True)

    def empty_rooms(self):
        return self.active().filter(Q(user1=None) | Q(user2=None))

    def create_room(self, user):
        room = self.empty_rooms().first()
        if not room:
            room = super().create(user1=user)
        else:
            room.user2 = user
            room.save()

        return room


class RoomGameModel(models.Model):
    user1 = models.CharField(max_length=30, blank=True, null=True)
    user2 = models.CharField(max_length=30, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # turn = models.CharField(max_length=30)

    rooms = RoomManager()

    def is_empty(self):
        if self.user1 is not None and self.user2 is not None:
            return False
        return True
