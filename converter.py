#!/usr/bin/env python3
import copy
from random import randint, random
import random
import string
from tkinter import *  # pip install
from tkinter import ttk
from tkinter import filedialog
from xml.etree import ElementTree as ET
from pathlib import Path
import csv
from bin import data_elements as de

# Okno
root = Tk()
root.geometry("900x700")
root.title("Facade request generator")

# setup

global records
records = list()

global recordLabelString
recordLabelString = StringVar()
recordLabelString.set("1/1")

global selectedRecordNumber
selectedRecordNumber = 0

global totalRecordsCount
totalRecordsCount = 1

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
canvas.create_window((140, 0), window=topButtonFrame, anchor="nw")
canvas.create_window((77, 545), window=midButtonFrame, anchor="nw")
canvas.create_window((77, 600), window=lowCharacteristicsFrame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

topFrame.pack(side=LEFT, anchor=N, padx=25, pady=25)
canvas.pack(side=LEFT, fill="both", expand=TRUE, ipady=500, ipadx=100)
scrollbar.pack(side=RIGHT, fill=Y)

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM, padx=25, pady=25)
rightFrame = Frame(root)
rightFrame.pack(side=RIGHT, anchor=N, padx=25, pady=25)

global var_list
global myElements
myElements = de.data_elements_class(scrollable_frame)
entries_list, var_list, dataElements = myElements.get_entries()
print(entries_list)
print(var_list)

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
    entries_list, var_list, notgonnause = myElements.get_entries()

    global characteristicsValueEntry
    global characteristicsNameEntry
    saveCurrentRecord()

    FileName = entries_list[0].get()
    eTrackingId = var_list[0]
    iTrackingId = var_list[1]
    sourceApplication = var_list[2]
    sourceUser = var_list[3]
    tenantId = var_list[4]
    timestamp = var_list[5]
    orderID = var_list[6]
    orderRef = var_list[7]
    planID = var_list[8]
    planItemID = var_list[9]
    processComponentID = var_list[10]
    processComponentName = var_list[11]
    processComponentVersion = var_list[12]
    originator = var_list[13]
    priority = var_list[14]
    actualProcessStep = var_list[15]
    entity = var_list[16]
    operation = var_list[17]
    command = var_list[18]

    # list with variables to write to file
    # var_list = [eTrackingId, iTrackingId, sourceApplication, sourceUser, tenantId, timestamp, orderID, orderRef, planID,
    #             planItemID, processComponentID, processComponentName, processComponentVersion, originator, priority,
    #             actualProcessStep, entity, operation, command]
    print(var_list)
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
        #csv file
        if chvar1.get() == 1:

            filepath = Path("out/csv/" + FileName + ".csv")
            saveCSV(filepath)





        #     # .csv file
        #     with open(Path("templates/csv_template.csv"), 'r') as file:
        #         csv_temp = file.read()
        #         f = open(Path("out/csv/" + FileName + ".csv"), 'w')
        #         f.write(csv_temp)
        #         for i in range(len(characteristicsNameEntry)):
        #             var.append(lowCharacteristicsFrame.nametowidget("characteristicNameEntry" + str(i)).get())
        #             # print(var)
        #             haha = var[i]
        #             # print(haha)
        #             f.write(',' + str(haha))
        #         f.write("\n")
        #
        #     f.write(str(eTrackingId) + ',' + str(iTrackingId) + ',' + str(sourceApplication) + ',' + str(
        #         sourceUser) + ',' + str(tenantId) + ',' + str(timestamp) + ',' + str(orderID) + ',' + str(
        #         orderRef) + ',' + str(planID) + ',' + str(planItemID) + ',' + str(processComponentID) + ',' + str(
        #         processComponentName) + ',' + str(processComponentVersion) + ',' + str(originator) + ',' + str(
        #         priority) + ',' + str(actualProcessStep) + ',' + str(entity) + ',' + str(operation) + ',' + str(
        #         command))
        #     var2 = []
        #     for i in range(len(characteristicsEntry)):
        #         var2.append(lowCharacteristicsFrame.nametowidget("characteristicEntry" + str(i)).get())
        #         # print(var2)
        #         haha2 = var2[i]
        #         # print(haha2)
        #         f.write(',' + str(haha2))
        #     f.close()
        # else:
        #     print("badluck3")
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
        entries_list[0].delete(0, 'end')
        entries_list[0]['bg'] = 'WHITE'
    else:
        entries_list[0]['bg'] = 'RED'


def saveCSV(filepath):
    global records
    csvcolumns = list(records[0])
    with open(filepath, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csvcolumns, lineterminator='\n')
        writer.writeheader()
        writer.writerows(records)


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


def getRandomString(stringLength):
    lettersAndDigits = string.ascii_lowercase + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(stringLength)))


