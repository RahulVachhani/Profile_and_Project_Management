from django.db import models
from users.models import Profile
# Create your models here.
['owner','title','discription','tags']
class Project(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    discription = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True,default='default.jpg',)
    created = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(null = True, blank=True ,default=0)
    vote_ratio = models.IntegerField(null=True, blank=True, default=0)
   
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-vote_ratio', '-votes', 'title']
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()

        ratio = (upVotes // totalVotes) * 100
        self.votes = totalVotes
        self.vote_ratio = ratio

        self.save()

class Review(models.Model):
    VOTE_TYPE = (
        ('up','Nice'),
        ('down', 'Not Good')
    ) 
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(max_length=2000,blank=True,null=True)
    value = models.CharField(max_length=200,choices=VOTE_TYPE,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.project.title + self.owner.name
    
    class Meta:
        unique_together = [['owner','project']]
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name