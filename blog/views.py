from django.shortcuts import render
from django.contrib.auth.decorators import login_required
post = [
    {
      'author': 'pooja yadav',
       'title': 'search',
        'date_posted': 'Sept 24,2018'
    },

    {
      'author': 'Arun yadav',
       'title': 'field',
        'date_posted': 'Sept 25,2018'
    }
]

@login_required
def home(request):
    return render(request, 'blog/home.html', context={'posts': post, 'title': 'home'})

@login_required
def about(request):
     return render(request, 'blog/about.html', context={})
