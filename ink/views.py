from django.shortcuts import render
import os
# Create your views here.
def InkView(request):
    if = os.popen('sudo escputil -i -u -r /dev/usb/lp0')
    text = f.read()
    words = text.split()

    table = ""
    for i in range(len(words)):

        if words[i] == "Black":
            for j in range(i,len(words)):
                
                table = table + " " + words[j] 
            break
    
    table = table.split()   
    context = {
        'Black':table[0],
        'BValue':table[1],
        'Cyan':table[2],
        'CValue':table[3],
        'Magenta':table[4],
        'MValue':table[5],
        'Yellow':table[6],
        'YValue':table[7]
    }
    return render(request, 'ink.html', context)
