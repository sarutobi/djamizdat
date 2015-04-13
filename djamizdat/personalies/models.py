# -*- coding: utf-8 -*-

from django.db import models

from samizdat.models import Catalog

class Name(models.Model):
    """ Именник """

    name = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Имя"
    )
    info = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Информация"
    )


class Author(models.Model):
    """ Описание автора """

    catalog = models.ForeignKey(verbose_name="Код каталога")
    #XXX Possible foreign key to Names
    names_code = models.IntegerField(verbose_name="Код именник")
    status = models.CharField(
        max_length=30,
        blank=True,
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
        verbose_name="Дата занесения"
    )


class Receiver(models.Model):
    """ Адресат """

    person = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Адресат-персона")
    title = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Адресат-титул")
    group = models.CharField(
        max_length=120,
        blank=True,
        verbose_name="Адресат-группа")
    #XXX Possible foreign key to docs?
    id_doc = models.IntegerField(verbose_name="id_doc")
