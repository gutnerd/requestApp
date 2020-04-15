#!/usr/bin/env python3
from tkinter import * #pip install
import tkinter
from xml.etree import ElementTree as ET

#Okno
root = Tk()
root.geometry("700x500")
root.title("Facade request generator")


#setup
global counter
counter = -1

global characteristics
characteristics = []

global characteristicsEntry
characteristicsEntry = []

global characteristicsNameEntry
characteristicsNameEntry = []
# topFrame = Frame(topFrame)
# topFrame.grid(row=0, column=0)
# topFrame = Frame(topFrame)
# topFrame.grid(row=0, column=1)
# topFrame.pack(fill=X, expand=TRUE)
topFrame = Frame(root)
topFrame.pack(side=LEFT, anchor=N, padx=25, pady=25)
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, padx=25, pady=25)
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT, anchor=N, padx=25, pady=25)


#Lables
FileName_Lable = Label(topFrame, text="Filename: ")
eTrackingId_Lable = Label(topFrame, text="eTrackingId: ")
iTrackingId_Lable = Label(topFrame, text="iTrackingId: ")
sourceApplication_Lable = Label(topFrame, text="sourceApplication: ")
sourceUser_Lable = Label(topFrame, text="sourceUser: ")
tenantId_Lable = Label(topFrame, text="tenantId: ")
timestamp_Lable = Label(topFrame, text="timestamp: ")
orderID_Lable = Label(topFrame, text="orderID: ")
orderRef_Lable = Label(topFrame, text="orderRef: ")
planID_Lable = Label(topFrame, text="planID: ")
planItemID_Lable = Label(topFrame, text="planItemID: ")
processComponentID_Lable = Label(topFrame, text="processComponentID: ")
processComponentName_Lable = Label(topFrame, text="processComponentName: ")
processComponentVersion_Lable = Label(topFrame, text="processComponentVersion: ")
originator_Lable = Label(topFrame, text="originator: ")
priority_Lable = Label(topFrame, text="priority: ")
actualProcessStep_Lable = Label(topFrame, text="actualProcessStep: ")
entity_Lable = Label(topFrame, text="entity: ")
operation_Lable = Label(topFrame, text="operation: ")
command_Lable = Label(topFrame, text="command: ")

FileName_Lable.grid(row=0, sticky=E)
eTrackingId_Lable.grid(row=1, sticky=E)
iTrackingId_Lable.grid(row=2, sticky=E)
sourceApplication_Lable.grid(row=3, sticky=E)
sourceUser_Lable.grid(row=4, sticky=E)
tenantId_Lable.grid(row=5, sticky=E)
timestamp_Lable.grid(row=6, sticky=E)
orderID_Lable.grid(row=7, sticky=E)
orderRef_Lable.grid(row=8, sticky=E)
planID_Lable.grid(row=9, sticky=E)
planItemID_Lable.grid(row=10, sticky=E)
processComponentID_Lable.grid(row=11, sticky=E)
processComponentName_Lable.grid(row=12, sticky=E)
processComponentVersion_Lable.grid(row=13, sticky=E)
originator_Lable.grid(row=14, sticky=E)
priority_Lable.grid(row=15, sticky=E)
actualProcessStep_Lable.grid(row=16, sticky=E)
entity_Lable.grid(row=17, sticky=E)
operation_Lable.grid(row=18, sticky=E)
command_Lable.grid(row=19, sticky=E)

#Entries
FileName_Entry = Entry(topFrame, text="FileName: ")
eTrackingId_Entry = Entry(topFrame, text="eTrackingId: ")
iTrackingId_Entry = Entry(topFrame, text="iTrackingId: ")
sourceApplication_Entry = Entry(topFrame, text="sourceApplication: ")
sourceUser_Entry = Entry(topFrame, text="sourceUser: ")
tenantId_Entry = Entry(topFrame, text="tenantId: ")
timestamp_Entry = Entry(topFrame, text="timestamp: ")
orderID_Entry = Entry(topFrame, text="orderID: ")
orderRef_Entry = Entry(topFrame, text="orderRef: ")
planID_Entry = Entry(topFrame, text="planID: ")
planItemID_Entry = Entry(topFrame, text="planItemID: ")
processComponentID_Entry = Entry(topFrame, text="processComponentID: ")
processComponentName_Entry = Entry(topFrame, text="processComponentName: ")
processComponentVersion_Entry = Entry(topFrame, text="processComponentVersion: ")
originator_Entry = Entry(topFrame, text="originator: ")
priority_Entry = Entry(topFrame, text="priority: ")
actualProcessStep_Entry = Entry(topFrame, text="actualProcessStep: ")
entity_Entry = Entry(topFrame, text="entity: ")
operation_Entry = Entry(topFrame, text="operation: ")
command_Entry = Entry(topFrame, text="command: ")