# preset values
def presetValues():
    eTrack = "S-5-2" + str(getRandomString(5)) + "-" + str(getRandomString(8)) + "-fw-" + str(randint(00000, 999999))
    # S-5-2bsiwgy-pita20zi-fw-O23218
    # S-5-2d9cckg-piuyux3s-fw-O59351

    planIdRan = randint(100, 999)
    planItemIdRan = randint(10, 99)
    compID = randint(100, 999)
    priority = random.choice("24567")

    # "{0:0=2d}".format(a)
    timeStampMonth = "{0:0=2d}".format(randint(1, 12))
    timeStampDay = "{0:0=2d}".format(randint(1, 28))
    timeStampHour = "{0:0=2d}".format(randint(0, 23))
    timeStampMinute = "{0:0=2d}".format(randint(0, 59))
    timeStampSecond = "{0:0=2d}".format(randint(0, 59))

    if entries_list[1].get() != "":
        rangeForLoop = len(entries_list) - 4
        for r in range(rangeForLoop):
            entries_list[r + 1].delete(0, 'end')

    entries_list[1].insert(END, eTrack)
    entries_list[2].insert(END, "TMCZ-" + str(planIdRan) + "-" + str(planItemIdRan))
    entries_list[3].insert(END, 'SOFacadeTMCZ')
    entries_list[4].insert(END, 'sndr:tmcz.telekom.it.architecture.COM:COM')
    entries_list[5].insert(END, 'TMCZ')
    entries_list[6].insert(END, "2020-" + timeStampMonth + "-" + timeStampDay + "T"
                           + timeStampHour + ":" + timeStampMinute + ":" + timeStampSecond + "Z")
    entries_list[7].insert(END, 'TEMP_interni_FOM_ID')
    entries_list[8].insert(END, eTrack)
    entries_list[9].insert(END, str(planIdRan))
    entries_list[10].insert(END, str(planItemIdRan))
    entries_list[11].insert(END, str(compID))
    entries_list[12].insert(END, 'TEMP_processComponentName')
    entries_list[13].insert(END, '1')
    entries_list[14].insert(END, 'node1')
    entries_list[15].insert(END, priority)
    entries_list[16].insert(END, 'TEMP_actualProcessStep')
    # entity_Entry.insert(END, '')
    # operation_Entry.insert(END, '')
    # command_Entry.insert(END, '')


