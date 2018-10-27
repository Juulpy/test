#--import section--
import time, random, sys, webbrowser, pyautogui, fileinput
import tkinter as tk
from tkinter import messagebox
from tkinter import Entry

#FAILSAFE
pyautogui.FAILSAFE = True

#Random
interval = random.uniform(0.03, 0.05)

#Typer
def Type():
	#Auto-typer ('Text', delay=[var]')
	time.sleep(2)
	text_file = open('vocab.txt', "r") #opens vocab.txt
	a = (text_file.read()) #reads vocab.txt
	pyautogui.typewrite((a), interval=(interval)) #starts
	text_file.close()
	res = tk.messagebox.showwarning('warning','PythonAutoTyper (beta-demo) closes after one run')
	sys.exit()
def FixVocab():
        with open('vocab.txt', 'r') as file:
                filedata = file.read()
        filedata = filedata.replace("'", "' ")
        filedata = filedata.replace("é", "'e")
        filedata = filedata.replace("è", "`e")
        filedata = filedata.replace("á", "'a")
        filedata = filedata.replace("à", "'a")
        filedata = filedata.replace("ù", "'u")
        filedata = filedata.replace("û", "^u")
        filedata = filedata.replace("î", "^i")
        filedata = filedata.replace("ô", "^o")
        filedata = filedata.replace("ê", "^e")
        filedata = filedata.replace("â", "^a")
        filedata = filedata.replace("ç", "'c")

        with open('vocab.txt', 'w') as file:
                file.write(filedata)

        file.close()


#Open vocab.txt
def Open():
        webbrowser.open("vocab.txt")

def Exit():
	res = tk.messagebox.askyesno('Exit','Exit?')
	if res == True:
		sys.exit()

#---GUI---
root = tk.Tk()
root.title("PythonAutoTyper")
root.geometry("200x200")

root.resizable(False, False)
#root.iconbitmap('ico.ico')

def createWindow():
	top = tk.Toplevel()
	top.title('About')
	root.columnconfigure(0, weight=1)
	tutorial_message = "Using PyListMaker: \n \n \n 1. Open vocab.txt and copy your text into it. Make sure it's in the right order, with a new line for every new word and without empty lines.\n \n 2. Click FixVocab to make sure the characters will appear in the right way \n \n 3. Click 'Start PyAutoTyper' and select your destination.\n \n IMPORTANT: To kill the task, move your mouse to the upper right corner. \n\n\n PyAutoTyper v0.4 (beta-demo version), made by Julian Petit."
	msg = tk.Message(top, text = tutorial_message, padx = 100).grid(row=0, column=1) #side='top', fill='both', expand='yes'
	button = tk.Button(top, text='OK', command=top.destroy).grid(row=2, column=1)
	top.mainloop()

#Button(Open file)


tk.Label(text='PyAutoTyper',font='Helvetica', fg='darkblue').grid(row=0,column=0)
typeButton = tk.Button(text="Start PyAutoTyper", command=Type).grid(row=1, column=0)
root.columnconfigure(0, weight=1)

openButton = tk.Button(text="Open vocab.txt", command=Open).grid(row=2, column=0)

fixVocab = tk.Button(text="Fix vocab.txt", command=FixVocab).grid(row=3, column=0)

createWindow = tk.Button(text='About', command = createWindow).grid(row=4, column=0)

exitButton = tk.Button(text="Exit", command=Exit).grid(row=5, column=0)
#Button(Start typing)


#Button(exit)


#Button(Fix vocab) (TEST)


root.mainloop()
#------
