from tkinter import*
from tkinter import ttk,filedialog,messagebox
import os,shutil
class Sorting_App:
    def __init__(self,root):
        self.root=root
        self.root.title("Sorting Application")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        self.logo_icon=PhotoImage(file="C:\Extn. sorting app\Folder\logo222.png")
        title=Label(self.root,text="Files Sorting Application",padx=10,image=self.logo_icon,compound=LEFT, font=("impact",40),bg="#023548",fg="white",anchor="w").place(x=0,y=0,relwidth=1)
        
        #======section1===
        self.var_foldername=StringVar()
        lbl_select_folder=Label(self.root,text="Select Folder",font=("Arial",25,),bg="white").place(x=60,y=127)
        text_folder_name=Entry(self.root,textvariable=self.var_foldername,font=("Arial",25),state='readonly',bg="lightyellow").place(x=280,y=127,height=40,width=600)
        btn_browse=Button(self.root,command=self.browse_function,font=("Arial",15,"bold"),text="BROWSE",bg="#262626",fg="white",activebackground="#262626",cursor="hand2",activeforeground="white").place(x=930,y=125,height=40,width=180)
        hr=Label(self.root,bg="lightgray").place(x=50,y=190,height=2,width=1250)
        
        self.video_extensions=["Video Extensions",".mp4",".mkv"]
        self.audio_extensions=["Audio Extensions",".mp3",".amr",".wav",".m4a",".aiff",".mpeg"]
        self.image_extensions=["Image Extensions",".jpg",".png",".jpeg",".gif"]
        self.doc_extensions=["Document Extensions",".doc",".xlsx",".xls",".pdf",".zip",".rar",".pages",".docx",".csv",".pptx",".txt"]
        
        self.folders={
                'Videos':self.video_extensions,
                'Audios':self.audio_extensions,
                'Images': self.image_extensions,
                'Documents':self.doc_extensions,
            }

        lbl_support_ext=Label(self.root,text="Various Supported Extensions",font=("times new roman",25,),bg="white").place(x=60,y=200)
        self.image_box=ttk.Combobox(self.root,values=self.image_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.image_box.place(x=70,y=270,width=250,height=35)
        self.image_box.current(0)

        self.video_box=ttk.Combobox(self.root,values=self.video_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.video_box.place(x=400,y=270,width=250,height=35)
        self.video_box.current(0)

        self.audio_box=ttk.Combobox(self.root,values=self.audio_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.audio_box.place(x=730,y=270,width=250,height=35)
        self.audio_box.current(0)

        self.doc_box=ttk.Combobox(self.root,values=self.doc_extensions,font=("times new roman",15),state='readonly',justify=CENTER)
        self.doc_box.place(x=1060,y=270,width=250,height=35)
        self.doc_box.current(0)


        self.image_icon=PhotoImage(file="C:\Extn. sorting app\Folder\image.png")
        self.audio_icon=PhotoImage(file="C:\Extn. sorting app\Folder\Audio1.png")
        self.video_icon=PhotoImage(file="C:\Extn. sorting app\Folder\Video.png")
        self.document_icon=PhotoImage(file="C:\Extn. sorting app\Folder\documents.png")
        self.other_icon=PhotoImage(file="C:\Extn. sorting app\Folder\others.png")

        Frame1=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Frame1.place(x=60,y=320,width=1250,height=300)
        self.lb1_total_files=Label(Frame1,text="Total Files",font=("Arial",20),bg="white")
        self.lb1_total_files.place(x=10,y=10)

        self.lb1_total_image=Label(Frame1,bd=2,relief=RAISED,image=self.image_icon,compound=CENTER,font=("Arial",20,"bold"),bg="#0875B7",fg="white")
        self.lb1_total_image.place(x=20,y=60,width=230,height=200)

        self.lb1_total_audio=Label(Frame1,bd=2,relief=RAISED,image=self.audio_icon,compound=CENTER,font=("Arial",20,"bold"),bg="#008EA4",fg="white")
        self.lb1_total_audio.place(x=260,y=60,width=230,height=200)

        self.lb1_total_video=Label(Frame1,bd=2,relief=RAISED,image=self.video_icon,compound=CENTER,font=("Arial",20,"bold"),bg="#0875B7",fg="white")
        self.lb1_total_video.place(x=500,y=60,width=230,height=200)

        self.lb1_total_document=Label(Frame1,bd=2,relief=RAISED,image=self.document_icon,compound=CENTER,font=("Arial",20,"bold"),bg="#008EA4",fg="white")
        self.lb1_total_document.place(x=740,y=60,width=230,height=200)

        self.lb1_total_other=Label(Frame1,bd=2,relief=RAISED,image=self.other_icon,compound=CENTER,font=("Arial",20,"bold"),bg="gray",fg="white")
        self.lb1_total_other.place(x=980,y=60,width=230,height=200)


        lbl_status=Label(self.root,text="STATUS",font=("times new roman",20,),bg="white").place(x=60,y=635)
        self.lbl_st_total=Label(self.root,text="",font=("times new roman",18,),bg="white",fg="green")
        self.lbl_st_total.place(x=300,y=638)
        
        self.lbl_st_moved=Label(self.root,text="",font=("times new roman",18,),bg="white",fg="blue")
        self.lbl_st_moved.place(x=500,y=638)
        
        self.lbl_st_left=Label(self.root,text="",font=("times new roman",18,),bg="white",fg="orange")
        self.lbl_st_left.place(x=700,y=638)

        #======Buttons======
        self.btn_clear=Button(self.root,font=("Arial",15,"bold"),text="CLEAR",command=self.clear,bg="#607d8b",fg="white",activebackground="#607d8b",cursor="hand2",activeforeground="white")
        self.btn_clear.place(x=880,y=635,height=40,width=180)
        self.btn_start=Button(self.root,state=DISABLED,command=self.start_function,font=("Arial",15,"bold"),text="START",bg="#ff5722",fg="white",activebackground="#ff5722",cursor="hand2",activeforeground="white")
        self.btn_start.place(x=1090,y=635,height=40,width=180)

    def Total_count(self):
        images=0
        audios=0
        videos=0
        documents=0
        others=0
        self.count=0
        cmbine_list=[]
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:
                self.count+=1
                ext="."+i.split(".")[-1]
                for folder_name in self.folders.items():
                    #print(folder_name)
                    for x in folder_name[1]:
                        cmbine_list.append(x)
                    if ext.lower() in folder_name[1] and folder_name[0]=="Images":
                         images+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="Audios":
                        audios+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="Videos":
                        videos+=1
                    if ext.lower() in folder_name[1] and folder_name[0]=="Documents":
                        documents+=1
            
        for i in self.all_files:
            if os.path.isfile(os.path.join(self.directry,i))==True:     
                ext="."+i.split(".")[-1]
                if ext.lower() not in cmbine_list:
                    others+=1
                 

        self.lb1_total_image.config(text="Total Images\n"+str(images),fg="yellow")
        self.lb1_total_video.config(text="Total Videos\n"+str(videos),fg="black")
        self.lb1_total_audio.config(text="Total Audios\n"+str(audios),fg="green")
        self.lb1_total_document.config(text="Total Documents\n"+str(documents),fg="black") 
        self.lb1_total_other.config(text="Other Files\n"+str(others),fg="#FF272A")
        self.lb1_total_files.config(text="Total Files: "+str(self.count))

    def browse_function(self):
        op=filedialog.askdirectory(title="SELECT FOLDER FOR SORTING")
        if op!=None:
            #print(op)
            self.var_foldername.set(str(op))
            self.directry=self.var_foldername.get()
            self.other_name="others"
            self.rename_folder()
            self.all_files=os.listdir(self.directry)
            length=len(self.all_files)
            count=1
            self.Total_count()
            self.btn_start.config(state=NORMAL)
            #print(self.all_files)
            
    def start_function(self):
        if self.var_foldername.get()!="":
            self.btn_clear.config(state=NORMAL)
            c=0
            for i in self.all_files:
                if os.path.isfile(os.path.join(self.directry,i))==True:
                    c+=1
                    self.create_move(i.split(".")[-1],i)
                    self.lbl_st_total.config(text="TOTAL: "+str(self.count))
                    self.lbl_st_moved.config(text="MOVED: "+str(c))
                    self.lbl_st_left.config(text="LEFT: "+str(self.count-c))

                    self.lbl_st_total.update()
                    self.lbl_st_moved.update()
                    self.lbl_st_left.update()
                    
            messagebox.showinfo("Success","All Files have moved Successfully")
            self.btn_start.config(state=NORMAL)
            self.btn_start.config(state=DISABLED)
        else:
            messagebox.showinfo("Error","Please select Folder")    

    def clear(self):
        self.btn_start.config(state=NORMAL)
        self.var_foldername.set("")
        self.lbl_st_total.config(text="")
        self.lbl_st_moved.config(text="")
        self.lbl_st_left.config(text="")
        self.lb1_total_image.config(text="")
        self.lb1_total_video.config(text="")
        self.lb1_total_audio.config(text="")
        self.lb1_total_document.config(text="") 
        self.lb1_total_other.config(text="")
        self.lb1_total_files.config(text="Total Files")

    def rename_folder(self):
        for folder in os.listdir(self.directry):
            if os.path.isdir(os.path.join(self.directry,folder))==True:
                os.rename(os.path.join(self.directry,folder),os.path.join(self.directry,folder.lower()))

    def create_move(self,ext,file_name):
        find=False
        for folder_name in self.folders:
            if '.'+ext in self.folders[folder_name]:
                if folder_name not in os.listdir(self.directry):
                    os.mkdir(os.path.join(self.directry,folder_name))
                shutil.move(os.path.join(self.directry,file_name),os.path.join(self.directry,folder_name))
                find=True
                break
        if find!=True:
            if self.other_name not in os.listdir(self.directry):
                os.mkdir(os.path.join(self.directry,self.other_name))
            shutil.move(os.path.join(self.directry,file_name),os.path.join(self.directry,self.other_name))


root=Tk()
obj=Sorting_App(root)
root.mainloop()
