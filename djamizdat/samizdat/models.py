# -*- coding: utf-8 -*-

from django.db import models


class WikiTexts(models.Model):
    """ Текст для вики """

    nazv = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    red_zag = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    author = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    translator = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    editor = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    data_n = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    place_n = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    data_i = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    place_i = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    zhanr = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    picture = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    samizdat = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    categories = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    link = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    user = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    ruwiki = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    enwiki = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Название"
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата")
    oborotka = models.TextField(
        blank=True,
        verbose_name="Оборотка"
    )


class TXTC(models.Model):
    """ TXTC """

    t_type = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="Тип"
    )


class XTC(models.Model):
    """ XTC """

    number = models.CharField(
        max_length=10,
        blank=True,
        verbose_name="Номер ХТС"
    )
    pages = models.CharField(
        max_length=50,
        verbose_name="Номера страниц",
        helper_text="Номера страниц хроники, на которых упомянут документ"
    )
    pages_from = models.IntegerField(
        blank=True, null=True,
        verbose_name="Начальная страница диапазона")
    pages_to = models.IntegerField(
        blank=True, null=True,
        verbose_name="Последняя страница диапазона")
    profile = models.CharField(
        max_length=20,
        blank=True,
        verbose_name="Профиль упоминания",
        default="упом."
    )
    notes = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Примечания"
    )
    #XXX Possible foreign key to ???
    id_doc = models.IntegerField(verbose_name="Документ")
    operator = models.CharField(
        max_length=8,
        blank=True,
        verbose_name="Оператор"
    )
    date = models.DateField(auto_now_add=True, verbose_name="Дата ввода")


class Catalog(models.Model):
    """ Основной каталог ?? """

    ACNumber = models.CharField(
        max_length=28,
        blank=True,
        verbose_name="Номер АС"
    )
    language = models.CharField(
        max_lenght=2,
        blank=True,
        verbose_name="Язык"
    )
    translated = models.CharField(
        max_length=2,
        blank=True,
        verbose_name="Переведено"
    )
    author = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Автор"
    )
    auth_notes = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Примечания к автору"
    )
    auth_group = models.CharField(
        max_lenght=100,
        blank=True,
        verbose_name="Группа авторов"
    )
    auth_group_notes = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Примечания к группе авторов"
    )
    group_members = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Состав группы"
    )
    members_notes = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Примечания к составу группы"
    )
    signers = models.CharField(
        max_lenght=255,
        blank=True,
        verbose_name="Подписанты"
    )
    signers_notes = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Примечания о подписантах"
    )
    complie_editors = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Редакторы_составители"
    )
    ce_notes = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Примечания о редакторах-составителях"
    )
    selfname = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="Самоназвание"
    )
    name1 = models.CharField(
        max_length=255,
        blank=True,
        verbose_name="name1"
    )
    #XXX Possible foreign key to TypeDoc
    typedoc = models.CharField(
        max_length=25,
        blank=True,
        verbose_name="Тип документа"
    )
    name = models.TextField(blank=True, verbose_name="Название")



