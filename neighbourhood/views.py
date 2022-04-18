
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from neighbourhood.models import Post
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.views.generic import ListView, DetailView, CreateView
# Create your views here.


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'neighbourhood/index.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'neighbourhood/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        



def register(request):
    form = UserRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'neighbourhood/register.html', {'form': form})

@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'neighbourhood/profile.html', context)

def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'neighbourhood/search.html',{"message":message,"articles": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'neighbourhood/search.html',{"message":message})
 