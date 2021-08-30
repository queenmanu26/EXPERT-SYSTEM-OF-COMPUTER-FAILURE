from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from expert.expert_system.interface import recuperer_liste_metiers
from .forms import SignUpForm



# Create your views here.
def home(request):
	return render(request, 'expert/home.html')

def login_view(request):
	if request.method == "POST":
		username = request.POST['login']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, 'expert/home.html')
			else:
				return render(
					request, 
					'expert/login.html', 
					{'error_msg' : 'Utilisateur inactif'}
				)
		else:
			return render(
				request, 
				'expert/login.html', 
				{'error_msg' : 'Nom d\'utilisateur ou mot de passe incorrect'}
			)
	else:
		return render(request, 'expert/login.html')

@login_required
def professions(request):
	return render(request, 'expert/professions.html')

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('expert:login'))

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('expert:home')
	else:
		form = SignUpForm()
		for field in form:
			print(field)
	return render(request, 'expert/signup.html', {'form': form})
	

@login_required
def evaluation(request):
	return render(request, 'expert/evaluation.html')

@login_required
def results(request):
	liste_metiers = recuperer_liste_metiers(request.GET.copy())
	return render(request, 'expert/results.html', {'liste_metiers' : liste_metiers})



