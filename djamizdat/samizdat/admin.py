# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import WikiTexts, XTC, Catalog


class AdminWikiTexts(admin.ModelAdmin):
    pass


class AdminXTC(admin.ModelAdmin):
    pass


class AdminCatalog(admin.ModelAdmin):
    pass

admin.site.register(WikiTexts, AdminWikiTexts)
admin.site.register(XTC, AdminXTC)
admin.site.register(Catalog, AdminCatalog)
