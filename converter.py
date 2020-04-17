#!/usr/bin/env python3
from random import randint
from tkinter import * #pip install
from tkinter import ttk
from xml.etree import ElementTree as ET

#Okno
root = Tk()
root.geometry("900x700")
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
topFrame = ttk.Frame(root)
canvas = Canvas(topFrame)
scrollbar = ttk.Scrollbar(topFrame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)


topFrame.pack(side=LEFT, anchor=N, padx=25, pady=25)
canvas.pack(side=LEFT, fill="both", expand=TRUE, ipady=500, ipadx=250)
scrollbar.pack(side=RIGHT, fill=Y)


bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, padx=25, pady=25)
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT, anchor=N, padx=25, pady=25)

# scrollbar = ttk.Scrollbar(topFrame, command=topFrame.yview)
# scrollbar.grid(sticky=E, fill=Y)
# topFrame.configure(yscrollcommand=scrollbar.set)


#Lables
FileName_Lable = Label(scrollable_frame, text="Filename: ")
eTrackingId_Lable = Label(scrollable_frame, text="eTrackingId: ")
iTrackingId_Lable = Label(scrollable_frame, text="iTrackingId: ")
sourceApplication_Lable = Label(scrollable_frame, text="sourceApplication: ")
sourceUser_Lable = Label(scrollable_frame, text="sourceUser: ")
tenantId_Lable = Label(scrollable_frame, text="tenantId: ")
timestamp_Lable = Label(scrollable_frame, text="timestamp: ")
orderID_Lable = Label(scrollable_frame, text="orderID: ")
orderRef_Lable = Label(scrollable_frame, text="orderRef: ")
planID_Lable = Label(scrollable_frame, text="planID: ")
planItemID_Lable = Label(scrollable_frame, text="planItemID: ")
processComponentID_Lable = Label(scrollable_frame, text="processComponentID: ")
processComponentName_Lable = Label(scrollable_frame, text="processComponentName: ")
processComponentVersion_Lable = Label(scrollable_frame, text="processComponentVersion: ")
originator_Lable = Label(scrollable_frame, text="originator: ")
priority_Lable = Label(scrollable_frame, text="priority: ")
actualProcessStep_Lable = Label(scrollable_frame, text="actualProcessStep: ")
entity_Lable = Label(scrollable_frame, text="entity: ")
operation_Lable = Label(scrollable_frame, text="operation: ")
command_Lable = Label(scrollable_frame, text="command: ")

FileName_Lable.grid(row=1, sticky=E)
eTrackingId_Lable.grid(row=2, sticky=E)
iTrackingId_Lable.grid(row=3, sticky=E)
sourceApplication_Lable.grid(row=4, sticky=E)
sourceUser_Lable.grid(row=5, sticky=E)
tenantId_Lable.grid(row=6, sticky=E)
timestamp_Lable.grid(row=7, sticky=E)
orderID_Lable.grid(row=8, sticky=E)
orderRef_Lable.grid(row=9, sticky=E)
planID_Lable.grid(row=10, sticky=E)
planItemID_Lable.grid(row=11, sticky=E)
processComponentID_Lable.grid(row=12, sticky=E)
processComponentName_Lable.grid(row=13, sticky=E)
processComponentVersion_Lable.grid(row=14, sticky=E)
originator_Lable.grid(row=15, sticky=E)
priority_Lable.grid(row=16, sticky=E)
actualProcessStep_Lable.grid(row=17, sticky=E)
entity_Lable.grid(row=18, sticky=E)
operation_Lable.grid(row=19, sticky=E)
command_Lable.grid(row=20, sticky=E)

