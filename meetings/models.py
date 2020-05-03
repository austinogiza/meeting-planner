from django.db import models
from datetime import  date, time
# Create your models here.


class Meetings(models.Model):
    title = models.CharField(max_length=500)
    date = models.DateField()
    start_time = models.TimeField()
    duration = models.IntegerField()
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} at {self.start_time} on {self.date}"
    class Meta:
        verbose_name_plural = 'Meetings'


class Room(models.Model):
    name = models.CharField(max_length=500)
    floor_number = models.IntegerField()
    room_number = models.IntegerField()

    def __str__(self):
        return f"{self.name}: room {self.room_number} on {self.floor_number}"