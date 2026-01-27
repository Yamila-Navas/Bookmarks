from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_likied', blank=True)

    class Meta:
        indexes = [models.Index(fields=['created'])]
        ordering = ['-created']

    def __str__(self):
        return self.title
    
    def save(self, *arg, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*arg, **kwargs)
    
    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
    

    
