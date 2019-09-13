from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    parent_field = models.IntegerField(default=0)

    class Meta:
        db_table = "categories"