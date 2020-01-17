from django import forms
from .models import Notes

class NotesCreateForm(forms.ModelForm):

	class Meta:
		model = Notes
		fields = ('title', 'body')

		widgets={
			'body': forms.Textarea(attrs={'cols': 1,'rows': 7}),
		}

class NotesUpdateForm(forms.ModelForm):
	
	class Meta:
		model = Notes
		fields = ('title', 'body')
		
		widgets={
			'body': forms.Textarea(attrs={'cols': 1,'rows': 7}),
		}