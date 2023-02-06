from django.shortcuts import render
from .models import Department,User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import DepartmentForm, UserForm, LoginForm, AssignDepartmentForm 
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(**data)
            if user is not None:
                login(request, user)
                if user.role == 'USER':
                    return redirect('user')
                return redirect('admin')
    context = {'form': form}
    return render(request, 'acme_app/login.html', context)


@login_required()
def admin_homepage(request):
    return render(request, 'acme_app/admin_homepage.html')


@login_required()
def user_homepage(request):
    return render(request, 'acme_app/user_homepage.html')


@login_required()
def register_view(request):
    if request.user.role == 'ADMIN':
        form = UserForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                obj = form.save(commit=False)
                password = form.cleaned_data.get('password')
                obj.username = obj.name
                obj.created_by = request.user.name
                obj.set_password(password)
                obj.save()
                return redirect('show-users')
        context = {'form': form}
        return render(request, 'acme_app/register_user.html', context)
    return HttpResponse('<h1>You Do Not Have Permission to access this Resource</h1>')


@login_required()
def show_users(request):
    if request.user.role == 'ADMIN':
        users = User.objects.all()
        return render(request,'acme_app/show_users.html', {'users': users})
    return HttpResponse('<h1>You Do Not Have Permission to access this Resource</h1>')


@login_required()
def add_department(request):
    if request.user.role == 'ADMIN':
        form = DepartmentForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = request.user.name
            obj.save()
            return redirect('show-departments')
        context = {'form': form}
        return render(request, 'acme_app/add_department.html', context)
    return HttpResponse('<h1>You Do Not Have Permission to access this Resource</h1>')


@login_required()
def show_departments(request):
    if request.user.role == 'ADMIN':
        depts = Department.objects.all()
        return render(request, 'acme_app/show_departments.html', {'depts': depts})
    return HttpResponse('<h1>You Do Not Have Permission to access this Resource</h1>')


@login_required()
def assign_department(request, pk):
    if request.user.role == 'ADMIN':
        obj = get_object_or_404(User, pk=pk)
        form = AssignDepartmentForm(request.POST or None , instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show-users')
        context = {'form': form}
        return render(request, 'acme_app/assign_department.html', context)
    return HttpResponse('<h1>You Do Not Have Permission to access this Resource</h1>')

@login_required()
def delete_department(request,pk):
    if request.user.role=='ADMIN':
        obj = User.objects.get(id= pk)
        if request.method == 'POST':
            obj.delete()
           # return redirect('show-users')
        template_name = 'acme_app/confirm.html'
        context = {'users' : obj}
        return render(request, template_name, context)
    return HttpResponse('<h1>You Do Not Have Permission to access this Resource</h1>')

  

def logout_view(request):
    logout(request)
    return redirect('home')



