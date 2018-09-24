from django.shortcuts import render

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


def home(request):
    return render(request, 'blog/home.html', context={'posts': post, 'title': 'home'})
def about(request):
     return render(request, 'blog/about.html', context={})
