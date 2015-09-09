# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Name, Author, Receiver


class AdminAuthor(admin.ModelAdmin):
    list_display = ("id", "catalog", "status")


admin.site.register(Name)
admin.site.register(Author, AdminAuthor)
admin.site.register(Receiver)
