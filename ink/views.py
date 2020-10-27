from django.shortcuts import render
import os
# Create your views here.
def InkView(request):
    f = os.popen('sudo escputil -i -u -r /dev/usb/lp0')
    text = f.read()

    context = {
        'text':text,
    }
    return render(request, 'ink.html', context)
