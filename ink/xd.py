f = "Escputil version 5.3.1, Copyright (C) 2000-2006 Robert Krawitz Escputil comes with ABSOLUTELY NO WARRANTY; for details type 'escputil -l' This is free software, and you are welcome to redistribute it under certain conditions; type 'escputil -l' for details. Ink color Percent remaining Photo Black 63 Cyan 39 Magenta 99 Yellow 99"
text = f
words = text.split()

ful = ""
for i in range(len(words)):

        if words[i] == "Black":
            for j in range(i,len(words)):
                
                ful = ful + " " + words[j] 
            break

print(ful.split())