#Entries
FileName_Entry = Entry(scrollable_frame, text="FileName: ")
eTrackingId_Entry = Entry(scrollable_frame, text="eTrackingId: ")
iTrackingId_Entry = Entry(scrollable_frame, text="iTrackingId: ")
sourceApplication_Entry = Entry(scrollable_frame, text="sourceApplication: ")
sourceUser_Entry = Entry(scrollable_frame, text="sourceUser: ")
tenantId_Entry = Entry(scrollable_frame, text="tenantId: ")
timestamp_Entry = Entry(scrollable_frame, text="timestamp: ")
orderID_Entry = Entry(scrollable_frame, text="orderID: ")
orderRef_Entry = Entry(scrollable_frame, text="orderRef: ")
planID_Entry = Entry(scrollable_frame, text="planID: ")
planItemID_Entry = Entry(scrollable_frame, text="planItemID: ")
processComponentID_Entry = Entry(scrollable_frame, text="processComponentID: ")
processComponentName_Entry = Entry(scrollable_frame, text="processComponentName: ")
processComponentVersion_Entry = Entry(scrollable_frame, text="processComponentVersion: ")
originator_Entry = Entry(scrollable_frame, text="originator: ")
priority_Entry = Entry(scrollable_frame, text="priority: ")
actualProcessStep_Entry = Entry(scrollable_frame, text="actualProcessStep: ")
entity_Entry = Entry(scrollable_frame, text="entity: ")
operation_Entry = Entry(scrollable_frame, text="operation: ")
command_Entry = Entry(scrollable_frame, text="command: ")

FileName_Entry.grid(row=1, column=1, sticky=W)
eTrackingId_Entry.grid(row=2, column=1, sticky=W)
iTrackingId_Entry.grid(row=3, column=1, sticky=W)
sourceApplication_Entry.grid(row=4, column=1, sticky=W)
sourceUser_Entry.grid(row=5, column=1, sticky=W)
tenantId_Entry.grid(row=6, column=1, sticky=W)
timestamp_Entry.grid(row=7, column=1, sticky=W)
orderID_Entry.grid(row=8, column=1, sticky=W)
orderRef_Entry.grid(row=9, column=1, sticky=W)
planID_Entry.grid(row=10, column=1, sticky=W)
planItemID_Entry.grid(row=11, column=1, sticky=W)
processComponentID_Entry.grid(row=12, column=1, sticky=W)
processComponentName_Entry.grid(row=13, column=1, sticky=W)
processComponentVersion_Entry.grid(row=14, column=1, sticky=W)
originator_Entry.grid(row=15, column=1, sticky=W)
priority_Entry.grid(row=16, column=1, sticky=W)
actualProcessStep_Entry.grid(row=17, column=1, sticky=W)
entity_Entry.grid(row=18, column=1, sticky=W)
operation_Entry.grid(row=19, column=1, sticky=W)
command_Entry.grid(row=20, column=1, sticky=W)

myLable3 = Text(rightFrame)
myLable3.pack(ipadx=250, ipady=250)

#Characteristics part
# command_Lable = Label(topFrame, text="command: ")
characteristicsLabel = Label(scrollable_frame, text="Characteristics")
characteristicsLabel.grid(row=21, column=0, pady=15, sticky=E)

#Request input
# requestInput = Entry(topFrame)
# requestInput.grid(row=0, column=1)
# requestInput.pack(side = LEFT)  #ipadx=150, ipady=200
# requestInput.pack(side=LEFT, fill=X, expand=TRUE)

def printsumstuff(event):
    global chvar1
    global chvar2

    print(chvar1.get())
    print(chvar2.get())
    # var2 = IntVar()
    # print(var2.state())

    global characteristicsValueEntry
    global characteristicsNameEntry

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

    #list with variables to write to file
    var_list = [eTrackingId, iTrackingId, sourceApplication, sourceUser, tenantId, timestamp, orderID, orderRef, planID, planItemID, processComponentID, processComponentName, processComponentVersion, originator, priority, actualProcessStep, entity, operation, command]
    str_list = ['${eTrackingId}', '${iTrackingId}', '${sourceApplication}', '${sourceUser}', '${tenantId}', '${timestamp}', '${orderID}', '${orderRef}', '${planID}', '${planItemID}', '${processComponentID}', '${processComponentName}', '${processComponentVersion}', '${originator}', '${priority}', '${actualProcessStep}', '${entity}', '${operation}', '${command}']
    print(var_list)
    print(str_list)

