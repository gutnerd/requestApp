#!/usr/bin/env python3
from tkinter import * #pip install
from xml.etree import ElementTree as ET

#Okno
root = Tk()
root.geometry("700x500")

#setup
row1 = Frame(root)
row1.grid(row=0, column=0)
# row1.pack(fill=X, expand=TRUE)

#Lable
myLable = Label(row1, text="Raw request: ")
myLable.grid(row=0, sticky=N)


#Request input
requestInput = Text(root)
requestInput.grid(row=0, column=1)
# requestInput.pack(side = LEFT)  #ipadx=150, ipady=200
# requestInput.pack(side=LEFT, fill=X, expand=TRUE)


def printsumstuff(event):
    entryVar = requestInput.get("1.0", "end-1c")
    f = open('sandbox.xml', 'w')
    f.write(entryVar)
    f.close()
    tree = ET.parse('sandbox.xml')
    xmlRoot = tree.getroot()
    i = 0
    for child in xmlRoot:
        print(child.tag, child.attrib)
        for i in child:
            print(i.text)






    myLable3 = Text(root)
    myLable3.insert(END, entryVar)
    myLable3.grid(row=4, column=1)



#Button
button = Button(root, text="Generate request")
# command=printsumstuff
button.grid(row=2, column=1)
button.bind("<Button-1>", printsumstuff)




#
# #Lable
# myLable = Label(topFrame, text="Request App")
# myLable.pack(side=RIGHT)
#
# #Lable
# myLable2 = Label(root, text="Request App", bg="blue", fg="white")
# myLable2.pack(fill=Y, expand=TRUE)



root.mainloop()
