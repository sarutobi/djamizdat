# -*- coding: utf-8 -*-

from django.db import models


class WikiTexts(models.Model):
    """ Текст для вики """

    nazv = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    red_zag = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    author = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    translator = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    editor = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    data_n = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    place_n = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    data_i = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    place_i = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    zhanr = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    picture = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    samizdat = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    categories = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    title = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    link = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    user = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    ruwiki = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    enwiki = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    timestamp = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата")
    oborotka = models.TextField(
        blank=True, default='',
        verbose_name="Оборотка"
    )


class TXTC(models.Model):
    """ TXTC """

    t_type = models.CharField(
        max_length=50,
        blank=True, default='',
        verbose_name="Тип"
    )


class XTC(models.Model):
    """ XTC """

    number = models.CharField(
        max_length=10,
        blank=True, default='',
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
        blank=True, default='',
        verbose_name="Профиль упоминания",
        default="упом."
    )
    notes = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Примечания"
    )
    catalog = models.ForeignKey("Catalog", verbose_name="Документ")
    operator = models.CharField(
        max_length=8,
        blank=True, default='',
        verbose_name="Оператор"
    )
    date = models.DateField(auto_now_add=True, verbose_name="Дата ввода")


class Catalog(models.Model):
    """ Основной каталог ?? """

    ACNumber = models.CharField(
        max_length=28,
        blank=True, default='',
        verbose_name="Номер АС"
    )
    language = models.CharField(
        max_length=2,
        blank=True, default='',
        verbose_name="Язык"
    )
    translated = models.CharField(
        max_length=2,
        blank=True, default='',
        verbose_name="Переведено"
    )
    author = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Автор"
    )
    auth_notes = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Примечания к автору"
    )
    auth_group = models.CharField(
        max_length=100,
        blank=True, default='',
        verbose_name="Группа авторов"
    )
    auth_group_notes = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Примечания к группе авторов"
    )
    group_members = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Состав группы"
    )
    members_notes = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Примечания к составу группы"
    )
    signers = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Подписанты"
    )
    signers_notes = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Примечания о подписантах"
    )
    complie_editors = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Редакторы_составители"
    )
    ce_notes = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Примечания о редакторах-составителях"
    )
    selfname = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Самоназвание"
    )
    name1 = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="name1"
    )
    #XXX Possible foreign key to TypeDoc
    typedoc = models.CharField(
        max_length=25,
        blank=True, default='',
        verbose_name="Тип документа"
    )
    name = models.TextField(blank=True, verbose_name="Название")
    name2 = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Name2"
    )
    place = models.CharField(
        max_length=100,
        blank=True, default='',
        verbose_name="Место"
    )
    m_ind = models.CharField(
        max_length=100,
        blank=True, default='',
        verbose_name="m-ind"
    )
    place_prim = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="PlacePrim"
    )
    date = models.CharField(
        max_length=125,
        blank=True, default='',
        verbose_name="Дата"
    )
    date_prim = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="DatePrim"
    )
    date1 = models.DateTimeField(blank=True, null=True, verbose_name="date1")
    date2 = models.DateTimeField(blank=True, null=True, verbose_name="date2")
    reproducing = models.CharField(
        max_length=15,
        blank=True, default='',
        verbose_name="Способ воспроизведения"
    )
    authencity = models.CharField(
        max_length=10,
        blank=True, default='',
        verbose_name="Подлинность"
    )
    num_copies = models.CharField(
        max_length=10,
        blank=True, null=True,
        verbose_name="Число экземпляров"
    )
    correction = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name="Правка"
    )
    medium = models.CharField(
        max_length=35,
        blank=True, null=True,
        verbose_name="Носитель"
    )
    pages = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name="Страниц"
    )
    archive_notes = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name="Архивные примечания"
    )
    notes = models.TextField(
        blank=True, null=True,
        verbose_name="Примечания"
    )
    published = models.TextField(
        blank=True, null=True,
        verbose_name="Опубликовано"
    )
    tome = models.CharField(
        max_length=15,
        blank=True, null=True,
        verbose_name="Том"
    )
    number_mc = models.CharField(
        max_length=10,
        blank=True, null=True,
        verbose_name="Номер МС"
    )
    year = models.CharField(
        max_length=20,
        blank=True, null=True,
        verbose_name="Год"
    )
    fund = models.CharField(
        max_length=70,
        blank=True, null=True,
        verbose_name="Фонд"
    )
    register = models.CharField(
        max_length=70,
        blank=True, null=True,
        verbose_name="Опись"
    )
    folder = models.CharField(
        max_length=10,
        blank=True, null=True,
        verbose_name="Дело"
    )
    sheets = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name="Листы"
    )
    annotation = models.TextField(
        blank=True, null=True,
        verbose_name="Аннотация"
    )
    web_address = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name="Адрес документа"
    )
    nas = models.IntegerField(
        blank=True, null=True,
        verbose_name="NAS"
    )
    nas_ind = models.CharField(
        max_length=28,
        blank=True, null=True,
        verbose_name="NAS-ind"
    )
    troubles = models.NullBooleanField(verbose_name="Troubles")
    hr = models.NullBooleanField(
        verbose_name="Число экземпляров",
        helper_text="Отметка о том, что документ упоминается в Хронике"
    )
    hr_search = models.NullBooleanField(
        verbose_name="hr_poisk",
        helper_text="Отметка для фильтра по номеру ХТС"
    )
    operator = models.CharField(
        max_length=10,
        blank=True, null=True,
        verbose_name="Оператор",
        helper_text="Имя оператора, вводящего запись"
    )
    registration_date = models.DateTimeField(
        blank=True, null=True,
        verbose_name="Дата ввода",
        helper_text="Дата ввода оператором(проставляется автоматически)",
        auto_now_add=True
    )
    ready = models.NullBooleanField(
        verbose_name="Ready",
        helper_text="Отметка для записей, обработанных на авторство по Именнику"
    )
    belles_lettres = models.NullBooleanField(
        verbose_name="Художка",
    )
    link = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name="Ссылка",
    )
    aka_name = models.CharField(
        max_length=255,
        blank=True, null=True,
        verbose_name="AKA_name",
    )
