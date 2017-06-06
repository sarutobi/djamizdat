# -*- coding: utf-8 -*-

from django.db import models

from samizdat.models import Catalog


class Name(models.Model):
    """ Именник """

    class Meta:
        verbose_name = "Имя"
        verbose_name_plural = "Имена"
        ordering = ['name', ]

    name = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Имя"
    )
    info = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Информация"
    )

    def __unicode__(self):
        return self.name


class Author(models.Model):
    """ Описание автора """

    class Meta:
        ordering = ["names_code", "catalog"]
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    catalog = models.ForeignKey(
        Catalog, null=True,
        verbose_name="Код каталога", related_name='catalog_FK')
    #XXX Possible foreign key to Names
    names_code = models.IntegerField(verbose_name="Код именник")
    #names_code = models.ForeignKey(
        # Name,
        # verbose_name=u"Код именник",
        # db_column="names_code", null=True)
    status = models.CharField(
        max_length=30,
        blank=True, default='',
        verbose_name="Статус"
    )
    note = models.TextField(
        verbose_name="Примечание",
        blank=True
    )
    #XXX Possible foreign key to Operator
    operator = models.CharField(
        max_length=30,
        verbose_name="Оператор"
    )
    date = models.DateField(
        auto_now_add=True,
        verbose_name="Дата занесения",
        null=True
    )

    def __unicode__(self):
        return "%s" % self.pk


class Receiver(models.Model):
    """ Адресат """

    class Meta:
        verbose_name = "Адресат"
        verbose_name_plural = "Адресаты"

    person = models.CharField(
        max_length=50,
        blank=True, default='',
        verbose_name="Адресат-персона")
    title = models.CharField(
        max_length=50,
        blank=True, default='',
        verbose_name="Адресат-титул")
    group = models.CharField(
        max_length=120,
        blank=True, default='',
        verbose_name="Адресат-группа")
    #XXX Possible foreign key to docs?
    id_doc = models.IntegerField(verbose_name="id_doc")

    def __unicode__(self):
        return self.person
