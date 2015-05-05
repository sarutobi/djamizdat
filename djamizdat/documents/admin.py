# -*- coding: utf-8 -*-

from django.contrib import admin


from .models import Languages, Docname, TypeDoc, Reference, Category


admin.site.register(Languages)
admin.site.register(Docname)
admin.site.register(TypeDoc)
admin.site.register(Reference)
admin.site.register(Category)
