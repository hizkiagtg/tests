from django.db import models
from accounts.models import User

# Create your models here.
class Question(models.Model):
    author = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=False)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 

    def get_responses(self):
        return self.responses.filter(parent=None)

class Answer(models.Model):
    user = models.ForeignKey(User, null=False, on_delete = models.CASCADE)
    body = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body

    def get_responses(self):
        return Answer.objects.filter(parent=self)

    