FileName_Entry.grid(row=0, column=1, sticky=W)
eTrackingId_Entry.grid(row=1, column=1, sticky=W)
iTrackingId_Entry.grid(row=2, column=1, sticky=W)
sourceApplication_Entry.grid(row=3, column=1, sticky=W)
sourceUser_Entry.grid(row=4, column=1, sticky=W)
tenantId_Entry.grid(row=5, column=1, sticky=W)
timestamp_Entry.grid(row=6, column=1, sticky=W)
orderID_Entry.grid(row=7, column=1, sticky=W)
orderRef_Entry.grid(row=8, column=1, sticky=W)
planID_Entry.grid(row=9, column=1, sticky=W)
planItemID_Entry.grid(row=10, column=1, sticky=W)
processComponentID_Entry.grid(row=11, column=1, sticky=W)
processComponentName_Entry.grid(row=12, column=1, sticky=W)
processComponentVersion_Entry.grid(row=13, column=1, sticky=W)
originator_Entry.grid(row=14, column=1, sticky=W)
priority_Entry.grid(row=15, column=1, sticky=W)
actualProcessStep_Entry.grid(row=16, column=1, sticky=W)
entity_Entry.grid(row=17, column=1, sticky=W)
operation_Entry.grid(row=18, column=1, sticky=W)
command_Entry.grid(row=19, column=1, sticky=W)

#Characteristics part
command_Lable = Label(topFrame, text="command: ")
characteristicsLabel = Label(topFrame, text="Characteristics")
characteristicsLabel.grid(row=20, column=0, pady=15, sticky=E)

#Request input
# requestInput = Entry(topFrame)
# requestInput.grid(row=0, column=1)
# requestInput.pack(side = LEFT)  #ipadx=150, ipady=200
# requestInput.pack(side=LEFT, fill=X, expand=TRUE)

