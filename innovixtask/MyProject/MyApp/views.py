from django.shortcuts import render, redirect
from django.views import View
from .forms import CustomUserForm, CustomUpdateForm
from django.views.generic import ListView
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

# Create your views here.

'''
view created for signup/registration of user
def get is method defined to view form when user hits url
def post is a method defined to post/submit form with details filled such as username, profile_pic etc
'''

class CreateCustomUser(View):
    template_name='MyApp/user.html'

    def get(self, request):
        form=CustomUserForm
        context={'form':form}
        return render(request, self.template_name, context)

    def post(self, request):
        form=CustomUserForm(request.POST, request.FILES)
        # print(request.POST.get('password'))
        if form.is_valid:
            form.save()
            return redirect('login')

        context={'form': form}
        return render(request, self.template_name, context)

'''
view created for displaying list of users that are saved in database
update and delete user options have also been added to the HTML page
''' 

class ListCustomUser(ListView):
    model=CustomUser
    template_name='MyApp/list.html'

'''
view defined for login using username, password
from django.contrib.auth login, logout, autheticate has been used
further, logout functionality has also been added
'''
def user_login_view(request):
    template_name='MyApp/login.html'
    context={}
    if request.method=='POST':
        un=request.POST.get('un')
        pass1=request.POST.get('pass')
        user=authenticate(username=un, password=pass1)
        if user is not None:
            login(request, user)
        return redirect('display')
    return render(request, template_name, context)

def user_logout_view(request):
    logout(request)
    return redirect('login')

'''
update view created for updating the details
pk will allow us to acces id of user
'''

def update(request, pk):
    current_user = request.user
    if current_user.id == pk:
        user = CustomUser.objects.get(pk=pk)
        form = CustomUpdateForm(instance=user)
        template_name = 'MyApp/update.html'
        context = {'form':form, 'user':user}

        if request.method == 'POST':
                form = CustomUpdateForm(request.POST,request.FILES, instance=user)
                context = {'form': form}
                if form.is_valid():
                    form.save()
                    return redirect('update', pk=user.id)
            
        return render(request, template_name, context)

    else:
        return HttpResponse('You do not have permission to edit this profile')

'''
delete view created for deleting user
the user which is logged in will only get an option to delete that user
'''
def delete(request, pk):
    if request.user.id == pk:
        user = CustomUser.objects.get(pk=pk)
        template_name = 'MyApp/confirm.html'
        context = {}
        if request.method == 'POST':
            user.delete()
            return redirect('display')
        return render(request, template_name, context)
    
    return HttpResponse('You do nor have permission to edit this profile')

'''
additional functionality to remove profile picture
once profile picture is removed, default image will be shown
'''

def remove_profile_pic(request,pk):
    user = CustomUser.objects.get(pk=pk)
    old_image = user.profile_pic
    old_image.delete()
    user.profile_pic = 'default.jpg'
    user.save()
    return redirect('update', pk=user.id)