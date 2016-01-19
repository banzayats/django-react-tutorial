from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import hashlib


@python_2_unicode_compatible
class Comment(models.Model):
    id = models.CharField(primary_key=True, editable=False, max_length=100)
    author = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return '{0}: {1}...'.format(self.author, self.text[:20])

    def save(self, *args, **kwargs):
        self.id = hashlib.md5(self.text).hexdigest()
        super(Comment, self).save(*args, **kwargs)
