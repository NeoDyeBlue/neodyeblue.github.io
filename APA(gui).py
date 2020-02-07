import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import datetime
from tkinter.filedialog import asksaveasfile 

ac = 1 #author count
auth = [] #where all author input was stored
Firstn = [] #this is where the first name initials will be stored
references = [] #this is where all confirmed citations are stored unsorted
sorted_ref = [] #this is where all confirmed citations are stored sorted

#destroys the intro window and proceed to Generator----------------------------------------------------------------------------------------------------------------------------------------------------------
def strt_now():
    """This function for 'Generate now!' button destroys the first widgets on root window, resizes the window then proceeds to Generator class."""
    
    tbdstryed = [a, ps, asso, web, welframe,creator]
    for e in range(len(tbdstryed)):
        tbdstryed[e].destroy()
        
    root.geometry('590x700')
    root.resizable(False,False)
    
    Generator(root).place()
#Generator---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Generator(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self,master)
        self.master = master
        self.gui()
        
    def gui(self):
        """
        This method contains the widgets of generator GUI and also has the variables, lists and loops:
        
        *Menu Bar
            -File
            -Help
        *'Enter details here' frame
            -Author frame
                >Author only radiobutton
                >Author count messagebox
                >'First:' label
                >First name entry
                >'M./M.I.:' label
                >Middle initial entry
                >'Last' label
                >Last name entry
                >Add author button
            -Corporate or Group of authors frame
                >Corporate or Group only radiobutton
                >Corporate or Group of authors entry
            -Publishing Date frame
                >'Month' label
                >Month dropdown menu
                >'Day' label
                >Day dropdown menu
                >'Year' label
                >Year dropdown menu
            -Retrieval Date frame
                >'Month' label
                >Month dropdown menu
                >'Day' label
                >Day dropdown menu
                >'Year' label
                >Year dropdown menu
            -Title & URL frame
                >'Title/Website' entry
                >Title/Website name entry
                >'URL' label
                >URL entry
            -'APA' label
            -Create button
        *'Editable result (no indents)' frame
            -editable result text box
            -Confirm button
            -Discard button
        *'Final result' frame
            -final result text box
            -add another citation button
            -clear all button
        """
        
        self.menubar = Menu(self.master)
        self.fmenu = Menu(self.menubar, tearoff=0)
        self.fmenu.add_command(label="Save as...", command= self.file_save)
        self.fmenu.add_separator()
        self.fmenu.add_command(label="Exit", command=self.master.destroy)
        self.menubar.add_cascade(label="File", menu=self.fmenu)
    
        self.hlpmenu = Menu(self.menubar, tearoff=0)
        self.hlpmenu.add_command(label="About...", command=self.hlp)
        self.menubar.add_cascade(label="Help", menu=self.hlpmenu)
        self.master.config(menu=self.menubar)
    
        self.labelframe = LabelFrame(self.master, text="Enter Details Here",font = ('impact', 10), height = 263, width = 580)
        self.labelframe.place(x = 5, y = 5)

        self.apa = Label(self.labelframe, text = "APA", font=('impact',80))
        self.apa.place(x = 383, y = 35)
        self.citate = Button(self.labelframe, text ="Create",activebackground ='gray', height = 4, width = 28, command = self.start)
        self.citate.place(x = 362, y = 161)
    
        #Author(s)-GUI---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        global ac
        
        self.a_frame = LabelFrame(self.labelframe, height = 42, width = 566).place(x  = 5, y = 8)
        self.auth_count = tk.Message(self.labelframe, text = ac, font = ('impact',7), relief=SUNKEN)
        self.auth_count.place(x = 67, y = -1)
        
        self.author_f = Label(self.a_frame, text = "First:").place(x = 15, y = 43)
        self.author_f_ent = Entry(self.a_frame, width = 13, state = 'normal')
        self.author_f_ent.place(x = 48, y = 45)
        self.author_f_ent.var = tk.StringVar()
        self.author_f_ent['textvariable'] = self.author_f_ent.var
        self.author_f_ent.var.trace_add('write',self.toggle)
        
        self.author_m = Label(self.a_frame, text = "M./M.I.:").place(x = 135, y = 43)
        self.author_m_ent = Entry(self.a_frame, width = 4, state = 'normal')
        self.author_m_ent.place(x= 184, y = 45)
        self.author_m_ent.var = tk.StringVar()
        self.author_m_ent['textvariable'] = self.author_m_ent.var
        self.author_m_ent.var.trace_add('write',self.toggle)

        self.author_l = Label(self.a_frame, text = "Last:").place(x = 218, y = 43)
        self.author_l_ent = Entry(self.a_frame, width = 13, state = 'normal')
        self.author_l_ent.place(x= 250, y = 45)
        self.author_l_ent.var = tk.StringVar()
        self.author_l_ent['textvariable'] = self.author_l_ent.var
        self.author_l_ent.var.trace_add('write',self.toggle)

        self.reg_or_corp_var = StringVar()
        self.reg_or_corp_var.set("author")

        self.auth_rb = Radiobutton(self.a_frame, text = "Author", font = ('impact',8), variable = self.reg_or_corp_var, value = "author", command = self.lock)
        self.auth_rb.place(x = 16, y = 20)

        self.add_a = Button(self.a_frame, text = "+",activebackground = 'gray', command = self.add_authr, state = 'disabled')
        self.add_a.place(x = 337, y =41)

        self.corp_or_grp = LabelFrame(self.labelframe, height = 42, width = 217).place(x=354,y=8)
        self.cg_rb = Radiobutton(self.corp_or_grp, text = "Corporate or Group of authors", font = ('impact', 8),variable = self.reg_or_corp_var, value = "group", command = self.lock, state = 'normal')
        self.cg_rb.place(x = 365, y = 20)
        self.cg_ent = Entry(self.corp_or_grp, width = 33, state = 'disabled')
        self.cg_ent.place(x = 368, y = 45)
        
        #Publishing and Retrieval Date-GUI-----------------------------------------------------------------------------------------------------------------------------------------------------------
        self.p_frame = LabelFrame(self.labelframe, text = "Publishing Date", font = ('impact', 8), height = 50, width = 351).place(x = 5, y = 50)
        self.r_frame = LabelFrame(self.labelframe, text = "Retrieval Date", font = ('impact', 8), height = 50, width = 351).place(x = 5, y = 100)

        self.Months = ["","January","February","March","April","May","June","July","August","September","October","November","December"]

        self.mp_var = StringVar(self.master)
        self.mp_var.set(self.Months[0])

        self.mr_var = StringVar(self.master)
        self.mr_var.set(self.Months[0])

        self.mp = OptionMenu(self.p_frame, self.mp_var, *self.Months)
        self.mp.place(x = 58, y = 90)
        self.mr = OptionMenu(self.r_frame, self.mr_var, *self.Months)
        self.mr.place(x = 58, y = 140)

        self.p_month = Label(self.p_frame, text = "Month:").place(x = 15, y = 94)
        self.r_month = Label(self.r_frame, text = "Month:").place(x = 15, y = 145)

        self.Days = ["",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

        self.dp_var = StringVar(self.master)
        self.dp_var.set(self.Days[0])

        self.dr_var = StringVar(self.master)
        self.dr_var.set(self.Days[0])

        self.dp = OptionMenu(self.p_frame, self.dp_var, *self.Days)
        self.dp.place(x = 193, y = 90)
        self.dr = OptionMenu(self.r_frame, self.dr_var, *self.Days)
        self.dr.place(x = 193, y = 140)

        self.p_day = Label(self.p_frame, text = "Day:").place(x = 167, y = 94)
        self.p_month = Label(self.r_frame, text = "Day:").place(x= 167, y = 144)

        self.Years = [""]
        self.Y = now.year
        while (self.Y >= 1000):
            self.Years.append(self.Y)
            self.Y -= 1
            
        self.yp_var = StringVar(self.master)
        self.yp_var.set(self.Years[0])

        self.yr_var = StringVar(self.master)
        self.yr_var.set(self.Years[0])

        self.yp = OptionMenu(self.p_frame, self.yp_var, *self.Years)
        self.yp.place(x = 288, y = 90)
        self.yr = OptionMenu(self.r_frame, self.yr_var, *self.Years)
        self.yr.place(x = 288, y = 140)

        self.p_year = Label(self.p_frame, text = "Year:").place(x = 259, y = 94)
        self.r_year = Label(self.r_frame, text = "Year:").place(x = 259, y = 144)

        #Title and URL-GUI-----------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.tandu = LabelFrame(self.labelframe, text = "Title & URL", font = ('impact',8), height = 86, width = 351).place(x = 5, y = 150)
        self.title = Label(self.tandu, text = "Title/Website name:").place(x = 15, y = 196)
        self.title_ent = Entry(self.tandu, width = 37)
        self.title_ent.place(x = 128, y = 197)

        self.url = Label(self.tandu, text = "URL:").place(x=15, y= 226)
        self.url_ent = Entry(self.tandu, width = 51)
        self.url_ent.place(x = 45, y =227)

        #Editable result-GUI---------------------------------------------------------------------------------------------------------------------------------------------------------------    
        self.confirmframe = LabelFrame(self.master, text = "Editable Result (no indents)", font = ('impact',10), height = 110, width = 580).place(x = 5, y = 268)
        self.ed_result = Text(self.confirmframe, height = 3, width =70, state = 'disabled')
        self.ed_result.place(x = 12, y = 288)
        self.confirm_b = Button(self.confirmframe, text = "Confirm", activebackground = 'gray', width = 38, state = 'disabled', command = self.Confirm)
        self.confirm_b.place(x = 12, y = 345)
        self.discard_b = Button(self.confirmframe, text = "Discard", activebackground = 'gray', width = 38, state = 'disabled', command = self.Discard)
        self.discard_b.place(x = 300, y = 345)

        #Final result-GUI------------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.finalframe = LabelFrame(self.master, text = "Final Result", font = ('impact',10), height = 289, width = 580).place(x = 5, y = 378)
        self.finalresult = Text(self.finalframe, height = 14, width = 70)
        self.finalresult.place(x = 12, y = 398)
        self.finalresult.config(state = DISABLED)
        self.add_b = Button(self.finalframe, text = "Add another citation!",activebackground = 'gray', width = 38, state = 'disabled', command = self.add_another)
        self.add_b.place(x = 12, y = 633)
        self.clear_b = Button(self.finalframe, text = "Clear all", activebackground = 'gray', width = 38, state = 'disabled', command = self.clear_all)
        self.clear_b.place(x = 300, y = 633)

    #help and about-GUI----------------------------------------------------------------------------------------------------------------------------------------------------------------
    def hlp(self):
        """Here the help and about widgets are defined"""
        
        self.menubar.entryconfig("Help", state = 'disabled')
        self.menubar.entryconfig("File", state = 'disabled')
        self.hlpframe = LabelFrame(self.master, text = "Help & About", font = ('impact', 10), width = 580, height = 662)
        self.hlpframe.place(x = 5, y = 5)
        self.abt = LabelFrame(self.hlpframe, width = 566, height = 111)
        self.abt.place(x = 5)
        self.abtproj = Label(self.abt, text = "A Program for citating web pages using APA 6th edition, commonly used in social sciences:")
        self.abtproj.place(x=35, y = 20)
        self.projtitle = Label(self.abt, text = "APA 6th Edition Web Citation Generator", font = ('impact', 25))
        self.projtitle.place(x = 16, y = 40)
        self.how2use = LabelFrame(self.hlpframe, text = "How to use?", font = ('impact', 8), width = 566, height = 400)
        self.how2use.place(x = 5, y = 110)
        self.inst1 = Label(self.how2use, text = "◾ Enter the required details first and click \"Create\":", justify = LEFT)
        self.inst1.place(x = 1, y = 1)
        self.inst1auth = Label(self.how2use, text = "▸ You can choose if the article's author is one or more author or a group of authors.", justify = LEFT)
        self.inst1auth.place(x = 25, y = 20)
        self.inst1auth2 = Label(self.how2use, text = "▸ By adding another author, enter the name of the first author to activate the \"+\" button to add \n    another one.", justify = LEFT)
        self.inst1auth2.place(x=25, y = 40)
        self.inst1dates = Label(self.how2use, text = "▸ Click the dropdown menus of Months, Days, and Years to choose for the article's date of \n    publication and the date of when did you retrieved it.",justify = LEFT)
        self.inst1dates.place(x=25, y= 75)
        self.inst1datestip = Label(self.how2use, text = "▸ If the article does not have a date of publication, just leave it blank or you can set it to none, \n    same goes for retrieval date if you don't want to include it.",justify = LEFT)
        self.inst1datestip.place(x = 25, y = 113)
        self.inst2edit = Label(self.how2use, text = "◾ In Editable result you can make changes on your created citation:", justify = LEFT)
        self.inst2edit.place(x = 1, y = 160)
        self.inst2conf = Label(self.how2use, text = "▸ Click \"Confirm\" to save changes and move on to Final result or \"Discard\" to go back to creating \n    a new citation.",justify = LEFT)
        self.inst2conf.place(x=25, y = 180)
        self.inst3final = Label(self.how2use, text = "◾ The Final result adds indents and handles the citations alphabetically:",justify = LEFT)
        self.inst3final.place(x = 1, y = 225)
        self.inst3add = Label(self.how2use, text = "▸ To add another citation to the reference list click \"Add another citation!\".",justify = LEFT)
        self.inst3add.place(x = 25, y = 245)
        self.inst3dis = Label(self.how2use, text = "▸ If you clicked \"Clear all\" it'll prompt you to clear the reference list, once confirmed it cannot \n    be undone.", justify = LEFT)
        self.inst3dis.place(x = 25, y = 265)
        self.inst4sav = Label(self.how2use, text = "◾ Saving the reference list by \".txt\" or \".doc\" type:",justify = LEFT)
        self.inst4sav.place(x = 1, y = 310)
        self.inst4how = Label(self.how2use, text = "▸ You can save the reference list by going to \"File\", \"Save as...\".", justify=LEFT)
        self.inst4how.place(x = 25, y = 330)
        self.inst4note = Label(self.how2use, text = "▸ Once the file has been saved, you can't make changes on it using the program.", justify = LEFT)
        self.inst4note.place(x = 25, y = 350)
        self.lbl = LabelFrame(self.hlpframe, width = 566, height = 55)
        self.lbl.place(x = 5, y = 515)
        self.built = Label(self.lbl, text = "Built using Python", font = 'impact')
        self.built.place(x = 225)
        self.jp = Label(self.lbl, text = "John Paul G. Zoleta     Bachelor of Science in Computer Science     College of Mary Immaculate")
        self.jp.place(x =25, y = 25)

        self.ok = Button(self.hlpframe, text = "Okay ⌐■_■",activebackground = 'gray', command = self.hlpframeclear, width = 79, height = 3)
        self.ok.place(x = 6, y = 575)

    #---Okay ⌐■_■ button function---------------------------------------------------------------------------------------------------------------------------------------------------------------   
    def hlpframeclear(self):
        """returns the file and help to normal state then forgets the help frame widget"""
        
        self.menubar.entryconfig("File", state = 'normal')
        self.menubar.entryconfig("Help", state = 'normal')
        self.hlpframe.place_forget()

    #---checks if author has entry before enabling the + button----------------------------------------------------------------------------------------------------------------------------
    def toggle(self, *_):
        """checks if any of the first, m and last has input then activates the '+' button"""
            
        global ac
        if self.author_f_ent.var.get():
            self.add_a['state'] = 'normal'
        elif self.author_m_ent.var.get():
            self.add_a['state'] = 'normal'
        elif self.author_l_ent.var.get():
            self.add_a['state'] = 'normal'
        else:
            self.add_a['state'] = 'disabled'

    #---here author that has been added will be formatted and appended---------------------------------------------------------------------------------------------------------------------
    def add_authr(self):
        
        global ac
        global auth
        global Firstn
        
        self.first = self.author_f_ent.get()
        self.middle = self.author_m_ent.get()
        self.last = self.author_l_ent.get()
        self.First = self.first.title()
        self.Middle = self.middle.title()
        self.Last = self.last.title()
            
        #if first only
        if len(self.First) != 0 and len(self.Middle) == 0 and len(self.Last) == 0:
            auth.append("{0}".format(self.First))
            ac += 1            
        #if all has input
        elif len(self.First) != 0 and len(self.Middle) != 0 and len(self.Last) != 0:
            self.F = self.First.split()
            for char in self.F:
                Firstn.append(char[0])
            self.F0 = ".".join(Firstn)
            auth.append("{0}, {1}. {2}".format(self.Last, self.F0, self.Middle))
            Firstn.clear()
            ac += 1            
        #if last only
        elif len(self.First) == 0 and len(self.Middle) == 0 and len(self.Last) != 0:
            auth.append("{0}".format(self.last))
            ac += 1            
        #if first and last only
        elif len(self.First) != 0 and len(self.Middle) == 0 and len(self.Last) != 0:
            self.F = self.First.split()
            for char in self.F:
                Firstn.append(char[0])
            self.F0 = ".".join(Firstn)
            auth.append("{0}, {1}.".format(self.last, self.F0))
            Firstn.clear()
            ac += 1
        #if first and middle only
        elif len(self.First) != 0 and len(self.Middle) != 0 and len(self.Last) == 0:
            self.F = self.First.split()
            for char in self.F:
                Firstn.append(char[0])
            self.F0 = ".".join(Firstn)
            auth.append("{0}, {1}".format(self.F0, self.Middle))
            Firstn.clear()
            ac += 1
        #if middle only
        elif len(self.First) == 0 and len(self.Middle) != 0 and len(self.Last) == 0:
            auth.append("{0}".format(self.Middle))
            ac += 1
        #if middle and last only
        elif len(self.First) == 0 and len(self.Middle) != 0 and len(self.Last) != 0:
            auth.append("{0}, {1}".format(self.Last, self.Middle))
            ac += 1
                    
        self.auth_count.configure(text = ac)
        self.author_f_ent.delete(0, 'end')
        self.author_m_ent.delete(0, 'end')
        self.author_l_ent.delete(0, 'end')
        self.add_a.config(state = DISABLED)
        
        if ac == 2:
            self.cg_rb.configure(state = 'disabled')
            self.cg_rb.update()
            self.cg_ent.configure(state = 'disabled')
            self.cg_ent.update()

    #---locks the entry of user to authors or group----------------------------------------------------------------------------------------------------------------------------------------
    def lock(self):
        self.chk = self.reg_or_corp_var.get()
        if self.chk == "author":
            if self.author_f_ent['state'] == 'disabled' and self.author_m_ent['state'] == 'disabled' and self.author_l_ent['state'] == 'disabled':
                self.author_f_ent.configure(state = 'normal')
                self.author_f_ent.update()
                self.author_m_ent.configure(state = 'normal')
                self.author_m_ent.update()
                self.author_l_ent.configure(state = 'normal')
                self.author_l_ent.update()
                self.cg_ent.configure(state = 'disabled')
                self.cg_ent.update()
        elif self.chk == "group":
            if self.cg_ent['state'] == 'disabled':
                self.cg_ent.configure(state = 'normal')
                self.cg_ent.update()
                self.author_f_ent.configure(state = 'disabled')
                self.author_f_ent.update()
                self.author_m_ent.configure(state = 'disabled')
                self.author_m_ent.update()
                self.author_l_ent.configure(state = 'disabled')
                self.author_l_ent.update()
    
    #---start here where the create button starts getting the author or group entries------------------------------------------------------------------------------------------------------    
    def start(self):
        """Starts getting the authors first before proceeding to the next"""
        global Firstn
        global auth
        self.chck = self.reg_or_corp_var.get()
        if self.chck == "author":
            self.tobeget = [self.author_f_ent.get(), self.author_m_ent.get(), self.author_l_ent.get()]
            self.Firstnme = self.tobeget[0].title()
            self.Middlenme = self.tobeget[1].title()
            self.Lastnme = self.tobeget[2].title()       
            #if all inputs are complete
            if len(self.Firstnme) != 0 and len(self.Middlenme) != 0 and len(self.Lastnme) != 0:
                self.Fi = self.Firstnme.split()
                for char in self.Fi:
                    Firstn.append(char[0])                    
                self.F1 = ".".join(Firstn)
                auth.append("{0}, {1}. {2}".format(self.Lastnme, self.F1, self.Middlenme))
                Firstn.clear()        
            #if f only   
            elif len(self.Firstnme) != 0 and len(self.Middlenme) == 0 and len(self.Lastnme) == 0:
                auth.append("{0}".format(self.Firstnme))        
            #if f and l only
            elif len(self.Firstnme) != 0 and len(self.Middlenme) == 0 and len(self.Lastnme) != 0:
                self.Fi = self.Firstnme.split()
                for char in self.Fi:
                    Firstn.append(char[0])
                self.F1 = ".".join(Firstn)
                auth.append("{0}, {1}.".format(self.Lastnme, self.F1))
                Firstn.clear()            
            #if l only
            elif len(self.Firstnme) == 0 and len(self.Middlenme) == 0 and len(self.Lastnme) != 0:
                auth.append("{0}".format(self.Lastnme))
            #if first and middle only
            elif len(self.Firstnme) != 0 and len(self.Middlenme) != 0 and len(self.Lastnme) == 0:
                self.Fi = self.Firstnme.split()
                for char in self.Fi:
                    Firstn.append(char[0])
                self.F1 = ".".join(Firstn)
                auth.append("{0}, {1}".format(self.F1, self.Middlenme))
                Firstn.clear()
            #if middle only
            elif len(self.Firstnme) == 0 and len(self.Middlenme) != 0 and len(self.Lastnme) == 0:
                auth.append("{0}".format(self.Middlenme))
            #if middle and last only
            elif len(self.Firstnme) == 0 and len(self.Middlenme) != 0 and len(self.Lastnme) != 0:
                auth.append("{0}, {1}".format(self.Lastnme, self.Middlenme))

            self.ref_formats()
            
        elif self.chck == "group":
            if len(self.cg_ent.get()) != 0:
                auth.append("{0}.".format(self.cg_ent.get()))
            else:
                pass
            
            self.ref_formats()

    #---here the details are formatted to apa web ciattion---------------------------------------------------------------------------------------------------------------------------------
    def ref_formats(self):
        global auth
        self.chek = self.reg_or_corp_var.get()
        self.titleandurl = [self.title_ent.get(), self.url_ent.get()]
        self.pub_date = [self.yp_var.get(), self.mp_var.get(), self.dp_var.get()]
        self.ret_date = [self.mr_var.get(), self.dr_var.get(), self.yr_var.get()]
        
        #get and format the pub dates first
        #complete date
        if len(self.pub_date[0]) != 0 and len(self.pub_date[1]) != 0 and len(self.pub_date[2]) != 0:
            self.pub_d = ("{0}, {1} {2}".format(self.pub_date[0], self.pub_date[1], self.pub_date[2]))
        #no year / month + day only
        elif len(self.pub_date[0]) == 0 and len(self.pub_date[1]) != 0 and len(self.pub_date[2]) != 0:
            self.pub_d = ("{1} {2}".format(self.pub_date[1], self.pub_date[2]))
        #no day / month + year only
        elif len(self.pub_date[0]) != 0 and len(self.pub_date[1]) != 0 and len(self.pub_date[2]) == 0:
            self.pub_d = ("{0}, {1}".format(self.pub_date[0], self.pub_date[1]))
        #no month / year + day only
        elif len(self.pub_date[0]) != 0 and len(self.pub_date[1]) == 0 and len(self.pub_date[2]) != 0:
            self.pub_d = ("{0}, {1}".format(self.pub_date[0], self.pub_date[2])) 
        #year only
        elif len(self.pub_date[0]) != 0 and len(self.pub_date[1]) == 0 and len(self.pub_date[2]) == 0:
            self.pub_d = ("{0}".format(self.pub_date[0]))
        #month only
        elif len(self.pub_date[0]) == 0 and len(self.pub_date[1]) != 0 and len(self.pub_date[2]) == 0:
            self.pub_d = ("{0}".format(self.pub_date[1]))
        #day only
        elif len(self.pub_date[0]) == 0 and len(self.pub_date[1]) == 0 and len(self.pub_date[2]) != 0:
            self.pub_d = ("{0}".format(self.pub_date[2]))
        elif len(self.pub_date[0]) == 0 and len(self.pub_date[1]) == 0 and len(self.pub_date[2]) == 0:
            self.pub_d = ("n.d.")
            
        #get and format the ret dates first
        #complete date
        if len(self.ret_date[0]) != 0 and len(self.ret_date[1]) != 0 and len(self.ret_date[2]) != 0:
            self.ret_d = ("{0} {1}, {2},".format(self.ret_date[0], self.ret_date[1], self.ret_date[2]))
        #no year / month + day only
        elif len(self.ret_date[0]) == 0 and len(self.ret_date[1]) != 0 and len(self.ret_date[2]) != 0:
            self.ret_d = ("{0} {1},".format(self.ret_date[1], self.ret_date[2]))
        #no day / month + year only
        elif len(self.ret_date[0]) != 0 and len(self.ret_date[1]) != 0 and len(self.ret_date[2]) == 0:
            self.ret_d = ("{0}, {1},".format(self.ret_date[0], self.ret_date[1]))
        #no month / year + day only
        elif len(self.ret_date[0]) != 0 and len(self.ret_date[1]) == 0 and len(self.ret_date[2]) != 0:
            self.ret_d = ("{0}, {1},".format(self.ret_date[0], self.ret_date[2])) 
        #year only
        elif len(self.ret_date[0]) != 0 and len(self.ret_date[1]) == 0 and len(self.ret_date[2]) == 0:
            self.ret_d = ("{0},".format(self.ret_date[0]))
        #month only
        elif len(self.ret_date[0]) == 0 and len(self.ret_date[1]) != 0 and len(self.ret_date[2]) == 0:
            self.ret_d = ("{0},".format(self.ret_date[1]))
        #day only
        elif len(self.ret_date[0]) == 0 and len(self.ret_date[1]) == 0 and len(self.ret_date[2]) != 0:
            self.ret_d = ("{0},".format(self.ret_date[2]))
            
        #without author
        if len(auth) == 0:
            #without author, without retrieval date
            if len(self.ret_date[0]) == 0 and len(self.ret_date[1]) == 0 and len(self.ret_date[2]) == 0:
                self.cite = ("{0}. ({1}). Retrieved from {2}".format(self.titleandurl[0], self.pub_d, self.titleandurl[1]))
                self.ed_frame(self.cite)
            #without author, with retrieval date
            else:
                self.cite = ("{0}. ({1}). Retrieved {2} from {3}".format(self.titleandurl[0], self.pub_d, self.ret_d, self.titleandurl[1]))
                self.ed_frame(self.cite)
        #with author
        else:
            #get and format the authors already
            if self.chek == "author":
                if len(auth) == 1:
                    self.authorrss = "".join(auth)
                elif len(auth) <= 7:
                    self.lastauth = auth.pop(-1)
                    self.ampersand = ("& {0}".format(self.lastauth)) 
                    auth.append(self.ampersand)
                    self.authorrss = ", ".join(auth)
                elif len(auth) > 7:
                    self.auth6 = []
                    self.lastauth = auth.pop(-1)
                    elipsis = ("...{0}".format(self.lastauth))
                    for aut in range(6):
                        self.auth6.append(auth[aut])
                    self.auth6.append(elipsis)
                    self.authorrss = ", ".join(self.auth6)
            elif self.chek == "group":
                self.authorrss = "".join(auth)
                
            #with author, without retrieval date
            if len(self.ret_date[0]) == 0 and len(self.ret_date[1]) == 0 and len(self.ret_date[2]) == 0:
                self.cite = ("{0} ({1}). {2}. Retrieved from {3}".format(self.authorrss, self.pub_d, self.titleandurl[0], self.titleandurl[1]))
                self.ed_frame(self.cite)
            #with author, with retrieval date
            else:
                self.cite = ("{0} ({1}). {2}. Retrieved {3} from {4}".format(self.authorrss, self.pub_d, self.titleandurl[0], self.ret_d, self.titleandurl[1]))
                self.ed_frame(self.cite)
                
        auth.clear()

    #---editable frame function----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
    def ed_frame(self, citation):
        self.ed_result.configure(state = 'normal')
        self.confirm_b.configure(state = 'normal')
        self.discard_b.configure(state = 'normal')
        
        self.tobedisabled = [self.citate, self.author_f_ent, self.author_m_ent, self.author_l_ent, self.mp, self.dp, self.yp, self.mr, self.dr, self.yr, self.title_ent, self.url_ent, self.cg_ent, self.auth_rb, self.cg_rb]
        for dis in self.tobedisabled:
            dis.configure(state = 'disabled')
            
        self.ed_result.insert(tk.END, citation)

    #---confirm button function----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
    def Confirm(self):
        """if the user clicks 'Confirm' it will append it to the list of references"""
        
        global references
        self.from_ed = self.ed_result.get("1.0",'end-1c')
        references.append(self.from_ed)
        self.confirm_b.configure(state = 'disabled')
        self.discard_b.configure(state = 'disabled')
        self.finalresult.configure(state = 'normal')
        self.finalresult.delete('1.0', END)
        
        self.final()

    #---discard button function----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
    def Discard(self):
        global ac
        
        self.ed_result.delete('1.0', END)
        self.tobeenabled = [self.author_f_ent, self.author_m_ent, self.author_l_ent, self.title_ent, self.url_ent, self.auth_rb, self.cg_rb, self.citate, self.mp, self.dp, self.yp, self.mr, self.dr, self.yr]
        for ena in self.tobeenabled:
            ena.configure(state = 'normal')
            
        self.clearedentry = [self.cg_ent, self.author_f_ent, self.author_m_ent, self.author_l_ent, self.title_ent, self.url_ent]
            
        for cle in self.clearedentry:
            cle.delete(0, END)
        
        self.mp_var.set(self.Months[0])
        self.dp_var.set(self.Days[0])
        self.yp_var.set(self.Years[0])
        self.mr_var.set(self.Months[0])
        self.dr_var.set(self.Days[0])
        self.yr_var.set(self.Years[0])
        
        self.reg_or_corp_var.set("author")
        
        ac = 1
        self.auth_count.configure(text = ac)
        
        self.ed_result.configure(state = 'disabled')
        self.confirm_b.configure(state = 'disabled')
        self.discard_b.configure(state = 'disabled')

    #---Final frame function------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
    def final(self):
        global references
        global sorted_ref
        self.i = 136
        count = 1
        elmnt = 0
        
        self.add_b.configure(state = 'normal')
        self.clear_b.configure(state = 'normal')
        
        sorted_ref = list(sorted(references))

        if len(sorted_ref) == 1:
            self.finalresult.insert(tk.END, "\t\t\t     REFERENCE\n\n")
        else:
            self.finalresult.insert(tk.END, "\t\t\t     REFERENCES\n\n")
        
        while(count <= len(references)):
            self.ref_count = ("{0}. {1}".format(count, sorted_ref[elmnt]))
            if len(self.ref_count) > 70: 
                self.indents = list(self.ref_count)
                self.indents.insert(70, "\n     ")
                while (self.i <= len(self.indents)):
                    if self.i % 68 == 0:
                        self.indents.insert(self.i, "\n     ")
                    self.i += 1
                self.chckindents = ''.join(self.indents)
                self.finalresult.insert(tk.END, self.chckindents + '\n\n')
            else:
                self.finalresult.insert(tk.END, self.ref_count + '\n\n')
            count += 1
            elmnt += 1
            
        self.finalresult.configure(state = 'disabled')

    #---add another function------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    def add_another(self):
        global ac
        
        self.ed_result.delete('1.0', END)
        self.ed_result.configure(state = 'disabled')
        self.tobeenabled = [self.author_f_ent, self.author_m_ent, self.author_l_ent, self.title_ent, self.url_ent, self.auth_rb, self.cg_rb, self.citate, self.mp, self.dp, self.yp, self.mr, self.dr, self.yr]
        for ena in self.tobeenabled:
            ena.configure(state = 'normal')
            
        self.clearedentry = [self.cg_ent, self.author_f_ent, self.author_m_ent, self.author_l_ent, self.title_ent, self.url_ent]
            
        for cle in self.clearedentry:
            cle.delete(0, END)
        
        self.mp_var.set(self.Months[0])
        self.dp_var.set(self.Days[0])
        self.yp_var.set(self.Years[0])
        self.mr_var.set(self.Months[0])
        self.dr_var.set(self.Days[0])
        self.yr_var.set(self.Years[0])
        
        self.reg_or_corp_var.set("author")
        
        ac = 1
        self.auth_count.configure(text = ac)
        self.add_b.configure(state = 'disabled')
        self.clear_b.configure(state = 'disabled')

    #---clear all function--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------      
    def clear_all(self):
        self.ask = askyesno("Confirm clear", "Clear all the reference list?")
        
        if self.ask == True:
            global ac
            global references
            global sorted_references
        
            self.ed_result.delete('1.0', END)
            self.finalresult.configure(state = 'normal')
            self.finalresult.delete('1.0', END)
            self.finalresult.configure(state = 'disabled')
            self.ed_result.configure(state = 'disabled')
            self.tobeenabled = [self.author_f_ent, self.author_m_ent, self.author_l_ent, self.title_ent, self.url_ent, self.auth_rb, self.cg_rb, self.citate, self.mp, self.dp, self.yp, self.mr, self.dr, self.yr]
            for ena in self.tobeenabled:
                ena.configure(state = 'normal')
            
            self.clearedentry = [self.cg_ent, self.author_f_ent, self.author_m_ent, self.author_l_ent, self.title_ent, self.url_ent]
            
            for cle in self.clearedentry:
                cle.delete(0, END)
        
            self.mp_var.set(self.Months[0])
            self.dp_var.set(self.Days[0])
            self.yp_var.set(self.Years[0])
            self.mr_var.set(self.Months[0])
            self.dr_var.set(self.Days[0])
            self.yr_var.set(self.Years[0])
        
            self.reg_or_corp_var.set("author")
        
            ac = 1
            self.auth_count.configure(text = ac)
            
            references.clear()
            sorted_ref.clear()
            
            self.add_b.configure(state = 'disabled')
            self.clear_b.configure(state = 'disabled')
        else:
            pass

    #---file saving-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------        
    def file_save(self):
        """Opens file explorer for file saving of references"""
        
        files = [('Text Document', '*.txt'),  
             ('Word Document', '*.doc')]
        f = asksaveasfile(mode='w', filetypes = files, defaultextension= files)
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        text2save = str(self.finalresult.get(1.0, END))
        f.write(text2save)
        f.close()
        
#Introduction / Main-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
root = tk.Tk()
root.title("APA web citation generator v1.0")
now = datetime.datetime.now()
root.geometry('590x305')
root.resizable(False,False)

a = Label(root, text="AMERICAN", font=('impact',30))
a.place(x = 10, y = 5)

ps = Label(root, text = "PSYCHOLOGICAL", font = ('impact', 19))
ps.place(x = 11, y = 50)

asso = Label(root, text = "ASSOCIATION", font = ('impact', 23))
asso.place(x = 10, y = 83)

web = Label(root, text = "Web Citation Generator", font = 37)
web.place(x = 10, y = 130)

welframe = LabelFrame(root, height = 274, width = 385)
welframe.place(x = 190, y = 15)

creator = Label(root, text = "Programming 2 Project\n\nJohn Paul G. Zoleta\nBachelor of Science in\nComputer Science")
creator.place(x = 28, y = 180)

Month = ["","January","February","March","April","May","June","July","August","September","October","November","December"]
samp = Label(welframe, text = "Sample result:").place(x = 8,y = 8)
sample = ("\t\t REFERENCE\n\n1. Author, F. M. (2020, January 13). Article      Title. Retrieved {1} {2}, {0}, from \n     https://url.com".format(now.year, Month[now.month], now.day))
sample_ent = Text(welframe,height = 5, width = 45)
sample_ent.place(x = 8, y = 30)
sample_ent.insert(tk.END, sample)
sample_ent.config(state = DISABLED)

note = Label(welframe, text = "◾ Simple APA 6th edition web citation generator\n◾ Manual inputs only\n◾ Supports file saving", justify=LEFT)
note.place(x = 8, y = 125)

generate = Button(welframe, text ="Generate now!", activebackground = 'gray', height = 4, width = 49, command = strt_now).place(x = 13, y = 185)
root.mainloop()

"""
APA 6th Edition Web Citation Generator
by: John Paul G. Zoleta (BSCS 1st Year)
"""