#AZ BUDE CAS DODELAM GENEROVANI XML SOUBORU
    # ind = 0
    #
    # #replace funky vars by real vars
    # with open('templates\\facade_template.xml') as oldfile, open(FileName + '.xml', 'w') as newfile:
    #     for line in oldfile:
    #         if any(s in line for s in str_list):
    #             if str(var_list[ind]) != "":
    #                 newfile.write(line)
    #                 ind += 1
    #             else:
    #                 newfile.write("")
    #                 ind += 1
    #         else:
    #             newfile.write(line)
    if FileName != "":
        if chvar2.get() == 1:
            #create parametrized file request
            ind = 0
            #zapsani requestu

            with open('templates\\facade_template.xml') as oldfile, open("out\\xml\\" + FileName + 'Parametrized.xml', 'w') as newfile:
                for line in oldfile:
                    if any(s in line for s in str_list):
                        if str(var_list[ind]) != "":
                            newfile.write(line)
                            ind += 1
                        else:
                            newfile.write("")
                            ind += 1
                    else:
                        newfile.write(line)
                #zapsani charakteristik
                with open("templates\\characteristics_templates.xml", 'r') as file:
                    characteristics_temp = file.read()
                    # print(characteristics_temp)
                    var = []
                    for i in range(len(characteristicsNameEntry)):
                        # print(i)
                        var.append(scrollable_frame.nametowidget("characteristicNameEntry" + str(i)).get())
                        # print(var)
                        haha = var[i]
                        # print(haha)
                        characteristic_temp = characteristics_temp.replace('${ATRIBUTE}', '${' + haha + '}')
                        characteristi_temp = characteristic_temp.replace('ATNAME', '"' + haha + '"')
                        # print(characteristi_temp)
                        newfile.write(characteristi_temp)

                #zapsani koncovky xml
                with open("templates\\end_facade_template.xml", 'r') as file:
                    end_temp = file.read()
                    newfile.write(end_temp)
        else:
            print("badluck1")
        if chvar1.get() == 1:
            #.csv file
            with open("templates\\csv_template.csv", 'r') as file:
                csv_temp = file.read()
                f = open("out\\csv\\" + FileName + ".csv", 'w')
                f.write(csv_temp)
                for i in range(len(characteristicsNameEntry)):
                    var.append(scrollable_frame.nametowidget("characteristicNameEntry" + str(i)).get())
                    # print(var)
                    haha = var[i]
                    # print(haha)
                    f.write(',' + str(haha))
                f.write("\n")

            f.write(str(eTrackingId) + ',' + str(iTrackingId) + ',' + str(sourceApplication) + ',' + str(sourceUser) + ',' + str(tenantId) + ',' + str(timestamp) + ',' + str(orderID) + ',' + str(orderRef) + ',' + str(planID) + ',' + str(planItemID) + ',' + str(processComponentID) + ',' + str(processComponentName) + ',' + str(processComponentVersion) + ',' + str(originator) + ',' + str(priority) + ',' + str(actualProcessStep) + ',' + str(entity) + ',' + str(operation) + ',' + str(command))
            var2 = []
            for i in range(len(characteristicsEntry)):
                var2.append(scrollable_frame.nametowidget("characteristicEntry" + str(i)).get())
                # print(var2)
                haha2 = var2[i]
                # print(haha2)
                f.write(',' + str(haha2))
            f.close()
        else:
            print("badluck2")
        if chvar2.get() == 1:
            #output
            f = open("out\\xml\\" + FileName + "Parametrized.xml", 'r')
            file = f.read()
            output = myLable3.get("1.0",'end-1c')
            if output != "":
                myLable3.delete('1.0', END)
            myLable3.insert(END, file)
            f.close()

        #delete filename
        FileName_Entry.delete(0, 'end')
        FileName_Entry['bg'] = 'WHITE'
    else:
        FileName_Entry['bg'] = 'RED'

###########################################################
def addChar(event):
    global counter
    global characteristicsValueEntry
    global characteristicsNameEntry
    counter += 1
    # print(counter)
    characteristics.append("characteristic" + str(counter))
    characteristics[-1] = Label(scrollable_frame, text=characteristics[-1])
    characteristics[-1].grid(row=22+counter, column=0, sticky=E)

    characteristicsNameEntry.append(Entry(scrollable_frame, name="characteristicNameEntry" + str(counter)))
    characteristicsNameEntry[-1].grid(row=22+counter, column=1, sticky=E)

    characteristicsEntry.append(Entry(scrollable_frame, name="characteristicEntry" + str(counter)))
    characteristicsEntry[-1].grid(row=22+counter, column=2, sticky=E)

    # print(characteristicsEntry)
    # print(characteristicsNameEntry)




