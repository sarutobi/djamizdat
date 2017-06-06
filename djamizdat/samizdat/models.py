# -*- coding: utf-8 -*-

from django.db import models

# from documents.models import Languages


class WikiTexts(models.Model):
    """ Текст для вики """
    class Meta:
        verbose_name = "Wiki заметка"
        verbose_name_plural = "Wiki заметки"

    nazv = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    red_zag = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="редакционный заголовок"
    )
    author = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Автор"
    )
    translator = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Переводчик"
    )
    editor = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Редактор"
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
        verbose_name="Жанр"
    )
    picture = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Изображение"
    )
    samizdat = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    categories = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Категории"
    )
    title = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Название"
    )
    link = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Ссылка"
    )
    user = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Пользователь"
    )
    ruwiki = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="RU wiki"
    )
    enwiki = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="EN wiki"
    )
    timestamp = models.DateTimeField(
        auto_now_add=True, null=True,
        verbose_name="Дата")
    oborotka = models.TextField(
        blank=True, default='',
        verbose_name="Оборотка"
    )

    def __unicode__(self):
        return self.nazv


class TXTC(models.Model):
    """ TXTC """

    t_type = models.CharField(
        max_length=50,
        blank=True, default='',
        verbose_name="Тип"
    )


class XTC(models.Model):
    """ XTC """
    class Meta:
        verbose_name = "Карточка"
        verbose_name_plural = "Карточки"

    number = models.CharField(
        max_length=10,
        blank=True, default='',
        verbose_name="Номер ХТС"
    )
    pages = models.CharField(
        max_length=50,
        verbose_name="Номера страниц",
        help_text="Номера страниц хроники, на которых упомянут документ"
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
        blank=True, default='',
        verbose_name="Примечания"
    )
    catalog = models.ForeignKey("Catalog", verbose_name="Документ")
    operator = models.CharField(
        max_length=8,
        blank=True, default='',
        verbose_name="Оператор"
    )
    date = models.DateField(
        auto_now_add=True, null=True, verbose_name="Дата ввода")

    def __unicode__(self):
        return self.number


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
    # language = models.ForeignKey(
        # "documents.Languages",
        # db_column="language",
        # null=True)
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
    # auth_group_notes = models.CharField(
        # max_length=255,
        # blank=True, default='',
        # verbose_name="Примечания к группе авторов"
    # )
    group_members = models.CharField(
        max_length=255,
        blank=True, default='',
        verbose_name="Состав группы"
    )
    # members_notes = models.CharField(
        # max_length=255,
        # blank=True, default='',
        # verbose_name="Примечания к составу группы"
    # )
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
        blank=True, null=True, default='',
        verbose_name="Место"
    )
    m_ind = models.CharField(
        max_length=100,
        blank=True, default='',
        verbose_name="m-ind"
    )
    place_prim = models.CharField(
        max_length=255,
        blank=True, null=True, default='',
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
        verbose_name="В хронике",
        help_text="Отметка о том, что документ упоминается в Хронике"
    )
    hr_search = models.NullBooleanField(
        verbose_name="hr_poisk",
        help_text="Отметка для фильтра по номеру ХТС"
    )
    operator = models.CharField(
        max_length=10,
        blank=True, null=True,
        verbose_name="Оператор",
        help_text="Имя оператора, вводящего запись"
    )
    registration_date = models.DateTimeField(
        blank=True, null=True,
        verbose_name="Дата ввода",
        help_text="Дата ввода оператором(проставляется автоматически)",
        auto_now_add=True
    )
    ready = models.NullBooleanField(
        verbose_name="Ready",
        help_text="Отметка для записей, обработанных на авторство по Именнику"
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

    def __unicode__(self):
        return self.name[0:60]
