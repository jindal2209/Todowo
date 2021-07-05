from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .models  import UserTodo
from .forms import UserTodoForm
from django.utils import timezone
from django.contrib import messages


# Create your views here.
def home(request):
	try: 
		todo = UserTodo.objects.filter(user=request.user)
		length_todo = todo.count()
		return render(request,'user_auth/home.html',{'todos':todo , 'num' : length_todo })
	except:
		return render(request,'user_auth/home.html')

def createuser(request):
	if request.user.is_authenticated :
		messages.warning(request, 'Logout to create new account') 
		return redirect('home')
	if request.method == 'GET':
		return render(request,'user_auth/createuser.html',{'form' : UserCreationForm()})
	else:
		if request.POST['password1'] == request.POST['password2']:
			try:    
				user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])  #User returns object which is saved in variable user 
				user.save()      # now save that user to insert in database
				messages.success(request, 'Account created successfully! Please login to continue') 
				return redirect('home')
			except IntegrityError:
				error = 'User already exist choose another username'
				return render(request,'user_auth/createuser.html',{'form' : UserCreationForm(),'error' : error})    
		else:
			error = 'ERROR:passwords do not match!!!'
			return render(request,'user_auth/createuser.html',{'form' : UserCreationForm(),'error' : error})
	   
def loginuser(request):
	if request.method == 'GET':
		if request.user.is_authenticated :
			return redirect('home')
		return render(request,'user_auth/loginuser.html',{'form':AuthenticationForm()})
	else:
		user = authenticate(request,username = request.POST['username'],password=request.POST['password'])
		if user :
			login(request,user)
			messages.success(request, 'Logged in successfully!')
			return redirect('home')
		else:
			message = 'username or password don\'t match!!!\ntry again!!'
			return render(request,'user_auth/loginuser.html',{'form':AuthenticationForm(),'error' : message})

@login_required            
def signout(request):
	logout(request)
	messages.success(request, 'Signed out successfully!') 
	return redirect('home')

@login_required
def createusertodo(request):
	if request.method == 'GET':
		return render(request,'user_auth/createtodo.html',{'form' : UserTodoForm()})
	else:
		form = UserTodoForm(request.POST)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.user = request.user
			todo.last_edited = timezone.now()
			todo.save()
			messages.success(request, 'Todo Created!') 
			return redirect('home')
		else:
			return render(request, 'user_auth/createtodo.html', {'form':UserTodoForm(), 'error':'Bad data passed in. Try again.'})

@login_required
def showtodos(request,todo_pk):
	todo = get_object_or_404(UserTodo,user=request.user,pk=todo_pk)
	if request.method == 'GET' :
		form = UserTodoForm(instance=todo)
		return render(request,'user_auth/showtodo.html',{'todo' : todo,'form':form})
	else:
		form = UserTodoForm(request.POST,instance=todo)
		if form.is_valid():
			todo = form.save(commit=False)
			todo.user = request.user
			todo.last_edited = timezone.now()
			todo.save()
			messages.success(request, 'Todo Edited!') 
			return redirect('home')
		else:
			return render(request, 'user_auth/createtodo.html', {'form':todo , 'error':'Bad data passed in. Try again.'})

@login_required
def delete_todo(request,pk):
	post = get_object_or_404(UserTodo, pk=pk)
	post.delete()
	messages.success(request, 'Todo Deleted!!') 
	return redirect('home')

# @login_required
# def edit_todo(request,pk):
#     todo = get_object_or_404(UserTodo,pk=pk)
#     if request.method == 'GET':
#         form = UserTodoForm(instance=todo)
#         return render(request,'user_auth/showtodo.html',{'todo' : todo,'form':form})
#     else:
#         form = UserTodoForm(request.POST)
#         if form.is_valid():
#             todo = form.save(commit=False)
#             todo.user = request.user
#             todo.last_edited = timezone.now()
#             todo.save()
#             messages.success(request, 'Todo Edited!') 
#             return redirect('home')
#         else:
#             return render(request, 'user_auth/createtodo.html', {'form':todo , 'error':'Bad data passed in. Try again.'})