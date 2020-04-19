#!/usr/bin/env python3
from random import randint
from tkinter import *  # pip install
from tkinter import ttk
from tkinter import filedialog
from xml.etree import ElementTree as ET
from pathlib import Path
import csv

# Okno
root = Tk()
root.geometry("900x700")
root.title("Facade request generator")

# setup
global counter
counter = 0

global characteristics
characteristics = []

global characteristicsEntry
characteristicsEntry = []

global characteristicsNameEntry
characteristicsNameEntry = []

global chvar1
global chvar2
chvar1 = IntVar()
chvar2 = IntVar()
# topFrame = Frame(topFrame)
# topFrame.grid(row=0, column=0)
# topFrame = Frame(topFrame)
# topFrame.grid(row=0, column=1)
# topFrame.pack(fill=X, expand=TRUE)
topFrame = ttk.Frame(root)
canvas = Canvas(topFrame)
scrollbar = ttk.Scrollbar(topFrame, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

topButtonFrame = ttk.Frame(canvas)
topButtonFrame.grid()

midButtonFrame = ttk.Frame(canvas)
midButtonFrame.grid()

lowCharacteristicsFrame = ttk.Frame(canvas)
lowCharacteristicsFrame.grid()

lowCharacteristicsFrame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 70), window=scrollable_frame, anchor="nw")
canvas.create_window((187, 0), window=topButtonFrame, anchor="nw")
canvas.create_window((77, 545), window=midButtonFrame, anchor="nw")
canvas.create_window((77, 600), window=lowCharacteristicsFrame, anchor="nw")
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


# Lables


dataElements = dict(fileName={'entry': Entry(scrollable_frame), 'label': Label(scrollable_frame, text="Filename: ")},
                    eTrackingId={'entry': Entry(scrollable_frame),
                                 'label': Label(scrollable_frame, text="eTrackingId: ")},
                    iTrackingId={'entry': Entry(scrollable_frame),
                                 'label': Label(scrollable_frame, text="iTrackingId: ")},
                    sourceApplication={'entry': Entry(scrollable_frame),
                                       'label': Label(scrollable_frame, text="sourceApplication: ")},
                    sourceUser={'entry': Entry(scrollable_frame),
                                'label': Label(scrollable_frame, text="sourceUser: ")},
                    tenantId={'entry': Entry(scrollable_frame), 'label': Label(scrollable_frame, text="tenantId: ")},
                    timestamp={'entry': Entry(scrollable_frame), 'label': Label(scrollable_frame, text="timestamp: ")},
                    orderID={'entry': Entry(scrollable_frame), 'label': Label(scrollable_frame, text="orderID: ")},
                    orderRef={'entry': Entry(scrollable_frame), 'label': Label(scrollable_frame, text="orderRef: ")},
                    planID={'entry': Entry(scrollable_frame), 'label': Label(scrollable_frame, text="planID: ")},
                    planItemID={'entry': Entry(scrollable_frame),
                                'label': Label(scrollable_frame, text="planItemID: ")},
                    processComponentID={'entry': Entry(scrollable_frame),
                                        'label': Label(scrollable_frame, text="processComponentID: ")},
                    processComponentName={'entry': Entry(scrollable_frame),
                                          'label': Label(scrollable_frame, text="processComponentName: ")},
                    processComponentVersion={'entry': Entry(scrollable_frame),
                                             'label': Label(scrollable_frame, text="processComponentVersion: ")},
                    originator={'entry': Entry(scrollable_frame),
                                'label': Label(scrollable_frame, text="originator: ")},
                    priority={'entry': Entry(scrollable_frame), 'label': Label(scrollable_frame, text="priority: ")},
                    actualProcessStep={'entry': Entry(scrollable_frame),
                                       'label': Label(scrollable_frame, text="actualProcessStep: ")},
                    entity={'entry': Entry(scrollable_frame), 'label': Label(scrollable_frame, text="entity: ")},
                    operation={'entry': Entry(scrollable_frame), 'label': Label(scrollable_frame, text="operation: ")},
                    command={'entry': Entry(scrollable_frame), 'label': Label(scrollable_frame, text="command: ")})