#delete a characteristic
def deleteChar():
    global counter
    #get last added characteristic elements
    labelToDestroy = characteristics[-1]
    characteristicsEntryToDestroy = characteristicsEntry[-1]
    characteristicsNameEntryToDestroy = characteristicsNameEntry[-1]

    #destroy a characteristic
    labelToDestroy.destroy()
    characteristicsEntryToDestroy.destroy()
    characteristicsNameEntryToDestroy.destroy()

    #unset elements from element list
    characteristics.remove(characteristics[-1])
    characteristicsEntry.remove(characteristicsEntry[-1])
    characteristicsNameEntry.remove(characteristicsNameEntry[-1])
    counter -= 1

#preset values
def presetValues():
    eTrack = randint(1000000000, 1001223218)
    planIdRan = randint(100, 999)
    planItemIdRan = randint(10, 99)
    compID = randint(100, 999)
    if eTrackingId_Entry.get() != "":
        FileName_Entry.delete(0, 'end')
        eTrackingId_Entry.delete(0, 'end')
        iTrackingId_Entry.delete(0, 'end')
        sourceApplication_Entry.delete(0, 'end')
        sourceUser_Entry.delete(0, 'end')
        tenantId_Entry.delete(0, 'end')
        timestamp_Entry.delete(0, 'end')
        orderID_Entry.delete(0, 'end')
        orderRef_Entry.delete(0, 'end')
        planID_Entry.delete(0, 'end')
        planItemID_Entry.delete(0, 'end')
        processComponentID_Entry.delete(0, 'end')
        # processComponentName_Entry.delete(0, 'end')
        processComponentVersion_Entry.delete(0, 'end')
        originator_Entry.delete(0, 'end')
        priority_Entry.delete(0, 'end')
        # actualProcessStep_Entry.insert(END, '')
        # entity_Entry.insert(END, '')
        # operation_Entry.insert(END, '')
        # command_Entry.insert(END, '')
    #set some default filename
    filename = "Zmen mi jmeno"
    FileName_Entry.insert(END, filename)
    eTrackingId_Entry.insert(END, 'O-' + str(eTrack))
    iTrackingId_Entry.insert(END, "TMCZ-" + str(planIdRan) + "-" + str(planItemIdRan))
    sourceApplication_Entry.insert(END, 'tmcz.telekom.it.architecture.COM:COM')
    sourceUser_Entry.insert(END, 'TEMP_sourceUser')
    tenantId_Entry.insert(END, 'TMCZ')
    timestamp_Entry.insert(END, '2020-03-014T10:38:00Z')
    orderID_Entry.insert(END, 'TEMP_interni_FOM_ID')
    orderRef_Entry.insert(END, str(eTrack))
    planID_Entry.insert(END, str(planIdRan))
    planItemID_Entry.insert(END, str(planItemIdRan))
    processComponentID_Entry.insert(END, str(compID))
    # processComponentName_Entry.insert(END, '')
    processComponentVersion_Entry.insert(END, '1')
    originator_Entry.insert(END, 'TMCZ')
    priority_Entry.insert(END, '4')
    # actualProcessStep_Entry.insert(END, '')
    # entity_Entry.insert(END, '')
    # operation_Entry.insert(END, '')
    # command_Entry.insert(END, '')

##############
#####Buttons
##############
#main button
requestButton = Button(bottomFrame, text="Generate request")
requestButton.pack(side=BOTTOM, pady=10)
requestButton.bind("<Button-1>", printsumstuff)

#secondary button
addCharacteristicButton = Button(scrollable_frame, text="Add a characteristic")
addCharacteristicButton.grid(row=21, column=1, pady=15, sticky=W)
addCharacteristicButton.bind("<Button-1>", addChar)

#tertiary button
setValuesButton = Button(scrollable_frame, text="Delete a characteristic", command=deleteChar)
setValuesButton.grid(row=21, column=2, pady=15, sticky=W)

#quaternary button
setValuesButton = Button(scrollable_frame, text="Preset values", command=presetValues)
setValuesButton.grid(row=0, column=1, pady=15, sticky=W)

topFrame.mainloop()
