from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .forms import UserForm
from ledina.exams.models import Exam
from ledina.core.views import index


def register(request):
	if request.method == "POST":
		form = UserForm(request.POST or None)
		if form.is_valid():
			username = request.POST['username']
			if len(username) > 14:
				context = {'form': form, 'error_message': 'Uporabniško ime je predolgo.'}
				return render(request, 'register.html', context)
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()
			user = authenticate(username = username, password = password)
			if user is not None:
				if user.is_active:
					login(request, user)
					return index(request, new_user=True)
		context = {"form": form, "error_message": "Poskusite registracijo z drugimi podatki."}
		return render(request, 'register.html', context)
	return render(request, 'register.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            else:
                return render(request, 'login.html', {'error_message': 'Vaš račun je bil onemogočen'})
        else:
            return render(request, 'login.html', {'error_message': 'Neveljavna prijava'})
    return render(request, 'login.html')

def logout_user(request):
	logout(request)
	form = UserForm(request.POST or None)
	context = {
	'form': form
	}
	return render(request, 'login.html', context)
