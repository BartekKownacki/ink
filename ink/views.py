from django.shortcuts import render
import os
# Create your views here.
def InkView(request):
    text = "asdfasdfasdfasdfasdfasdfasdfasdf"

    context = {
        'text':text,
    }
    return render(request, 'ink.html', context)