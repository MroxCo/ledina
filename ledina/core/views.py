from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.http import JsonResponse
import json

from django.contrib.auth.models import User
from ledina.exams.models import Exam, ExamComment


def index(request, **new_user):
	users = User.objects.all().order_by('username')
	odd_users = users[::2]
	even_users = users[1::2]
	latest_exams = Exam.objects.all().order_by('-exam_date')[:4]
	return render(request, 'index.html', {'users': users, 
		                                  'odd_users': odd_users, 
		                                  'even_users': even_users,
		                                  'latest_exams': latest_exams,
		                                  'new_user': new_user})

	
def profile(request, username):
	page_user = get_object_or_404(User, username=username)
	exams = Exam.objects.filter(exam_user=page_user).order_by('exam_number')
	comments = ExamComment.objects.filter(comment_user=page_user).order_by('comment_date')
	return render(request, "profile.html",{'exams': exams, 'comments': comments, 'page_user': page_user})


def noscript(request):
	return render(request, 'noscript.html')