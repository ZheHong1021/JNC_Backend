from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('作者', max_length=255)
    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)
    class Meta:
        db_table = 'authors'
        ordering = ('created_at',)

# Create your models here.
class Book(models.Model):
    title = models.CharField('Token使用的場', max_length=255)
    author_id = models.ForeignKey(
        Author,
        related_name="books",
        db_column="author_id",
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField("創立時間", auto_now_add=True)
    updated_at = models.DateTimeField("修改時間", auto_now=True)
    class Meta:
        db_table = 'books'
        ordering = ('created_at',)
