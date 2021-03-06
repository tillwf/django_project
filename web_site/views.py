from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text

from .forms import SignUpForm

from django.views.generic.list import ListView
from web_site.models import Project

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def landpage(request):
    return render(request, 'web_site/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()

            current_site = get_current_site(request)
            
            return render(request, 'home.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


class ProjectListView(LoginRequiredMixin,ListView):

    model = Project
    paginate_by = 10  # if pagination is desired
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
