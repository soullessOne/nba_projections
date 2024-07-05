from django.db import models

class Team(models.Model):
    team_name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="media/logos/")

    def __str__(self):
        return self.team_name
