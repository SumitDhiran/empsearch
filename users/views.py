from django.http.response import HttpResponse
from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout

from django.contrib import messages

from .models import Candidate
from .forms import CandidateForm,CustomUserCreationForm
from django.contrib.auth.models import User
# Create your views here.



def loginUser(request):
    if request.user.is_authenticated:
        return redirect('candidates')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.get(username=username)
    
        if user:
            user = authenticate(username=username,password=password)
        else:
            messages.info(request," Username or Password is incorrect ")

        if user is not None:
            login(request,user)
            messages.info(request,"logged in succesfully")
            return redirect('candidates')


    return render(request,'users/login.html')



@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request,"User logged out successfully")
    return redirect('login')

    #return render(request,'users/login.html')


def registerUser(request):
    if request.user.is_authenticated:
        return redirect('login')
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            messages.success(request,"User account created successfully")
            return redirect('login')

    context = {'form':form}
    return render(request,'users/register.html',context)




def candidates(request):
    if request.user.is_authenticated:
        #user       = request.user
        candidates = request.user.candidate_set.all()
    else:
        candidates = Candidate.objects.all()
    
    context={'candidates':candidates}
    return render(request,'users/candidates.html',context)


@login_required(login_url='login')
def addCandidate(request):
    user = request.user
    form = CandidateForm()
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()
            messages.success(request,"New Candidate added succesfully")
            return redirect('candidates') 

    context = {'form':form}
    return render(request,'users/candidate_form.html',context)
    

@login_required(login_url='login')
def updateCandidate(request,pk):
    candidate = Candidate.objects.get(id=pk)
    form = CandidateForm(instance=candidate)

    if request.method == 'POST':
        form = CandidateForm(request.POST,instance=candidate)
        if form.is_valid():
            form.save()
            messages.info(request,"Candidate information updated succesfully")
            return redirect('candidates')

    context = {'form':form}
    return render(request,'users/candidate_form.html',context)


@login_required(login_url='login')
def deleteCandidate(request,pk):
    candidate = Candidate.objects.get(id=pk)

    if request.method == 'POST':
        candidate.delete()
        messages.info(request,"Candidate deleted succesfully")
        return redirect('candidates')

    context = {'candidate':candidate}
    return render(request,'users/delete-candidate.html',context)