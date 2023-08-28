from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

from .models import Drawing
from .forms import DrawingForm, RatingForm

import random

# This is the home page with everything
def home(request):
  records = Record.objects.all()

  
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user= authenticate(request, username = username, password = password)
    if user is not None:
        login(request,user)
        messages.success(request, "Successfully logged in!")
        return redirect('home')
    else:
      messages.success(request, "There was an error logging in.")
      return redirect('home')
  else:
    return render(request, 'home.html', {'records':records})

## This function takes all the drawings that users have submitted and picks a random one.
## It also allows users to submit ratings for the random object that was chosen. 
## It would keep assigning the rating to a random object until I put the drawing ID thing
def imagerate(request):
    random_drawing = Drawing.objects.order_by('?').first()
    if request.method == 'POST':
      rating_form = RatingForm(request.POST)
      if rating_form.is_valid():
        drawing_id = request.POST.get('drawing_id')
        rating = rating_form.cleaned_data['rating']
        random_drawing = Drawing.objects.get(id=drawing_id)
        random_drawing.rating = rating
        random_drawing.save()
        return redirect('imagerate')
    else: 
       rating_form = RatingForm()
    return render(request, 'imagerate.html', {'random_drawing': random_drawing,'rating_form': rating_form})


#Logging out user
def logout_user(request):
  logout(request)
  messages.success(request, "Successfully logged out")
  return redirect('home')

#Registering the user
def register_user(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      form.save()
      username=form.cleaned_data['username']
      password=form.cleaned_data['password1']
      user=authenticate(username=username, password= password)
      login(request, user)
      messages.success(request,"You have successfully registered")
      return redirect('home')
    
  else:
    form = SignUpForm()
    return render(request, 'register.html', {'form':form})
  
  return render(request, 'register.html', {'form':form})

#When someone submits their drawing
def draw_and_submit(request):
    if request.method == 'POST':
        form = DrawingForm(request.POST)
        if form.is_valid():
            drawing_data = form.cleaned_data['image_data']
            drawing_name = form.cleaned_data['drawing_name'] 
            Drawing.objects.create(image_data=drawing_data, drawing_name=drawing_name)
            return redirect('draw_and_submit')  # Redirect after submission
    else:
        form = DrawingForm()
    return render(request, 'draw_and_submit.html', {'form': form})


