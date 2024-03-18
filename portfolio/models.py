from django.db import models

# Create your models here.


class Profile(models.Model):
    
    name = models.CharField('名前', max_length=100)
    image = models.ImageField('イメージ', upload_to='profile')
    career = models.CharField('職業',max_length=55, null=True, blank=True)
    org = models.CharField('所属組織',max_length=55, null=True, blank=True)
    age = models.CharField('年齢',max_length=55, null=True, blank=True)
    twitter = models.URLField('X(旧Twitter)のURL', null=True, blank=True)
    facebook = models.URLField('FacebookのURL', null=True, blank=True)
    instagram = models.URLField('InstagramのURL', null=True, blank=True)
    line = models.URLField('LINEのURL', null=True, blank=True) 
    introduction = models.TextField('自己紹介文')
    
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
    year = models.FloatField('経験年数', default=0)
    description = models.ForeignKey(Description, on_delete=models.SET_NULL, null=True, verbose_name='説明文')
    
    def years_rounded(self):
        years = self.year
        if years.is_integer():
            years = int(years)
        return years

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'スキル'


class Work(models.Model):
    
    title = models.CharField('タイトル', max_length=100)
    image = models.ImageField('イメージ', upload_to='works', null=True, blank=True)
    url = models.URLField('URL')
    published = models.DateField('公開日', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = '作品'