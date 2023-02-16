import PySimpleGUI as sg

#Set the theme for the frames (I need to check them some more to see what other themes are offered!)
sg.theme("Dark Grey 5")

def Butt(buttonText):
    buttonText = str(buttonText)
    if buttonText.isdigit():
        keyNum = "-NUM-" + buttonText
    elif "Exit" in buttonText:
        keyNum = "-EXIT-"
    else:
        keyNum = "-OP-" + buttonText
    return sg.Button(buttonText, size=("5", "1"), key=keyNum)

layout = [
    [sg.Text(size=(12,1), key='-OUT-')],
    [Butt(i) for i in ("AC", "/")],
    [Butt(i) for i in list(range(1, 4)) + ["*"]],
    [Butt(i) for i in list(range(4, 7)) + ["-"]],
    [Butt(i) for i in list(range(7, 10)) + ["+"]],
    [Butt(i) for i in ("Exit", "0", "=")],
]

#Create the window
window = sg.Window("Calculator", layout)

#Creates the list for the numbers
numString = ""

event = "-NUM-0"
print(event)

#Forever loop to process events and gather values
while event != "-EXIT-":
    event, values = window.read()
    #Checks if the window was closed or if the EXIT button was pressed, if so it closes the loop
    if event == sg.WIN_CLOSED or event == "-EXIT-":
        break
    #Checks if the key contains "-NUM-" and if so it takes the last char (the actual num) and adds it to the numString
    elif "-NUM-" in event:
        print(f"Event: {event}")
        #Adds the num and updates the window
        numString += event[-1]
        window['-OUT-'].update(numString)
        print(f"Event: {event}")
        print(f"numString: {numString}")
    #Checks if the key contains "-OP-" and if so it takes the last char (the operend) and adds it to the numString
    elif "-OP-" in event:
        if "=" in event:
            #It updates the window to display the eval of the entire numString
            window['-OUT-'].update(f"{numString} = {eval(numString)}")
            print(f"{numString} = {eval(numString)}")
            #Clears the num string
            numString = ""
        #Checks if the end of the numstring has any other operend, if so it doesn't add a new one
        elif "AC" in event:
            print(f"CLEAR!")
            #If it's clear then it.. clears it! (Sets it to an empty string)
            numString = ""
            window['-OUT-'].update(numString)
        elif numString[-1] == "+" or numString[-1] == "-" or numString[-1] == "*" or numString[-1] == "/":
            print(f"No. No doubles.")
        #If it is allowed to add the operend it does so here and updates the window
        else:
            numString += event[-1]
            window['-OUT-'].update(numString)
            print(f"Event: {event}")
            print(f"numString: {numString}")
    #Checks if the event is the enter key

    #Checks if the event is to clear

    else:
        print(f"Break")
        break

#Closes the window!
window.close()
