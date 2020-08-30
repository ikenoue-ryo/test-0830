from django.shortcuts import render

def indexfunc(request):
    context = {
        'hello': 'こんにちは'
    }
    return render(request, 'myapp/index.html', context)