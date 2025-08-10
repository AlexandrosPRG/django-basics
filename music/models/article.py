from django.db import models

class Article(models.Model):
    class Status(models.TextChoices):
        IN_WRITING = "in_writing", "in writing"
        PENDING   = "pending_editor_approval", "pending editor approval"
        PUBLISHED = "published", "published"

    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True, blank=True)
    content = models.TextField()

    date_added = models.DateTimeField(auto_now_add=True)  # при первом сохранении

    status = models.CharField(
        max_length=32,
        choices=Status.choices,
        default=Status.IN_WRITING,
    )
    publish_date = models.DateTimeField(null=True, blank=True)
    removal_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_added"]