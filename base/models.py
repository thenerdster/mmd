from django.db import models

# Create your models here.
class Characters(models.Model):
    class Meta:
        verbose_name_plural = "Characters"
    first_name = models.CharField(max_length=100, blank=False, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    bio = models.TextField(blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    net_worth = models.CharField(max_length=100, blank=False, null=True)
    relation = models.CharField(max_length=100, blank=False, null=True)
    alive = models.BooleanField(default=True)
    is_murderer = models.BooleanField(default=False)

    def __str__(self):
        return F"{self.first_name} {self.last_name}"

class Clues(models.Model):
    class Meta:
        verbose_name_plural = "Clues"
    name = models.CharField(max_length=100, blank=False, null=True,)
    location = models.CharField(max_length=100, blank=False, null=True)
    found = models.BooleanField(default=False)

    def __str__(self):
        return F"CLUE: {self.name}"

class Solves(models.Model):
    class Meta:
        verbose_name_plural = "Solves"
    name = models.CharField(max_length=100, blank=False, null=True)
    whodonit = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True, blank=True, null=True)


    def __str__(self):
        return F"{self.first_name} {self.last_name}"