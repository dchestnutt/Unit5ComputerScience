######################################################
## Example tKinkter Code for use in GUI Development ##
######################################################

# ***** Import Functions ***** #

from tkinter import *                   # This will import ALL (*) from the tkinter library.
from tkinter import Menu                # Menu and messagebox seem to have to be imported separately (probs bc it's python idk :/)
from tkinter import messagebox as ms    # <- Libraries/subroutines can be imported as other names if defined like this. 

window = Tk()                   # <- This line defines the name of the window variable which we will call throughout our program.

window.geometry('1000x500+0+0')          # <- This line declares the size of window which tkinter should draw when it runs the code.
# window.configure(background='#202C4F') # <- This code can be used to set the background colour for the tKinter window.
window.title("Example Code")             # <- This line declares the text displayed at the top of the drawn window.

# ***** Defining the Variables which will be used to return user-entered values ***** #

variableToBeReturned = StringVar()      # Each of these varibles will be used to return data from the entered forms to our
dropDownListVariableName = StringVar()  # database. They must be declared here along with their data-type before they can be
radiobuttonVariableName = IntVar()      # referenced in out tkinter code. Note that these are ONLY variables used to RETURN
checkbuttonVariableName1 = IntVar()     # data. Variables used to store data (e.g. the lists which store data for the 
checkbuttonVariableName2 = IntVar()     # Dropdown Menu Entry do not need to be declared here.

# ***** Define Functions to be called Later ***** #

def doNothing():
    print("Okay... Doing Nothing.")

# ***** Menu Bar ***** #

menu = Menu(window) # Declares the menu function as part of our tkinter interface.

dropdown1 = Menu(menu) 

dropdown1.add_command(label='Option 1', command=doNothing) # These three options are for the entities of the cascade. Each one can be
dropdown1.add_command(label='Option 2', command=doNothing) # selected in order to trigger a process (e.g. save). This is similar to the
dropdown1.add_command(label='Option 3', command=doNothing) # command button, however, ss many can be added as needed.

menu.add_cascade(label='Dropdown Label 1', menu=dropdown1) # <- This line defines the header label which the cascade will fall below.

window.config(menu=menu)

# ***** Simple Label (No Entry ***** #

labelTitle = Label(window, 
                   text="Text to be Displayed", 
                   width=20, 
                   font=("bold", 20),
                   anchor=CENTER)                       # This is a label which will display text to the user. It does
labelTitle.grid(row=0, column=0, columnspan=3)          # not take any form of data entry.
# In these examples I am using the grid function of tKinter. By using this we can devide the window into grids which we can then place elements into 
# respectively. In these examples I have three columns, on each row in the first column is the label and spread between the second and third columns 
# are the entries. Columns will shrink to the size of the smallest element in them. 

# ***** Simple Text Entry ***** #

labelSimpleTextEntry = Label(window, 
                             text="Simple Text Entry: ", 
                             width=20, 
                             font=("bold", 10),
                             anchor=E)                          # This will take simple StringVar or IntVar data entry
labelSimpleTextEntry.grid(row=2, column=0)                          # from a user and return this using the predefined
entrySimpleTextEntry = Entry(window, textvar=variableToBeReturned)  # variable. This code will create a box for the data
entrySimpleTextEntry.grid(row=2, column=1, columnspan=2)            # to be entered by the user.

# ***** Drop Down Menu Entry ***** #

labelDropDownEntry = Label(window, 
                           text="Dropdown Menu Entry: ", 
                           width=20, 
                           font=("bold", 10),
                           anchor=E,
                           cursor='hand2')                                                # This allows for the user to select one option from
labelDropDownEntry.grid(row=3, column=0)                                            # a dropdown list of options. The list must be assigned
dropdownListOfOptions = ['Option 1', 'Option 2', 'Option 3'];                       # either here or previously. The chosen value will be
droplist = OptionMenu(window, dropDownListVariableName, *dropdownListOfOptions)     # returned as the predefined variable.
droplist.config(width=20, cursor='hand2')                   
dropDownListVariableName.set('Select Option from List')                             # It is also possible (using the code on this line) to set
droplist.grid(row=3, column=1, columnspan=2)                                        # a predefined text to display before an option is picked.

# ***** Radiobutton Entry ***** #

labelRadiobuttonEntry = Label(window, 
                              text="Radiobutton Entry: ", 
                              width=20, 
                              font=("bold", 10),
                              anchor=E)                     # This allows for the user to select only
labelRadiobuttonEntry.grid(row=3, column=0)                 # one option. The chosen option will be 
Radiobutton(window,                                         # returned as the predefined varibale. 
            text="Option 1", 
            padx = 5,
            variable=radiobuttonVariableName,
            cursor='hand2',
            value=1).grid(row=4, column=1) 
Radiobutton(window, 
            text="Option 2", 
            padx = 5, 
            variable=radiobuttonVariableName,
            cursor='hand2',
            value=2).grid(row=4, column=2)

# ***** Checkbutton Entry ***** #

labelCheckbuttonEntry = Label(window,                       # This allows for the user to select more than one option.
                              text="Checkbutton Entry: ",   # It will then return these as the predefined variable. They
                              width=20,                     # will be default-set to have no selection.
                              font=("bold", 10),
                              anchor=E)  
labelCheckbuttonEntry.grid(row=5, column=0)                                                    
Checkbutton(window, 
            text="Option 1", 
            cursor='hand2',
            variable=checkbuttonVariableName1,
            onvalue='Yes', offvalue='No').grid(row=5, column=1)  
Checkbutton(window, 
            text="Option 2", 
            cursor='hand2',
            variable=checkbuttonVariableName2,
            onvalue='Yes', offvalue='No').grid(row=5, column=2)   

# ***** Spacer Label using Grid Function ***** #

spacerLabel = Label(window, text=" ", width=20)
spacerLabel.grid(row=6, column=0, columnspan=3)

# ***** Command Button ***** #

Button(window, text='Command to Execute', width=20, bg='darkblue', fg='white', command=doNothing).grid(row=7, column=0, columnspan=3)
# These buttons can be used to trigger a command to be executed. Ususally this command is defined in a function previously in our
# program, however, it could also be included here. For example, this button could be used to trigger a function which collects the
# user-inputs from each field in the form and appends them to a database.

window.mainloop() # This will run the main loop of tKinter code.