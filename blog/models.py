from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from unidecode import unidecode



class Post(models.Model):
    slug = models.SlugField(blank=True, null=True, max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-detail', kwargs={
            'pk': self.pk,
            'slug': self.slug
        })
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super(Post, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse("post-detail", kwargs={"pk": self.pk})
    