from django.db import models
from django.utils.timezone import now
from autoslug import AutoSlugField


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.URLField()
    release_date = models.DateField(default=now())
    lte_exists = models.BooleanField(default=None)
    slug = AutoSlugField(populate_from='name', unique=True)
    pass
