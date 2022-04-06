from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, db_index=True, verbose_name='заголовок')
    description = models.CharField(max_length=1000, default='', verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='время обновления')
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', related_name="advertisements", default=None,
                               null=True, on_delete=models.CASCADE)
    type = models.ForeignKey('AdvertisementType', related_name="advertisements", default=None,
                             null=True, on_delete=models.CASCADE)
    author = models.ForeignKey('Author', related_name="advertisements", default=None,
                               null=True, on_delete=models.CASCADE)
    '''rubric = models.ForeignKey('Rubric', related_name="advertisements", default=None,
                               null=True, on_delete=models.SET_DEFAULT)'''

    def __str__(self):
        return self.title


    class Meta:
        db_table= 'advertisements'
        ordering = ['title']


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Author(models.Model):
    name=models.CharField(max_length=100, primary_key=True)
    email=models.EmailField(max_length=50)
    phone_number=models.CharField(max_length=11)

    def __str__(self):
        return str(self.name or '')


'''class Rubric(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name'''
