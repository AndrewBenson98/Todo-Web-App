from django.shortcuts import render, redirect

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

class TaskListView(LoginRequiredMixin,TemplateView):
    template_name = 'todofrontend/tasks-list.html'
    

# class UserCreateView(CreateView):
#     model = User
#     template_name = 'todofrontend/register.html'
#     fields = ['username','email', 'password']
#     form=UserCreationForm
#     success_url = reverse_lazy('login')



def register(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Please log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'todofrontend/register.html',{'form':form})