from django.forms import ModelForm, modelform_factory
from .models import NoteGroup, Note


class NoteForm(ModelForm):
    class Meta:
        model = Note
        # fields = '__all__'
        fields = ['title', 'content', 'note_group', 'is_fast']


class NoteGroupForm(ModelForm):
    class Meta:
        model = NoteGroup
        fields = ['name']