# draw data element labels and textboxes
i = 1
for element in dataElements:
    dataElements[element]["label"].grid(row=i, sticky=E)
    dataElements[element]["entry"].grid(row=i, column=1, sticky=W, ipadx=100)
    i += 1

    # variables for legacy functions
    FileName_Entry = dataElements["fileName"]["entry"]
    eTrackingId_Entry = dataElements["eTrackingId"]["entry"]
    iTrackingId_Entry = dataElements["iTrackingId"]["entry"]
    sourceApplication_Entry = dataElements["sourceApplication"]["entry"]
    sourceUser_Entry = dataElements["sourceUser"]["entry"]
    tenantId_Entry = dataElements["tenantId"]["entry"]
    timestamp_Entry = dataElements["timestamp"]["entry"]
    orderID_Entry = dataElements["orderID"]["entry"]
    orderRef_Entry = dataElements["orderRef"]["entry"]
    planID_Entry = dataElements["planID"]["entry"]
    planItemID_Entry = dataElements["planItemID"]["entry"]
    processComponentID_Entry = dataElements["processComponentID"]["entry"]
    processComponentName_Entry = dataElements["processComponentName"]["entry"]
    processComponentVersion_Entry = dataElements["processComponentVersion"]["entry"]
    originator_Entry = dataElements["originator"]["entry"]
    priority_Entry = dataElements["priority"]["entry"]
    actualProcessStep_Entry = dataElements["actualProcessStep"]["entry"]
    entity_Entry = dataElements["entity"]["entry"]
    operation_Entry = dataElements["operation"]["entry"]
    command_Entry = dataElements["command"]["entry"]

myLable3 = Text(rightFrame)
myLable3.pack(ipadx=250, ipady=250)

# Characteristics part
# command_Lable = Label(topFrame, text="command: ")
characteristicsLabel = Label(scrollable_frame, text="Characteristics")
characteristicsLabel.grid(row=21, column=0, pady=15, sticky=E)


# Request input
# requestInput = Entry(topFrame)
# requestInput.grid(row=0, column=1)
# requestInput.pack(side = LEFT)  #ipadx=150, ipady=200
# requestInput.pack(side=LEFT, fill=X, expand=TRUE)

def printsumstuff(event):
    global chvar1
    global chvar2

    # print(chvar1.get())
    # print(chvar2.get())
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

    # list with variables to write to file
    var_list = [eTrackingId, iTrackingId, sourceApplication, sourceUser, tenantId, timestamp, orderID, orderRef, planID,
                planItemID, processComponentID, processComponentName, processComponentVersion, originator, priority,
                actualProcessStep, entity, operation, command]
    str_list = ['${eTrackingId}', '${iTrackingId}', '${sourceApplication}', '${sourceUser}', '${tenantId}',
                '${timestamp}', '${orderID}', '${orderRef}', '${planID}', '${planItemID}', '${processComponentID}',
                '${processComponentName}', '${processComponentVersion}', '${originator}', '${priority}',
                '${actualProcessStep}', '${entity}', '${operation}', '${command}']
    # print(var_list)
    # print(str_list)

    if FileName != "":
        # Raw xml
        ind = 0

        # replace funky vars by real vars
        with open(Path('templates/facade_template.xml')) as oldfile, open(Path("out/raw/" + FileName + '.xml'),
                                                                          'w') as newfile:
            for line in oldfile:
                if any(s in line for s in str_list):
                    if str(var_list[ind]) != "":
                        line = line.replace(str_list[ind], str(var_list[ind]))
                        newfile.write(line)
                        ind += 1
                    else:
                        newfile.write("")
                        ind += 1
                else:
                    newfile.write(line)
            with open(Path("templates/characteristics_templates.xml"), 'r') as file:
                characteristics_temp = file.read()
                print(characteristics_temp)
                var = []
                val = []
                print(len(characteristicsNameEntry))
                for i in range(len(characteristicsNameEntry)):
                    print(i)
                    var.append(lowCharacteristicsFrame.nametowidget("characteristicNameEntry" + str(i)).get())
                    val.append(lowCharacteristicsFrame.nametowidget("characteristicEntry" + str(i)).get())
                    print(val)
                    haha = str(var[i])
                    ahaha = str(val[i])

                    # print(haha)
                    characteristic_temp = characteristics_temp.replace('${ATRIBUTE}', ahaha)
                    characteristi_temp = characteristic_temp.replace('ATNAME', '"' + haha + '"')
                    # print(characteristi_temp)
                    newfile.write(characteristi_temp)
            # zapsani koncovky xml
            with open(Path("templates/end_facade_template.xml"), 'r') as file:
                end_temp = file.read()
                newfile.write(end_temp)
    else:
        print("badluck1")
    #####################################################################################################################
    if FileName != "":
        if chvar2.get() == 1:
            # create parametrized file request
            ind = 0
            # zapsani requestu

            with open(Path('templates/facade_template.xml')) as oldfile, open(
                    Path("out/xml/" + FileName + 'Parametrized.xml'), 'w') as newfile:
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
                # zapsani charakteristik
                with open(Path("templates/characteristics_templates.xml"), 'r') as file:
                    characteristics_temp = file.read()
                    # print(characteristics_temp)
                    var = []
                    for i in range(len(characteristicsNameEntry)):
                        # print(i)
                        var.append(lowCharacteristicsFrame.nametowidget("characteristicNameEntry" + str(i)).get())
                        # print(var)
                        haha = var[i]
                        # print(haha)
                        characteristic_temp = characteristics_temp.replace('${ATRIBUTE}', '${' + haha + '}')
                        characteristi_temp = characteristic_temp.replace('ATNAME', '"' + haha + '"')
                        # print(characteristi_temp)
                        newfile.write(characteristi_temp)

                # zapsani koncovky xml
                with open(Path("templates/end_facade_template.xml"), 'r') as file:
                    end_temp = file.read()
                    newfile.write(end_temp)
        else:
            print("badluck2")
        if chvar1.get() == 1:
            # .csv file
            with open(Path("templates/csv_template.csv"), 'r') as file:
                csv_temp = file.read()
                f = open(Path("out/csv/" + FileName + ".csv"), 'w')
                f.write(csv_temp)
                for i in range(len(characteristicsNameEntry)):
                    var.append(lowCharacteristicsFrame.nametowidget("characteristicNameEntry" + str(i)).get())
                    # print(var)
                    haha = var[i]
                    # print(haha)
                    f.write(',' + str(haha))
                f.write("\n")

            f.write(str(eTrackingId) + ',' + str(iTrackingId) + ',' + str(sourceApplication) + ',' + str(
                sourceUser) + ',' + str(tenantId) + ',' + str(timestamp) + ',' + str(orderID) + ',' + str(
                orderRef) + ',' + str(planID) + ',' + str(planItemID) + ',' + str(processComponentID) + ',' + str(
                processComponentName) + ',' + str(processComponentVersion) + ',' + str(originator) + ',' + str(
                priority) + ',' + str(actualProcessStep) + ',' + str(entity) + ',' + str(operation) + ',' + str(
                command))
            var2 = []
            for i in range(len(characteristicsEntry)):
                var2.append(lowCharacteristicsFrame.nametowidget("characteristicEntry" + str(i)).get())
                # print(var2)
                haha2 = var2[i]
                # print(haha2)
                f.write(',' + str(haha2))
            f.close()
        else:
            print("badluck3")
        if chvar2.get() == 1:
            # output
            f = open(Path("out/xml/" + FileName + "Parametrized.xml"), 'r')
            file = f.read()
            output = myLable3.get("1.0", 'end-1c')
            if output != "":
                myLable3.delete('1.0', END)
            myLable3.insert(END, file)
            f.close()

        # delete filename
        FileName_Entry.delete(0, 'end')
        FileName_Entry['bg'] = 'WHITE'
    else:
        FileName_Entry['bg'] = 'RED'


