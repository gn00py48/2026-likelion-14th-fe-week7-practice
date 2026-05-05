from django.db import models


class PracticeUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Review(models.Model):
    reviewer_name = models.CharField(max_length=30)
    star = models.IntegerField()
    content = models.TextField()
    photo = models.ImageField(upload_to="reviews/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} - {self.star}점"