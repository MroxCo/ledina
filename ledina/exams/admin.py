from django.contrib import admin

from .models import Exam, ExamFile, ExamComment


class ExamAdmin(admin.ModelAdmin):
	list_display = ['exam_path', 'exam_number', 'exam_user']
	ordering = ['exam_path']

class ExamCommentAdmin(admin.ModelAdmin):
	list_display = ['comment', 'exam', 'comment_user']
	ordering = ['exam']

class ExamFileAdmin(admin.ModelAdmin):
	list_display = ['exam']
	ordering = ['exam']

admin.site.register(Exam, ExamAdmin)
admin.site.register(ExamComment, ExamCommentAdmin)
admin.site.register(ExamFile, ExamFileAdmin)