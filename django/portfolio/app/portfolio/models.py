from distutils.command.upload import upload
from pydoc import describe
from django.db import models
from django.forms import CharField


class Profile(models.Model):

    name = models.CharField('名前', max_length=100)
    image = models.ImageField('イメージ', upload_to='profile')
    career = models.CharField('職業', max_length=55, null=True, blank=True)
    org = models.CharField('所属組織', max_length=55, null=True, blank=True)
    age = models.CharField('年齢', max_length=55, null=True, blank=True)
    twitter = models.URLField('TwitterのURL', null=True, blank=True)
    github = models.URLField('githubのURL', null=True, blank=True)
    instagram = models.URLField('InstagramのURL', null=True, blank=True)
    introduction = models.TextField('自己紹介文')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'プロフィール'


class Description(models.Model):

    text = models.CharField('本文', max_length=255)

    def __str__(self):
        return self.text
    
    class Meta:
        verbose_name_plural = 'スキルの概要文'

class Skill(models.Model):

    name = models.CharField('名前', max_length=100)
    years = models.FloatField('経験年数', default=0)
    description = models.ForeignKey(Description, on_delete=models.SET_NULL, null=True, verbose_name='説明文')

    def years_rounded(self):
        years = self.years
        if years.is_integer():
            years = int(years)
        return years

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'スキル'


class WorkDetail(models.Model):

    text = models.CharField('本文', max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = '作品の詳細文'


class Work(models.Model):

    title = models.CharField('タイトル', max_length=100)
    detail = models.ForeignKey(WorkDetail, on_delete=models.SET_NULL, null=True, verbose_name='詳細文')
    image = models.ImageField('イメージ', upload_to='works', null=True)
    url = models.URLField('URL')
    published = models.DateField('公開日', null=True, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = '作品'