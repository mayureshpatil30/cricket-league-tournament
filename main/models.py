from django.db import models
from django.urls import reverse


# Create your models here.

class Team(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    logo_url = models.ImageField(upload_to='images/teams/')
    club_state = models.CharField(max_length=32)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('main:team_details', args=[str(self.id)])


class Player(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    image_url = models.ImageField(upload_to='images/players/', default='images/players/default_image.png')
    player_jersey_no = models.SmallIntegerField()
    Country = models.CharField(max_length=32) # Country should be foegin key to a new table.
    matches = models.SmallIntegerField(default=0)
    run = models.SmallIntegerField(default=0)
    highest_score = models.SmallIntegerField(default=0)
    fifties = models.SmallIntegerField(default=0)
    hundreds = models.SmallIntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.lastname, self.team.name)
    
    def get_fullname(self):
        return "{} {}".format(self.firstname, self.lastname) 

# 
class Matches(models.Model):
    id = models.AutoField(primary_key=True)
    left_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team")
    right_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="oppsite_team")
    winner_team = models.CharField(max_length = 32)
    looser_team = models.CharField(max_length = 32)
    man_of_the_match = models.CharField(max_length = 32)
    bowler_of_the_match = models.CharField(max_length = 32 )

    class Meta:
        verbose_name_plural = "Matches"
#   
    def __str__(self):
        return "{} Vs {}".format(self.left_team.name, self.right_team.name)
    
    @property
    def get_left_team_name(self):
        return "".format(self.left_team.name)
    
    @property
    def get_right_team_name(self):
        return "".format(self.right_team.name)

class Venue(models.Model):
    id = models.AutoField(primary_key=True)
    ground_name =  models.CharField(max_length=32)

    def __str__(self):
        return self.ground_name