def printsumstuff(event):
    global characteristicsValueEntry
    global characteristicsNameEntry
    length: int = len(characteristicsNameEntry)
    print(length)

    FileName = FileName_Entry.get()
    eTrackingId = eTrackingId_Entry.get()
    iTrackingId = iTrackingId_Entry.get()
    sourceApplication = sourceApplication_Entry.get()
    sourceUser = sourceUser_Entry.get()
    tenantId = tenantId_Entry.get()
    timestamp = timestamp_Entry.get()
    orderID = orderID_Entry.get()
    orderRef = orderRef_Entry.get()
    planID = planID_Entry.get()
    planItemID = planItemID_Entry.get()
    processComponentID = processComponentID_Entry.get()
    processComponentName = processComponentName_Entry.get()
    processComponentVersion = processComponentVersion_Entry.get()
    originator = originator_Entry.get()
    priority = priority_Entry.get()
    actualProcessStep = actualProcessStep_Entry.get()
    entity = entity_Entry.get()
    operation = operation_Entry.get()
    command = command_Entry.get()

    #replace funny vars by real vars
    with open("templates/facade_template.xml", 'r') as file:
        facade_temp = file.read()
        facade_temp = facade_temp.replace('${eTrackingId}', eTrackingId)
        facade_temp = facade_temp.replace('${iTrackingId}', iTrackingId)
        facade_temp = facade_temp.replace('${sourceApplication}', sourceApplication)
        facade_temp = facade_temp.replace('${sourceUser}', sourceUser)
        facade_temp = facade_temp.replace('${tenantId}', tenantId)
        facade_temp = facade_temp.replace('${timestamp}', timestamp)
        facade_temp = facade_temp.replace('${orderID}', orderID)
        facade_temp = facade_temp.replace('${orderRef}', orderRef)
        facade_temp = facade_temp.replace('${planID}', planID)
        facade_temp = facade_temp.replace('${planItemID}', planItemID)
        facade_temp = facade_temp.replace('${processComponentID}', processComponentID)
        facade_temp = facade_temp.replace('${processComponentName}', processComponentName)
        facade_temp = facade_temp.replace('${processComponentVersion}', processComponentVersion)
        facade_temp = facade_temp.replace('${originator}', originator)
        facade_temp = facade_temp.replace('${priority}', priority)
        facade_temp = facade_temp.replace('${actualProcessStep}', actualProcessStep)
        facade_temp = facade_temp.replace('${entity}', entity)
        facade_temp = facade_temp.replace('${operation}', operation)
        facade_temp = facade_temp.replace('${command}', command)
    # print(facade_temp)

    #create file request
    f = open(FileName + ".xml", 'w')
    f.write(facade_temp)
    f.close()

    #create parametrized file request
    f = open(FileName + "Parametrized.xml", 'w')

    #create jmeter template
    with open("templates/facade_template.xml", 'r') as file:
        facade_temp = file.read()
        f.write(facade_temp)
        file.close()
    with open("templates/characteristics_templates.xml", 'r') as file:
        characteristics_temp = file.read()
        var = []
        for i in range(len(characteristicsNameEntry)):
            print(i)
            var.append(topFrame.nametowidget("characteristicNameEntry" + str(i)).get())
            print(var)
            haha = var[i]
            print(haha)
            characteristic_temp = characteristics_temp.replace('${ATRIBUTE}', '${' + haha + '}')
            characteristi_temp = characteristic_temp.replace('ATNAME', '"' + haha + '"')
            print(characteristi_temp)
            f.write(characteristi_temp)
        file.close()

    with open("templates/end_facade_template.xml", 'r') as file:
        end_temp = file.read()
        f.write(end_temp)
    f.close()

    #.csv file
    with open("templates/csv_template.csv", 'r') as file:
        csv_temp = file.read()
        f = open(FileName + ".csv", 'w')
        f.write(csv_temp)
        for i in range(len(characteristicsNameEntry)):
            var.append(topFrame.nametowidget("characteristicNameEntry" + str(i)).get())
            print(var)
            haha = var[i]
            print(haha)
            f.write(',' + str(haha))
        f.write("\n")

    f.write(str(eTrackingId) + ',' + str(iTrackingId) + ',' + str(sourceApplication) + ',' + str(sourceUser) + ',' + str(tenantId) + ',' + str(timestamp) + ',' + str(orderID) + ',' + str(orderRef) + ',' + str(planID) + ',' + str(planItemID) + ',' + str(processComponentID) + ',' + str(processComponentName) + ',' + str(processComponentVersion) + ',' + str(originator) + ',' + str(priority) + ',' + str(actualProcessStep) + ',' + str(entity) + ',' + str(operation) + ',' + str(command))
    var2 = []
    for i in range(len(characteristicsEntry)):
        var2.append(topFrame.nametowidget("characteristicEntry" + str(i)).get())
        print(var2)
        haha2 = var2[i]
        print(haha2)
        f.write(',' + str(haha2))
    f.close()


    #output
    f = open(FileName + "Parametrized.xml", 'r')
    file = f.read()
    myLable3 = Text(rightFrame)
    myLable3.insert(END, file)
    myLable3.pack()
    f.close()




def addChar(event):
    global counter
    global characteristicsValueEntry
    global characteristicsNameEntry
    counter += 1
    print(counter)
    characteristics.append("characteristic" + str(counter))
    characteristics[-1] = Label(topFrame, text=characteristics[-1])
    characteristics[-1].grid(row=21+counter, column=0, sticky=E)
    # characteristicsEntry.append("characteristicEntry" + str(counter))
    # characteristicsEntry[-1] = Entry(topFrame)
    # characteristicsEntry[-1].grid(row=21+counter, column=2, sticky=E)

    characteristicsNameEntry.append(Entry(topFrame, name="characteristicNameEntry" + str(counter)))
    characteristicsNameEntry[-1].grid(row=21+counter, column=1, sticky=E)

    characteristicsEntry.append(Entry(topFrame, name="characteristicEntry" + str(counter)))
    characteristicsEntry[-1].grid(row=21+counter, column=2, sticky=E)

    print(characteristicsEntry)
    print(characteristicsNameEntry)





##############
#####Buttons
##############
#main button
requestButton = Button(bottomFrame, text="Generate request")
requestButton.pack(side=BOTTOM, pady=10)
requestButton.bind("<Button-1>", printsumstuff)

#secondary button
addCharacteristicButton = Button(topFrame, text="Add a characteristic")
addCharacteristicButton.grid(row=20, column=1, pady=15, sticky=W)
addCharacteristicButton.bind("<Button-1>", addChar)

#
# #Lable
# myLable = Label(topFrame, text="Request App")
# myLable.pack(side=RIGHT)
#
# #Lable
# myLable2 = Label(topFrame, text="Request App", bg="blue", fg="white")
# myLable2.pack(fill=Y, expand=TRUE)



topFrame.mainloop()
