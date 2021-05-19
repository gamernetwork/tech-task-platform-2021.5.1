from django.db import models


class Category(models.Model):
    slug = models.SlugField(
        unique=True,
    )
    title = models.CharField(
        max_length=200,
    )

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Post(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    slug = models.SlugField(
        unique=True,
    )
    title = models.CharField(
        max_length=1000,
    )
    meta_description = models.CharField(
        max_length=160,
        null=True,
        blank=True,
    )
    body = models.TextField()
    is_featured = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.title
