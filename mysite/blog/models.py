from django.conf import settings
from django.db import models
from django.urls import reverse
from mysite.utils import uuid_upload_to


class DevTool(models.Model):
    name = models.CharField(max_length=50, verbose_name='>>이름')
    kind = models.CharField(max_length=50, verbose_name='>>종류')
    content = models.TextField(blank=True, verbose_name='>>개발툴 설명')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.pk}> {self.name}'

    def get_absolute_url(self):
        return reverse("blog:devtool_detail", kwargs={'pk': self.pk})

class Idea(models.Model):
    name = models.CharField(max_length=100, verbose_name='>>아이디어명')
    photo = models.ImageField(blank=True, upload_to = uuid_upload_to, verbose_name='>>대표사진')
    desc = models.TextField(blank=True, verbose_name='>>아이디어 설명')
    intrest = models.PositiveIntegerField(verbose_name='>>아이디어 관심도')
    devtool = models.ForeignKey(DevTool, related_name='ideas', on_delete=models.CASCADE, verbose_name='>>예상 개발툴')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<{self.pk}> {self.name}'

    def get_absolute_url(self):
        return reverse("blog:idea_detail", kwargs={'pk': self.pk})



