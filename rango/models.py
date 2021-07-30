from django.db import models

class Category(models.Model):
    NAME_MAX_LENGTH = 128
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
   

    class Meta:
        verbose_name_plural =  'Categories'
        
    def __str__(self):
        return self.name

class Page(models.Model):
    TITLE_MAX_LENGTH = 200
    URL_MAX_LENGTH = 250
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharFieldmax_length=TITLE_MAX_LENGTH)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title