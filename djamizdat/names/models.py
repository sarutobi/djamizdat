# -*- coding: utf-8 -*-

from django.db import models


class Geografy(models.Model):
    """ Таблица "География" из именника """
    class Meta:
        verbose_name = "География"
        verbose_name_plural = "География"

    name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="География")


class Suit(models.Model):
    """ Таблица "Масть" из именника """
    class Meta:
        verbose_name = "Масть"
        verbose_name_plural = "Масти"

    name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Масть")


class Name(models.Model):
    """ Таблица "Grind2" из именника """
    class Meta:
        verbose_name = "Имя"
        verbose_name_plural = "Имена"

    fio = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="ФИО")
    src_note = models.TextField(
        blank=True, null=True, verbose_name="Справка из других источников")
    editor_note = models.TextField(
        blank=True, null=True, verbose_name="Справка редактора")
    chr_note = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="Ссылка на хронику")
    ours = model.BooleanField(verbose_name="Сделано нами")
    verified = models.BooleanField(verbose_name="Просмотрена Хр")
    geo = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="География")