def openFile():
    file = Path(filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")]))
    if file.name == "":
        return False

    global records
    records = list()
    with open(file, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            records.append(row)
            print(str(row))

    # select the first record
    record = records[0]
    global totalRecordsCount
    totalRecordsCount = len(records)
    global selectedRecordNumber
    selectedRecordNumber = 0
    updateRecordLabel()

    printRecord(record)

    # display filename
    entries_list[0].delete(0, "end")
    entries_list[0].insert(0, file.stem)

def printRecord(record):
    # remove all characteristics fields
    while counter > 0:
        deleteChar()

    # delete all textbox values except filename
    rangeForLoop = len(entries_list)
    for r in range(rangeForLoop)[1:]:
        entries_list[r].delete(0, 'end')

    # Write values. if it does not exist, add it as a characterstic.
    for key, value in record.items():
        if key in dataElements:
            textbox = dataElements[key]["entry"]
            textbox.delete(0, "end")
            textbox.insert(0, value)
        else:
            addChar("", key, value)


def goToRecord(shift):
    global selectedRecordNumber
    global totalRecordsCount

    # check if not out of bounds
    if shift < 0 and selectedRecordNumber + shift < 0:
        return False

    if shift > 0 and selectedRecordNumber + shift >= totalRecordsCount:
        return False

    saveCurrentRecord()

    selectedRecordNumber += shift
    updateRecordLabel()

    # display selected record
    record = records[selectedRecordNumber]
    printRecord(record)


def updateRecordLabel():
    recordLabelString.set(str(selectedRecordNumber + 1) + "/" + str(totalRecordsCount))


def saveCurrentRecord():
    global selectedRecordNumber
    global records
    global totalRecordsCount

    record = {}

    # remove filename it will not be saved
    elements = copy.copy(myElements.get())
    try:
        elements.pop("fileName")
    except:
        pass

    # write data in textboxes to record (excecpt characterstics)
    for key in elements:
        record[key] = elements[key]["entry"].get()

    # write characteristics
    for name, value in zip(characteristicsNameEntry, characteristicsEntry):
        record[name.get()] = value.get()

    # finally, write record into records element
    try:
        records[selectedRecordNumber] = record
    except:
        records.append(record)

    # save characteristic name/count change for all records
    #   create a new mini dict of new chars only
    new_keys_list = list(record)
    del new_keys_list[:19]
    new_values = record.values()
    new_values_list = list(new_values)
    del new_values_list[:19]
    newchars = {}
    for key, value in zip(new_keys_list, new_values_list):
        newchars[key] = value


    for oldrecord in records:
        # get characteristic keys - index 19 and up
        old_keys_list = list(oldrecord)
        del old_keys_list[:19]

                              
        # get values for keys
        old_values = oldrecord.values()
        old_values_list = list(old_values)
        del old_values_list[:19]


        # create a new mini dict of chars only, delete chars from old record
        oldchars = {}
        for key, value in zip(old_keys_list, old_values_list):
            oldchars[key] = value
            try:
                del oldrecord[key]
            except:
                pass

        #replace old chars with new with old values
        for key in newchars:
            if key in oldchars:
                oldrecord[key] = oldchars[key]
            else:
                oldrecord[key] = ""


        print("oldchar: " + str(oldchars))
        print("newchar: " + str(newchars))


        # put new characteristics with old values

        # keysList = list(record)
        #
        # loopRange = range(len(record))
        #
        # for i in loopRange:
        #     # skip non characteristic elements
        #     if i >= 19:
        #         continue
        #     # save values of old characteristic
        #     # record[]


    print(str(len(record)))
    print(record)

    # for element in elements:
    # print(elements)

    # rangeForLoop = len(entries_list)
    # for r in range(rangeForLoop):
    #     record[r] =
    #     entries_list[r].delete(0, 'end')
    #
    # i = range(counter)
    # for

    return True


def addRecord():
    global selectedRecordNumber
    global totalRecordsCount
    global records

    saveCurrentRecord()
    totalRecordsCount += 1
    selectedRecordNumber = totalRecordsCount - 1
    records.append({})
    updateRecordLabel()

    return True

def deleteRecord():
    global selectedRecordNumber
    global totalRecordsCount
    global records

    if totalRecordsCount <= 1:
        return False

    totalRecordsCount -= 1
    if selectedRecordNumber + 1 > totalRecordsCount:
        selectedRecordNumber = totalRecordsCount - 1
    del records[-1]
    updateRecordLabel()
    printRecord(records[selectedRecordNumber])

    return True

def saveCSVbutton():
    saveCurrentRecord()
    filepath = Path(filedialog.asksaveasfilename(filetypes=[("CSV files", "*.csv")]))
    if filepath.name == "":
        return False

    saveCSV(filepath)

##############
#####Buttons
##############
# Characteristics part
# command_Lable = Label(topFrame, text="command: ")
characteristicsLabel = Label(midButtonFrame, text="Characteristics  ")
characteristicsLabel.grid(row=0, column=0, pady=15, sticky=E)

# main button
requestButton = Button(bottomFrame, text="Generate request")
requestButton.grid(row=0, sticky=N)
requestButton.bind("<Button-1>", printsumstuff)

# labels for file generation
# Label(bottomFrame, text="csv").grid(row=1, column=0, sticky=S)
chkbtn1 = Checkbutton(bottomFrame, text="csv", variable=chvar1, onvalue=1, offvalue=0)
chkbtn2 = Checkbutton(bottomFrame, text="xml", variable=chvar2, onvalue=1, offvalue=0)
chkbtn1.grid(row=1, column=0, sticky=W)
chkbtn2.grid(row=2, column=0, sticky=W)
chkbtn1.select()
chkbtn2.select()

# secondary button
addCharacteristicButton = Button(midButtonFrame, text="Add a characteristic")
addCharacteristicButton.grid(row=0, column=1, pady=15)
addCharacteristicButton.bind("<Button-1>", addChar)

# tertiary button
setValuesButton = Button(midButtonFrame, text="Delete a characteristic", command=deleteChar)
setValuesButton.grid(row=0, column=2, pady=15)

# quaternary button
openFileButton = Button(topButtonFrame, text="Open file", command=openFile)
openFileButton.grid(row=0, column=1, pady=15, padx=(0,20), sticky=W)

setValuesButton = Button(topButtonFrame, text="Generate values", command=presetValues)
setValuesButton.grid(row=0, column=2, pady=15, padx=(0,32), sticky=W)

prevRecordButton = Button(topButtonFrame, text="←", width=2, command=lambda: goToRecord(-1))
prevRecordButton.grid(row=0, column=3, pady=15, sticky=W)

recordLabel = Label(topButtonFrame, font=(None, 14), textvariable=recordLabelString)
recordLabel.grid(row=0, column=4, pady=15, sticky=W)

nextRecordButton = Button(topButtonFrame, text="→", width=2, command=lambda: goToRecord(1))
nextRecordButton.grid(row=0, column=5, pady=15, sticky=W)

AddRecordButton = Button(topButtonFrame, text="+", width=2, command=addRecord)
AddRecordButton.grid(row=0, column=6, pady=15, padx=(10,0), sticky=W)

DeleteRecordButton = Button(topButtonFrame, text="-", width=2, command=deleteRecord)
DeleteRecordButton.grid(row=0, column=7, pady=15, sticky=W)

saveCSVButton = Button(topButtonFrame, text="Save to CSV", command=saveCSVbutton)
saveCSVButton.grid(row=0, column=8, pady=15, padx=10, sticky=W)

topFrame.mainloop()