###########################################################
def addChar(self, charName="", charValue=""):
    global counter
    global characteristicsValueEntry
    global characteristicsNameEntry
    counter += 1
    # print(counter)
    characteristics.append("characteristic" + str(counter - 1))
    characteristics[-1] = Label(lowCharacteristicsFrame, text=characteristics[-1])
    characteristics[-1].grid(row=21 + counter, column=0, sticky=E)

    characteristicsNameEntry.append(Entry(lowCharacteristicsFrame, name="characteristicNameEntry" + str(counter - 1)))
    characteristicsNameEntry[-1].grid(row=21 + counter, column=1, sticky=E)

    characteristicsEntry.append(Entry(lowCharacteristicsFrame, name="characteristicEntry" + str(counter - 1)))
    characteristicsEntry[-1].grid(row=21 + counter, column=2, sticky=E)

    characteristicsNameEntry[-1].insert(0, charName)
    characteristicsEntry[-1].insert(0, charValue)

    # print(characteristicsEntry)
    # print(characteristicsNameEntry)


# delete a characteristic
def deleteChar():
    global counter
    # get last added characteristic elements
    labelToDestroy = characteristics[-1]
    characteristicsEntryToDestroy = characteristicsEntry[-1]
    characteristicsNameEntryToDestroy = characteristicsNameEntry[-1]

    # destroy a characteristic
    labelToDestroy.destroy()
    characteristicsEntryToDestroy.destroy()
    characteristicsNameEntryToDestroy.destroy()

    # unset elements from element list
    characteristics.remove(characteristics[-1])
    characteristicsEntry.remove(characteristicsEntry[-1])
    characteristicsNameEntry.remove(characteristicsNameEntry[-1])
    counter -= 1


