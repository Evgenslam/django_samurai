from django.urls import reverse
from unidecode import unidecode
from django.db import models
from django.utils.text import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Samurai.Status.PUBLISHED)


class Samurai(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='samurais')

    objects = models.Manager()
    published = PublishedManager()
    tags = models.ManyToManyField('PostTag', blank=True, related_name='samurais')
    lifework = models.OneToOneField('Lifework', on_delete=models.SET_NULL, null=True, blank=True, related_name='owner')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(' '.join(str(self.name).split()[:2])), allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Самурай'
        verbose_name_plural = 'Самураи'
        ordering = ["-time_create"]
        indexes = [
            models.Index(fields=["-time_create"])
        ]


class Lifework(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Дело жизни'
        verbose_name_plural = 'Дела'


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class PostTag(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'