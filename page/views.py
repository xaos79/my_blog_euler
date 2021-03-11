from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Article
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUp

def home(request):
	obj_art=Article.objects.all()
	return render(request, 'home.html', {'obj_art':obj_art})

def work(request, pk):
	zadacha_obj=Article.objects.get(id=pk)
	lasted_comment=zadacha_obj.comment_set.all()
	context={
		'zadacha_obj':zadacha_obj,
		'lasted_comment':lasted_comment,
	}
	return render(request, 'work.html', context)

def leave_comment(request, pk):
	zadacha=Article.objects.get(id=pk)
	zadacha.comment_set.create(text=request.POST['text'], person=request.user.username)
	zadacha.save()
	return redirect(reverse('work', args=[zadacha.id]))

def Sign_View(request):
	if request.method=='POST':
		form=SignUp(request.POST)
		if form.is_valid:
			form.save()
	else:
		form=SignUp()
	return render(request, 'sign.html', {'form':form})

def Sign_Out(request):
	logout(request)
	return redirect('home')

def Login_View(request):
	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)
		if form.is_valid:
			username=request.POST['username']
			password=request.POST['password']
			user=authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				return redirect('sign')
	else:
		form=AuthenticationForm()
	return render(request, 'login.html', {'form':form})

