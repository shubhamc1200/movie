from django.db import models
from django.utils.text import slugify
# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField(unique=True)
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(default='default.png',blank='True')
    movie_url= models.URLField(blank=True)
    GENRE_CHOICES = ( ('Drama','Drama') ,('Action','Action'),('Scifi','Scifi'),('Thriller','Thriller'),('Horror','Horror'),('Anime','Anime') )
    genre=models.CharField(max_length=100,choices=GENRE_CHOICES)
    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

class Comment(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
