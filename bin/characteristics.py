from tkinter import *
class Characteristics_class:
    def __init__(self, frame):
        # # command_Lable = Label(topFrame, text="command: ")
        # self.characteristicsLabel = Label(frame, text="Characteristics  ")
        # self.characteristicsLabel.grid(row=0, column=0, pady=15, sticky=E)
        #
        # # secondary button
        # self.addCharacteristicButton = Button(frame, text="Add a characteristic")
        # self.addCharacteristicButton.grid(row=0, column=1, pady=15)
        # self.addCharacteristicButton.bind("<Button-1>", self.addChar)
        #
        # # tertiary button
        # self.setValuesButton = Button(frame, text="Delete a characteristic", command=self.deleteChar)
        # self.setValuesButton.grid(row=0, column=2, pady=15)
        print("initialized")

    def addChar(self, string):
        #(self, frame, characteristics, characteristicsEntry, characteristicsNameEntry, counter, charName="", charValue="")
        print(str(string))



        # counter += 1
        # # print(counter)
        # characteristics.append("characteristic" + str(counter - 1))
        # characteristics[-1] = Label(frame, text=characteristics[-1])
        # characteristics[-1].grid(row=21 + counter, column=0, sticky=E)
        #
        # characteristicsNameEntry.append(
        #     Entry(frame, name="characteristicNameEntry" + str(counter - 1)))
        # characteristicsNameEntry[-1].grid(row=21 + counter, column=1, sticky=E)
        #
        # characteristicsEntry.append(Entry(frame, name="characteristicEntry" + str(counter - 1)))
        # characteristicsEntry[-1].grid(row=21 + counter, column=2, sticky=E)
        #
        # characteristicsNameEntry[-1].insert(0, charName)
        # characteristicsEntry[-1].insert(0, charValue)

    # delete a characteristic
    def deleteChar(self, characteristics, characteristicsEntry, characteristicsNameEntry):
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
