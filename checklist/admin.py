from django.contrib import admin
from django import forms
from .models import *
from .forms import *
import nested_admin
from django_admin_json_editor import JSONEditorWidget
# from django_jsonforms.forms import JSONSchemaField


class StepInline(admin.StackedInline):
    model = Step


class SectionInline(admin.StackedInline):
    model = Section
    inlines = [StepInline]


class SectionAdmin(admin.ModelAdmin):
    model = Section
    inlines = [SectionInline, StepInline]

admin.site.register(Section, SectionAdmin)


class ChecklistAdmin(admin.ModelAdmin):
    # inlines = [SectionInline]
    model = Checklist
    form = ChecklistForm

admin.site.register(Checklist, ChecklistAdmin)
