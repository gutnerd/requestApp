import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd


class data_elements_class:
    def __init__(self, frame):
        global dataElements
        self.dataElements = dict(fileName={'entry': Entry(frame), 'label': Label(frame, text="Filename: ")},
                            eTrackingId={'entry': Entry(frame),
                                         'label': Label(frame, text="eTrackingId: ")},
                            iTrackingId={'entry': Entry(frame),
                                         'label': Label(frame, text="iTrackingId: ")},
                            sourceApplication={'entry': Entry(frame),
                                               'label': Label(frame, text="sourceApplication: ")},
                            sourceUser={'entry': Entry(frame),
                                        'label': Label(frame, text="sourceUser: ")},
                            tenantId={'entry': Entry(frame), 'label': Label(frame, text="tenantId: ")},
                            timestamp={'entry': Entry(frame), 'label': Label(frame, text="timestamp: ")},
                            orderID={'entry': Entry(frame), 'label': Label(frame, text="orderID: ")},
                            orderRef={'entry': Entry(frame), 'label': Label(frame, text="orderRef: ")},
                            planID={'entry': Entry(frame), 'label': Label(frame, text="planID: ")},
                            planItemID={'entry': Entry(frame),
                                        'label': Label(frame, text="planItemID: ")},
                            processComponentID={'entry': Entry(frame),
                                                'label': Label(frame, text="processComponentID: ")},
                            processComponentName={'entry': Entry(frame),
                                                  'label': Label(frame, text="processComponentName: ")},
                            processComponentVersion={'entry': Entry(frame),
                                                     'label': Label(frame, text="processComponentVersion: ")},
                            originator={'entry': Entry(frame),
                                        'label': Label(frame, text="originator: ")},
                            priority={'entry': Entry(frame), 'label': Label(frame, text="priority: ")},
                            actualProcessStep={'entry': Entry(frame),
                                               'label': Label(frame, text="actualProcessStep: ")},
                            entity={'entry': Entry(frame), 'label': Label(frame, text="entity: ")},
                            operation={'entry': Entry(frame), 'label': Label(frame, text="operation: ")},
                            command={'entry': Entry(frame), 'label': Label(frame, text="command: ")})

        # draw data element labels and textboxes
        i = 1
        for element in self.dataElements:
            self.dataElements[element]["label"].grid(row=i, sticky=E)
            self.dataElements[element]["entry"].grid(row=i, column=1, sticky=W, ipadx=100)
            i += 1

            # variables for legacy functions
            FileName_Entry = self.dataElements["fileName"]["entry"]
            eTrackingId_Entry = self.dataElements["eTrackingId"]["entry"]
            iTrackingId_Entry = self.dataElements["iTrackingId"]["entry"]
            sourceApplication_Entry = self.dataElements["sourceApplication"]["entry"]
            sourceUser_Entry = self.dataElements["sourceUser"]["entry"]
            tenantId_Entry = self.dataElements["tenantId"]["entry"]
            timestamp_Entry = self.dataElements["timestamp"]["entry"]
            orderID_Entry = self.dataElements["orderID"]["entry"]
            orderRef_Entry = self.dataElements["orderRef"]["entry"]
            planID_Entry = self.dataElements["planID"]["entry"]
            planItemID_Entry = self.dataElements["planItemID"]["entry"]
            processComponentID_Entry = self.dataElements["processComponentID"]["entry"]
            processComponentName_Entry = self.dataElements["processComponentName"]["entry"]
            processComponentVersion_Entry = self.dataElements["processComponentVersion"]["entry"]
            originator_Entry = self.dataElements["originator"]["entry"]
            priority_Entry = self.dataElements["priority"]["entry"]
            actualProcessStep_Entry = self.dataElements["actualProcessStep"]["entry"]
            entity_Entry = self.dataElements["entity"]["entry"]
            operation_Entry = self.dataElements["operation"]["entry"]
            command_Entry = self.dataElements["command"]["entry"]





