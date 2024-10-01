from django.db import models
from slugify import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class CategoryModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Category name", unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class TagModel(models.Model):
    name = models.CharField(max_length=255, verbose_name="Tag name", unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class AuthorModel(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    avatar = models.ImageField(upload_to='news/authors/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class NewsModel(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="news/")
    description = RichTextUploadingField()
    status = models.BooleanField(default=False)
    views_count = models.PositiveBigIntegerField(default=0)

    author = models.ForeignKey(AuthorModel,
                               on_delete=models.SET_NULL,
                               related_name="news",
                               null=True)

    categories = models.ManyToManyField(CategoryModel, related_name="news")
    tags = models.ManyToManyField(TagModel, related_name="news")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.title)

        obj = NewsModel.objects.filter(slug=self.slug)
        counter = 1
        while obj.exists():
            self.slug = f"{self.slug}-{counter}"
            counter += 1
            obj = NewsModel.objects.filter(slug=self.slug)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"


class NewsCollectionModel(models.Model):
    types = (
        ("carousel", "carousel"),
        ("categorized", "categorized"),
    )

    news = models.ManyToManyField(NewsModel, related_name="collection")
    type = models.CharField(choices=types, max_length=128)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "News Collection"
        verbose_name_plural = "News Collections"


class ContactModel(models.Model):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.full_name} - {self.subject}"

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


class NewsletterModel(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Newsletter"
        verbose_name_plural = "Newsletters"
