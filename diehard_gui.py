import time
import sys
import os

if sys.version_info<(3,0,0):
  sys.stderr.write("You need python 3.0 or later to run this script\n")
  exit(1)



#3.X import statements
from tkinter import *
from tkinter import filedialog as fd

filename=""
class gui:

    def d1(self):
            from tkinter.filedialog import askopenfilename
            Tk().withdraw()
            self.filename=askopenfilename()
            print (self.filename)
            self.e.insert(0,self.filename)


    def d2(self):
            
            self.filename1= fd.asksaveasfilename(initialdir = "/home/ubuntu/Desktop",title = "Select file")
            print (self.filename1)
            self.e2.insert(0,self.filename1)
    def d3(self):
            global var
            selc=self.w.get(ACTIVE)
            print (selc)
            buff="Test name = "
            buff+=selc
            buff+="\n"
            self.log.insert(END,buff)
            
            
            testname=selc
            source=self.e.get()
            dest=self.e2.get()
            print (source)
            print (dest)
            
            #print testname
            if testname == "    All Test    ":
                testno=210
            if testname == "diehard_birthdays":
                testno=0
            if testname == "diehard_operm5":
                testno=1
            if testname == "diehard_rank_32x32":
                testno=2
            if testname == "diehard_rank_6x8":
                testno=3
            if testname == "diehard_bitstream":
                testno=4
            if testname == "diehard_opso":
                testno=5
            if testname == "diehard_oqso":
                testno=6
            if testname == "diehard_dna":
                testno=7
            if testname == "diehard_count_1s_str":
                testno=8
            if testname == "diehard_count_1s_byt":
                testno=9
            if testname == "diehard_parking_lot":
                testno=10
            if testname == "diehard_2dsphere":
                testno=11
            if testname == "diehard_3dsphere":
                testno=12
            if testname == "diehard_squeeze":
                testno=13
            if testname == "diehard_sums":
                testno=14
            if testname == "diehard_runs":
                testno=15
            if testname == "diehard_craps":
                testno=16
            if testname == "marsaglia_tsang_gcd":
                testno=17
            if testname == "sts_monobit":
                testno=100
            if testname == "sts_runs":
                testno=101
            if testname == "sts_serial":
                testno=102
            if testname == "rgb_minimum_distance":
                testno=201
            if testname == "rgb_permutations":
                testno=202
            if testname == "rgb_lagged_sum":
                testno=203
            if testname == "rgb_kstest_test":
                testno=204
            if testname == "dab_bytedistrib":
                testno=205
            if testname == "dab_dct":
                testno=206
            if testname == "dab_filltree":
                testno=207
            if testname == "dab_filltree2":
                testno=208
            if testname == "dab_monobit2":
                testno=209
            
            print (testno)
            buff="Test no = "
            buff+=str(testno)
            buff+="\n"
            self.log.insert(END,buff)
            mode= self.v.get()
            wmode=""
            if(mode==1):
                wmode="w"
            elif(mode==2):
                wmode="a"
            f=open(dest,wmode)
            u=testno
            
            print (" ")
            print ("")
            if u==210:
                    
                str1='dieharder -a '
    
                print ("Full test" ,u)
                f.write(str(u))
                f.write("\n\n")
                str1+='-g 201 -f '
                str1+=source
                print (str1)
                #os.system(str1)
                str2= os.popen(str1).read()
                f.write(str2)
                f.write("\n\n")
                print (str2)
                #time.sleep(10)
                print (" ")
                print (" ")
                print ("``````````````````````````````````````````````````````````")
            else:
                str1='dieharder -d '
                print ("d = " ,u)
                f.write(str(u))
                f.write("\n\n")
                str1+=str(u)
                str1+=' -g 201 -f '
                str1+=source
                print (str1)
                #os.system(str1)
                str2= os.popen(str1).read()
                f.write(str2)
                f.write("\n\n")
                print (str2)
                #timee.sleep(10)
                print (" ")
                print (" ")
                print ("``````````````````````````````````````````````````````````")
            buff=selc
            buff+="  test finished \n"
            self.log.insert(END,buff)
            buff="--------------------------------\n"
            self.log.insert(END,buff)
            
                
            
              
            
    def __init__(self, master):
        self.master = master
        master.configure(background='ivory2')
        master.wm_title("DIEHARD")
        Label(master, text="""DIEHARD TEST SUITE""",fg="red",bg='ivory2',justify = LEFT,padx = 20,font = "courier 16 bold italic").pack()
        #Label(master, text="""""",justify = LEFT,padx = 20,bg='bisque',font = "courier 7 bold italic").pack()
        Label(master, text="""Information Security Research Group""",bg='ivory2',fg="blue",justify = CENTER,padx = 20,font = "courier 16 bold italic").pack()
        Label(master, text="""School of EEE - SASTRA University""",bg='ivory2',fg="blue",justify = CENTER,padx = 20,font = "courier 16 bold italic").pack()
        width=850
        height=660
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        master.geometry('%dx%d+%d+%d' % (width, height, x, y))
        
        
        

        global var
        var = StringVar(master)
        var.set("    All Test    ")
        OPTIONS = [
        "    All Test    ",
        "diehard_birthdays",
        "diehard_operm5",
        "diehard_rank_32x32",
        "diehard_rank_6x8",
        "diehard_bitstream",
        "diehard_opso",
        "diehard_oqso",
        "diehard_dna",
        "diehard_count_1s_str",
        "diehard_count_1s_byt",
        "diehard_parking_lot",
        "diehard_2dsphere",
        "diehard_3dsphere",
        "diehard_squeeze",
        "diehard_sums",
        "diehard_runs",
        "diehard_craps",
        "marsaglia_tsang_gcd",
        "sts_monobit",
        "sts_runs",
        "sts_serial",
        "rgb_minimum_distance",
        "rgb_permutations",
        "rgb_lagged_sum",
        "rgb_kstest_test",
        "dab_bytedistrib",
        "dab_dct",
        "dab_filltree",
        "dab_filltree2",
        "dab_monobit2",
        
        
        
        ]

        self.l=Label(master,text="Select the test",bg='ivory2',fg="black",font = "courier 15 bold italic")
        self.l.pack()
        self.l.place(x=120,y=130)
        
        frame = Frame(master)


        xscrollbar = Scrollbar(frame, orient=HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=E+W)

        yscrollbar = Scrollbar(frame)
        yscrollbar.grid(row=0, column=1, sticky=N+S)
    

        
        self.w =Listbox(frame,width=30,height=8,xscrollcommand=xscrollbar.set,
                yscrollcommand=yscrollbar.set,font=('courier',12),selectmode=EXTENDED)
        self.w.grid(row=0, column=0, sticky=N+S+E+W)
        #self.w.select_set(0)
        
        
        for i in range(31):
            self.w.insert(0, OPTIONS[30-i])
        
        xscrollbar.config(command=self.w.xview)
        
        yscrollbar.config(command=self.w.yview)

        frame.pack()
        frame.place(x=50,y=180)
        
        self.l1=Label(master,text="Select Source File Location",bg='ivory2',fg="black",font = "courier 15 bold italic")
        self.l1.pack()
        self.l1.place(x=50,y=370)
        self.e = Entry(master, width=35)
        self.e.pack()
        self.e.place(x=70,y=420)
        self.b1=Button(master,text="Browse",command=self.d1)
        self.b1.pack()
        self.b1.place(x=172,y=460)



        self.l2=Label(master,text="Select Destination Folder",bg='ivory2',fg="black",font = "courier 15 bold italic")
        self.l2.pack()
        self.l2.place(x=50,y=510)
        self.e2 = Entry(master, width=35)
        self.e2.pack()
        self.e2.place(x=50,y=560)
        self.b2=Button(master,text="Browse",command=self.d2)
        self.b2.pack()
        self.b2.place(x=172,y=600)

        
    
        frame1 = Frame(master)


        xscrollbar1 = Scrollbar(frame1, orient=HORIZONTAL)
        xscrollbar1.grid(row=1, column=0, sticky=E+W)

        yscrollbar1 = Scrollbar(frame1)
        yscrollbar1.grid(row=0, column=1, sticky=N+S)
    
        self.log = Text (frame1, width=55, height=20,bg='grey100',xscrollcommand=xscrollbar1.set,
                yscrollcommand=yscrollbar1.set ,takefocus=0)
        
        self.log.grid(row=0, column=0, sticky=N+S+E+W)
        #self.w.select_set(0)
        
        
        
        xscrollbar1.config(command=self.log.xview)
        
        yscrollbar1.config(command=self.log.yview)

        frame1.pack()
        frame1.place(x=400,y=180)
        
        self.l3=Label(master,text="Modes of Operation",bg='ivory2',fg="black",font = "courier 15 bold italic")
        self.l3.pack()
        self.l3.place(x=500,y=510)
        self.v=IntVar()
        self.r1=Radiobutton(master,text="Erase/Write",font=('courier',12,'italic'),bg='ivory2',variable=self.v,value=1)
        self.r1.pack()
        self.r1.place(x=450,y=550)
        self.r2=Radiobutton(master,text="Append",font=('courier',12,'italic'),bg='ivory2',variable=self.v,value=2)
        self.r2.pack()
        self.r2.place(x=620,y=550)
        self.b3=Button(master,text="Start Test",bg="ivory2",command=self.d3)
        self.b3.pack()
        self.b3.place(x=690,y=600)



        
root = Tk()
g=gui(root)
root.mainloop()
