from django.db import models

# Create your models here.

class Actor(models.Model):
    firstname = models.CharField(max_length=255, verbose_name='Actor name')
    lastname = models.CharField(max_length=255 )
    age = models.IntegerField(default=0)

    def __str__(self):
        return  self.firstname+' '+self.lastname
    class Meta:
        ordering= ('firstname',)

class Review(models.Model):
    comment = models.TextField(default='my commentt:')
    creationDate= models.DateField(auto_now_add=True)
    movie= models.ForeignKey('Movie', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return 'review for {}'.format(self.movie)



class Movie(models.Model):
    name= models.CharField(max_length=255,unique=True,verbose_name='Movie name')
    description = models.TextField(default='movie def',null=True)
    likes = models.IntegerField(default=0,null=True)
    watchCount = models.IntegerField(default=0,null=True)
    rate = models.PositiveIntegerField(default=0,null=True)
    productionDate= models.DateField(null=True, blank=True)
    creationDate= models.DateField(auto_now_add=True)
    modificationDate= models.DateField(auto_now=True)
    actors= models.ManyToManyField('Actor')
    # poster= models.ImageField(upload_to='', null=True, blank=True)
    # video= models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self):
        return self.name


