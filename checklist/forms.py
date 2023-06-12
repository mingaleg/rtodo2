from django.shortcuts import render
from django import forms
from .models import *
from django_admin_json_editor import JSONEditorWidget

# Create your views here.
DATA_SCHEMA = {
    'definitions': {
        'section': {
            'type': 'object',
            'properties': {
                'title': {
                    'type': 'string',
                },
                'sections': {
                    'type': 'array',
                    'items': { "$ref": "#/definitions/section" },
                    'default': [],
                },
                'steps': {
                    'type': 'array',
                    'items': { "$ref": "#/definitions/step" },
                    'default': [],
                },
            },
        },
        'step': {
            'type': 'object',
            'properties': {
                'title': {
                    'type': 'string',
                },
                'content': {
                    'type': 'string',
                    'format': 'textarea',
                },
            },
        },
    },
    'title': 'section',
    'properties': {
        'section': { "$ref": "#/definitions/section"},
    },
    'type': 'object',
    'default': {'section': {
        'title': 'TODO',
    }},
}

class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = '__all__'
        widgets = {
            'contents': JSONEditorWidget(DATA_SCHEMA, collapsed=False),
        }
