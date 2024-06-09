from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Samurai.Status.PUBLISHED)


class Samurai(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, "черновик"
        PUBLISHED = 1, "опубликовано"

    name = models.CharField(
        max_length=255,
        verbose_name="имя",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="слаг",
    )
    content = models.TextField(
        blank=True,
        verbose_name="описание",
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name="создано",
    )
    time_update = models.DateTimeField(
        auto_now=True,
        verbose_name="обновлено",
    )
    is_published = models.BooleanField(
        choices=tuple((bool(x[0]), x[1]) for x in Status.choices),  # Костыль: переделываем 0, 1 в були
        default=Status.DRAFT,
        verbose_name="опубликовано",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.PROTECT,
        related_name="samurais",
        verbose_name="категория",
    )

    objects = models.Manager()
    published = PublishedManager()
    tags = models.ManyToManyField(
        to="PostTag",
        blank=True,
        related_name="samurais",
        verbose_name="теги",
    )
    lifework = models.OneToOneField(
        to="Lifework",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owner",
        verbose_name="дело жизни",
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(" ".join(str(self.name).split()[:2])), allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Самурай"
        verbose_name_plural = "Самураи"
        ordering = ["-time_create"]
        indexes = [models.Index(fields=["-time_create"])]


class Lifework(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="название",
    )
    description = models.TextField(
        blank=True,
        verbose_name="описание",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Дело жизни"
        verbose_name_plural = "Дела"


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="название",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="слаг",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"cat_slug": self.slug})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class PostTag(models.Model):
    tag = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name="название",
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        db_index=True,
        verbose_name="слаг",
    )

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("tag", kwargs={"tag_slug": self.slug})

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
