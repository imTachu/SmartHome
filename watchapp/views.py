from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages 
from django.contrib.auth.models import User, Group
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
 
from forms import SignUpForm

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
	
@login_required()
def home(request):
    return render_to_response('watchapp/home.html', {'user': request.user}, context_instance=RequestContext(request))

def main(request):
    return render_to_response('watchapp/main.html', {}, context_instance=RequestContext(request))

def signup(request):
    if request.method == 'POST':  # If the form has been submitted...
        form = SignUpForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
 
            # Process the data in form.cleaned_data
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
 
            # At this point, user is a User object that has already been saved
            # to the database. You can continue to change its attributes
            # if you want to change other fields.
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
 
            # Save new user attributes
            user.save()
            return HttpResponseRedirect(reverse('watchapp:login'))  # Redirect after POST
    else:
        form = SignUpForm()
 
    data = {
        'form': form,
    }
    return render_to_response('watchapp/signup.html', data, context_instance=RequestContext(request))

def login_success(request):
    if request.user.groups.filter(name="constructoras").exists():
        # user is an admin
        return HttpResponseRedirect(reverse('watchapp:constructora_home'))
    elif request.user.groups.filter(name="usuarios").exists():
        return HttpResponseRedirect(reverse('watchapp:usuarios_home'))

@login_required()
@user_passes_test(lambda u: u.groups.filter(name='constructoras').exists(), login_url='/watchapp/login/')
def constructora_home(request):
	return HttpResponse("Usuario constructora autenticado")

@login_required()
@user_passes_test(lambda u: u.groups.filter(name='usuarios').exists(), login_url='/watchapp/login/')
def usuarios_home(request):
	return HttpResponse("Usuario residente / propietario autenticado")
