# -*- coding: utf-8 -*-

from django.db import models


class Languages(models.Model):
    """ Язык документа """

    language = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Язык"
    )


class Docname(models.Model):
    """ Наименование документа """

    docname = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Наименование документа"
    )


class TypeDoc(models.Model):
    """ Тип документа """

    doctype = models.CharField(
        max_length=25,
        primary_key=True,
        verbose_name="Тип документа"
    )


class Reference(models.Model):
    """ Ссылки """

    ACnumber = models.CharField(
        max_length=28,
        blank=True,
        verbose_name="НомерАС"
    )
    notes = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Примечания"
    )
    page = models.CharField(
        max_length=15,
        blank=True,
        verbose_name="Страница"
    )
    #XXX FK to Names structure
    name = models.IntegerField(verbose_name="Имя")


class Category(models.Model):
    """ Категории документа """

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


class TextCategory(models.Model):
    """ Промежуточная таблица для связи документов с категориями """

    text_code = models.IntegerField()
    category_code = models.IntegerField()
    timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)
