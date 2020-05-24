
from tkinter import *
from tkinter.ttk import Frame, Label, Style, Notebook
import os


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()




    def initUI(self):
############################## SETTINGS ARE IN HERE

        self.starting_dir = os.getcwd()
        self.toptext = "starting directory"+os.getcwd()

        self.mainfile = None # this will chang if you want it to

        self.master.title("File Helper")
        self.pack(fill=BOTH, expand=1)
        
        Style().configure("TFrame", background="#333")# backgroundcolor


#############################
        #top part

        
        self.toppart = Frame(self)
        self.toppart.pack(fill=X)


        self.nbt = Notebook(self.toppart)#.first)
        self.nbt.pack(fill=X, expand=1)

        # Adds tab 1 of the notebook    top tab 1
        self.paget1top = Frame(self.nbt)
        self.nbt.add(self.paget1top, text='Home')
        

        # Adds tab 2 of the notebook     top tab 2
        self.paget2top = Frame(self.nbt)
        self.nbt.add(self.paget2top, text='Settings')

#############################################    top tabs
            #FRAMES
        
        self.tab2frame1 = Frame(self.paget2top)
        self.tab2frame1.pack(fill=X)

        self.tab2frame2 = Frame(self.paget2top)
        self.tab2frame2.pack(fill=X)

        self.tab2frame3 = Frame(self.paget2top)
        self.tab2frame3.pack(fill=X)

        self.tab2frame4 = Frame(self.paget2top)
        self.tab2frame4.pack(fill=X)
        

##
        self.Labelone0 = Label(self.tab2frame1, text="SETTINGS")
        self.Labelone0.pack()
        
        self.Labelone1 = Label(self.tab2frame2, text="Current directory")
        self.Labelone1.pack(side=LEFT)
        '''
        self.Labelone2 = Label(self.tab2frame2, text=self.mainfile)#self.starting_dir)#self.mainfile)
        self.Labelone2.pack(side=RIGHT)
        '''
        self.Labelone2 = Listbox(self.tab2frame2, width=60, height=1)#self.starting_dir)#self.mainfile)
        self.Labelone2.pack(side=RIGHT)
        
        self.labchange = Label(self.tab2frame3, text="Change Dir^")#self.mainfile)
        self.labchange.pack(side=LEFT)
        
        self.changecwd = Entry(self.tab2frame3)#self.mainfile)
        self.changecwd.pack(fill=X)

        self.changedirb = Button(self.tab2frame3, text="change", command=self.changedir)
        self.changedirb.pack(side=RIGHT)
        


###############################3        
        
        self.first = Frame(self.master)
        self.first.pack(fill=X)
        
        self.nb = Notebook(self)#.first)
        self.nb.pack(fill=X, expand=1)#grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

        # Adds tab 1 of the notebook
        self.page1 = Frame(self.nb)
        self.nb.add(self.page1, text='Tools')
        

        # Adds tab 2 of the notebook
        self.page2 = Frame(self.nb) 
        self.nb.add(self.page2, text='Find file')
        


        
