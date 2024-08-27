from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=40)
    full_name=models.CharField(max_length=40)
    job=models.CharField(max_length=40)
    def __str__(self) -> str:
        return f"{self.full_name} "

class Result(models.Model):
    name=models.CharField(max_length=20)
    full_name=models.CharField(max_length=40)
    date=models.DateTimeField()
    comment=models.CharField(max_length=20)
    def __str__(self):
        date_str = self.date.strftime("%H:%M") if self.date else "No date"
        return f"{self.full_name}      {self.comment}   {date_str}"
