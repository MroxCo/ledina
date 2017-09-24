from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms

class Exam(models.Model):
	exam_number = models.PositiveIntegerField(validators=[MaxValueValidator(6),MinValueValidator(1)])
	exam_path = models.CharField(max_length=255)
	exam_date = models.DateTimeField(auto_now_add=True)
	exam_user = models.ForeignKey(User, null=True)
	exam_mark = models.ManyToManyField(User, blank=True, related_name='post_likes')

	def get_comments(self):
		return ExamComment.objects.filter(exam=self)

	def get_files(self):
		return ExamFile.objects.filter(exam=self)

	def __str__(self):
		return str(self.exam_number) + ' - ' + str(self.exam_path) 

class ExamFile(models.Model):
	exam_file = models.ImageField()
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

	def __str__(self):
		return str(self.exam)

class ExamComment(models.Model):
	exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
	comment = models.CharField(max_length=255)
	comment_date = models.DateTimeField(auto_now_add=True)
	comment_user = models.ForeignKey(User)

	def __str__(self):
		return str(self.comment)