######################           middle tabs
        
        self.firstFrame = Frame(self.page1)
        self.firstFrame.pack(fill=X)

        self.secFrame = Frame(self.page1)
        self.secFrame.pack(fill=X)
        
        self.test = Button(self.firstFrame, text='current dir', command=self.pwdcomm)
        self.test.pack(side=LEFT)

        self.test = Button(self.firstFrame, text='list folders', command=self.listfolders)
        self.test.pack(side=LEFT)
        
        self.test = Button(self.firstFrame, text='list dir', command=self.listdircomm)
        self.test.pack(side=LEFT)
        
        self.test = Button(self.firstFrame, text='About', command=self.imageTop)
        self.test.pack(side=LEFT)#side=LEFT)

        #self.resizeEntry = Entry(self.firstFrame)
        #self.resizeEntry.pack(side=LEFT)
        '''
        Style().configure("TFrame", background="#333")
        
        self.lbl = Label(self.secFrame,text = "A list of favourite countries...")  
        '''
        self.listbox = Listbox(self.secFrame)#self.secFrame)  
        
        #self.lbl.pack(fill=X)  
        self.listbox.pack(fill=X)



        #page 2
        self.sfirstFrame = Frame(self.page2)
        self.sfirstFrame.pack(fill=X)

        self.ssecFrame = Frame(self.page2)
        self.ssecFrame.pack(fill=X)

        self.therFrame = Frame(self.page2)
        self.therFrame.pack(fill=X)

        self.fourFrame = Frame(self.page2)
        self.fourFrame.pack(fill=X)
        
        '''
        self.tests = Button(self.sfirstFrame, text='current dir')#, command=self.pwdcomm)
        self.tests.pack(side=LEFT)
        '''

        
        self.Labelone = Label(self.sfirstFrame, text="Path to search")
        self.Labelone.pack(side=LEFT)

        self.entrypath = Entry(self.sfirstFrame)
        self.entrypath.pack(fill=X)

        self.Labelt = Label(self.ssecFrame, text="File Name")
        self.Labelt.pack(side=LEFT)

        self.entrypatht = Entry(self.ssecFrame)
        self.entrypatht.pack(fill=X)

        self.buttonfind = Button(self.therFrame, text="FIND", command=self.find_all)
        self.buttonfind.pack(side=LEFT)

        self.exlp = Label(self.therFrame, text="Enter two of the other / instead on one")
        self.exlp.pack()

        self.findlistb = Listbox(self.fourFrame)
        self.findlistb.pack(fill=BOTH)
        

    def find_all(self):
        r = ''
        self.findlistb.delete(1, END)
        path = self.entrypath.get()
        name = self.entrypatht.get()
        result = []
        for root, dirs, files in os.walk(path):
            if name in files:
                result.append(os.path.join(root, name))

        if '\\\\' in str(result):
            r = str(result).replace('\\\\','\\')

        else:
            pass
        self.findlistb.insert(1, str(r))
    #C:\\Users\\root\\Desktop\\hour82
        

    def pwdcomm(self):
        try:
            self.listbox.delete(0, END)
        except:
            pass
        cwd = self.mainfile
        #cwd = os.getcwd()
        if cwd == None:
            self.listbox.insert(0,os.getcwd())
        else:
            self.listbox.insert(0,cwd)


    def listdircomm(self):
        f = []
        try:
            self.listbox.delete(0, END)
        except:
            pass
        self.listbox.insert(END,"Files")
        self.listbox.insert(END,"-----------")
        cwd = self.mainfile
        #cwd = os.getcwd()
        li = os.listdir(cwd)
        for x in li:  #add a if no . in x its not a file so dont add
            f.append(x)
        for x in f:
            self.listbox.insert(END,x)

            
    def listfolders(self):
        try:
            self.listbox.delete(0, END)
        except:
            pass
        self.listbox.insert(END,"Directorys")
        self.listbox.insert(END,"-----------")
        cwd = self.mainfile
        #cwd = os.getcwd()
        subfolders = [f.path for f in os.scandir(cwd) if f.is_dir() ]
        
        for x in subfolders:
             self.listbox.insert(END,os.path.split(x)[1])

             
    def imageTop(self):
        self.top = Toplevel(self.page1)
        self.top.title("About this application...")

        self.msg = Message(self.top, text="This is so I can find\n files without\nworrying about\nfinding viruses.")
        self.msg.pack()

        self.buttons = Button(self.top, text="Dismiss", command=self.top.destroy)
        self.buttons.pack()

    def changedir(self):
        self.Labelone2.delete(0, END)
        text = self.changecwd.get()
        self.mainfile = text
        self.Labelone2.insert(END, text)

    
        
    
        
def main():

    root = Tk()
    root.geometry("500x500")#400x380+400+400")
    app = Example()

    # gives weight to the cells in the grid
    
    rows = 0
    while rows < 50:
        root.rowconfigure(rows, weight=1)
        root.columnconfigure(rows, weight=1)
        rows += 1
    
    root.mainloop()


if __name__ == '__main__':
    main()


