from django import forms

from .models import Exam, ExamFile

class ExamForm(forms.ModelForm):
	class Meta:
		model = Exam
		fields = ['exam_number']
		widgets = {
		'exam_number': forms.NumberInput(
			attrs={'id': 'exam_number', 'required': True,})
		}

class FileForm(forms.ModelForm):
	class Meta:
		model = ExamFile
		fields = ['exam_file']
		widgets = {
		'exam_file': forms.ClearableFileInput(
			attrs={'multiple': True, 'required': True,})
		}