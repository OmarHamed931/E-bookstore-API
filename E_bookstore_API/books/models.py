from django.db import models
from category.models import Category 

def upload_location(instance, filename):
    return f"book_cover/{instance.title}/{filename}"
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    published_at = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = models.ImageField(upload_to=upload_location, null=True, blank=True)
    category = models.ManyToManyField(Category, verbose_name=("categories"), related_name='books')

    
    def __str__(self):
        return self.title
    
# Create your models here.