# preset values
def presetValues():
    eTrack = randint(1000000000, 1001223218)
    planIdRan = randint(100, 999)
    planItemIdRan = randint(10, 99)
    compID = randint(100, 999)

    # "{0:0=2d}".format(a)
    timeStampMonth = "{0:0=2d}".format(randint(1, 12))
    timeStampDay = "{0:0=2d}".format(randint(1, 28))
    timeStampHour = "{0:0=2d}".format(randint(0, 23))
    timeStampMinute = "{0:0=2d}".format(randint(0, 59))
    timeStampSecond = "{0:0=2d}".format(randint(0, 59))

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
        processComponentName_Entry.delete(0, 'end')
        processComponentVersion_Entry.delete(0, 'end')
        originator_Entry.delete(0, 'end')
        priority_Entry.delete(0, 'end')
        actualProcessStep_Entry.delete(0, 'end')
        # entity_Entry.insert(END, '')
        # operation_Entry.insert(END, '')
        # command_Entry.insert(END, '')
    # set some default filename
    filename = "Zmen mi jmeno"
    FileName_Entry.insert(END, filename)
    eTrackingId_Entry.insert(END, 'O-' + str(eTrack))
    iTrackingId_Entry.insert(END, "TMCZ-" + str(planIdRan) + "-" + str(planItemIdRan))
    sourceApplication_Entry.insert(END, 'tmcz.telekom.it.architecture.COM:COM')
    sourceUser_Entry.insert(END, 'TEMP_sourceUser')
    tenantId_Entry.insert(END, 'TMCZ')
    # timestamp_Entry.insert(END, '2020-03-014T10:38:00Z')
    timestamp_Entry.insert(END, "2020-" + timeStampMonth + "-" + timeStampDay + "T"
                           + timeStampHour + ":" + timeStampMinute + ":" + timeStampSecond + "Z")
    orderID_Entry.insert(END, 'TEMP_interni_FOM_ID')
    orderRef_Entry.insert(END, 'O-' + str(eTrack))
    planID_Entry.insert(END, str(planIdRan))
    planItemID_Entry.insert(END, str(planItemIdRan))
    processComponentID_Entry.insert(END, str(compID))
    processComponentName_Entry.insert(END, 'TEMP_processComponentName')
    processComponentVersion_Entry.insert(END, '1')
    originator_Entry.insert(END, 'node1')
    priority_Entry.insert(END, '4')
    actualProcessStep_Entry.insert(END, 'TEMP_actualProcessStep')
    # entity_Entry.insert(END, '')
    # operation_Entry.insert(END, '')
    # command_Entry.insert(END, '')


def openFile():
    file = Path(filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")]))

    records = list()
    with open(file, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append(row)

# remove all characteristics fields
    while (counter > 0):
        deleteChar()
# select the first record
    record = records[0]

    textboxFilename = dataElements["fileName"]["entry"]
    textboxFilename.delete(0,"end")
    textboxFilename.insert(0,file.stem)

    for key, value in record.items():
        if key in dataElements:
            textbox = dataElements[key]["entry"]
            textbox.delete(0, "end")
            textbox.insert(0, value)
        else:
            addChar("", key, value)


##############
#####Buttons
##############
#Characteristics part
# command_Lable = Label(topFrame, text="command: ")
characteristicsLabel = Label(midButtonFrame, text="Characteristics  ")
characteristicsLabel.grid(row=0, column=0, pady=15, sticky=E)

#main button
requestButton = Button(bottomFrame, text="Generate request")
requestButton.grid(row=0, sticky=N)
requestButton.bind("<Button-1>", printsumstuff)

#labels for file generation
# Label(bottomFrame, text="csv").grid(row=1, column=0, sticky=S)
chkbtn1 = Checkbutton(bottomFrame, text="csv", variable=chvar1, onvalue = 1, offvalue = 0)
chkbtn2 = Checkbutton(bottomFrame, text="xml", variable=chvar2, onvalue = 1, offvalue = 0)
chkbtn1.grid(row=1, column=0, sticky=W)
chkbtn2.grid(row=2, column=0, sticky=W)


#secondary button
addCharacteristicButton = Button(midButtonFrame, text="Add a characteristic")
addCharacteristicButton.grid(row=0, column=1, pady=15)
addCharacteristicButton.bind("<Button-1>", addChar)

#tertiary button
setValuesButton = Button(midButtonFrame, text="Delete a characteristic", command=deleteChar)
setValuesButton.grid(row=0, column=2, pady=15)

#quaternary button
setValuesButton = Button(topButtonFrame, text="Generate values", command=presetValues)
setValuesButton.grid(row=0, column=1, pady=15, sticky=W)
openFileButton = Button(topButtonFrame, text="Open file", command=openFile)
openFileButton.grid(row=0, column=2, pady=15, sticky=W)

topFrame.mainloop()
