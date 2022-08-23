
from django.shortcuts import render
from .models import List

def index(request):
    context = {'success': False}
    if request.method == "POST":
        #Handling the form
        titles = request.POST.get('tsktitle')
        descriptions = request.POST['descriptions']
        print(titles, descriptions)
        ins = List(title=titles, description=descriptions)
        ins.save()
        context = {'success': True,
                    'tsktitle': titles
                  }
        
    return render(request, 'index.html', context)


def tasks(request):
    Task = List.objects.all()
    context = {'tasks': Task}
    return render(request, 'tasks.html', context)