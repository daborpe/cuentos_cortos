# coding: utf-8
from __future__ import unicode_literals
import os
import uuid
from django.db import models


def get_uuid():
    return uuid.uuid4().hex


def file_path(instance, filename):
    ext = os.path.splitext(filename)
    return '{}{}'.format(get_uuid(), ext)


class Cuento(models.Model):
    title = models.CharField('Título', max_length=30)
    beginning = models.TextField('Inicio')
    middle = models.TextField('Desarrollo')
    end = models.TextField('Final')
    storyimage = models.ImageField('Imagen del cuento', upload_to=file_path)
    active = models.BooleanField(default=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "Cuento"
        verbose_name_plural = "Cuentos"
