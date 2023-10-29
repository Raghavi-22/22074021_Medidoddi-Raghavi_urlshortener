from django.db import models

# Create your models here.
from django.db import models
import random
import string

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

class URL(models.Model):
    long_url = models.URLField(max_length=5000)
    short_code = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = generate_short_code()
        super().save(*args, **kwargs)
