# -*- coding: utf-8 -*-

from django.db import models

from personalies.models import Name
from samizdat.models import Catalog


class Languages(models.Model):
    """ Язык документа """

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"

    language = models.CharField(
        max_length=50,
        blank=True, default='',
        verbose_name="Язык"
    )

    def __unicode__(self):
        return self.language


class Docname(models.Model):
    """ Наименование документа """
    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    docname = models.CharField(
        max_length=50,
        blank=True, default='',
        verbose_name="Наименование документа"
    )

    def __unicode__(self):
        return self.docname


class TypeDoc(models.Model):
    """ Тип документа """
    class Meta:
        verbose_name = "Тип документа"
        verbose_name_plural = "Типы документов"

    doctype = models.CharField(
        max_length=25,
        primary_key=True,
        verbose_name="Тип документа"
    )

    def __unicode__(self):
        return self.doctype


class Reference(models.Model):
    """ Ссылки """
    class Meta:
        verbose_name = "Ссылка"
        verbose_name_plural = "Ссылки"

    ACnumber = models.CharField(
        max_length=28,
        blank=True, default='',
        verbose_name="НомерАС"
    )
    notes = models.CharField(
        max_length=100,
        blank=True, default='',
        verbose_name="Примечания"
    )
    page = models.CharField(
        max_length=15,
        blank=True, default='',
        verbose_name="Страница"
    )
    name = models.ForeignKey(Name, verbose_name="Имя")


class Category(models.Model):
    """ Категории документа """
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    parent_code = models.ForeignKey(
        "Category",
        verbose_name="Родительская категория",
        blank=True, null=True
    )
    level = models.SmallIntegerField(
        verbose_name="Уровень",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Категория"
    )
    path = models.CharField(
        max_length=255,
        verbose_name="Полный путь категории"
    )

    def __unicode__(self):
        return self.name


class TextCategory(models.Model):
    """ Промежуточная таблица для связи документов с категориями """

    catalog = models.ForeignKey(Catalog)
    category = models.ForeignKey(Category)
    timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)
