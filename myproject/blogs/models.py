from django.db import models
from category.models import Category

# Create your models here.
class Blogs(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    
    # access category's data
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    writer = models.CharField(max_length=255)
    
    # number of reader(s)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blogImages', blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
