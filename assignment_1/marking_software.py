import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk # import pillow library for images

Title_Font = ("Century Gothic", 15)
MARK_IV_Heading_Font = ("Century Gothic", 25)
Headline_Font = ("Century Gothic", 16)
imageMonash= "monash-university-malaysia_2.png"

def popMessage(msg):
    pop = tk.Tk()

    def quit():
        pop.destroy()
    
    pop.wm_title("pop up message")
    label = ttk.Label(pop,text=msg, font = ("Century Gothic", 10))
    label.grid(row=0, column=0)
    button1= ttk.Button(pop, text="Okay", command = quit)
    button1.grid(row=1,column=0)
    pop.mainloop()

class Mark(tk.Tk):

    def __init__(self,*args, **kwargs):  # Runs everytime the class mark is called
        
        tk.Tk.__init__(self, *args, **kwargs)
        #tk.Tk.iconbitmap(self, default = "markiv.ico")
        tk.Tk.wm_title(self, "Marking Software")
        
        container = tk.Frame(self) # Creating a window
        container.pack(side="top", fill="both", expand=True) # expand fills entire space of pack
        container.grid_rowconfigure(0, weight = 1)      # first arg = minimum size
        container.grid_columnconfigure(0, weight = 1)      # first arg = minimum size

        self.frames = {} # creating a dictionary for frames NOT YET IMPLEMENTED
        # creating a tuple of  frames with their own geometry
        for F,geometry in zip( (HomePage, StudentPage, MarkingPage), ('475x400','500x200','500x200')):
            page_name = F.__name__
            frame = F(parent=container, controller=self)            
            self.frames[page_name] = (frame,geometry)
            frame.config(bg="white")
            # assign grid to frame
            # sticky == allignment and strech
            #  sticky to north south east west
            #  means everything is strecthced to the size of frame
            frame.grid(row=0, column = 0, sticky="nsew")
        #initialise first page to show
        self.show_frame("HomePage")
    
    # Shows only the frame chosen by user
    def show_frame(self, page_name):
        frame,geometry = self.frames[page_name]
        self.update_idletasks()
        self.geometry(geometry)
        frame.tkraise()

# Class that opens the the first frame
# Inherits all parent classes method and attributes
# Parent class in this case is Mark
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        ########################################
        #####        CODE GOES HERE       ######
        ########################################

        # create an object and assign to label
        # basically an initializer for a label
        label1 = tk.Label(self, text = "MARK IV",bg = "white",fg = "black", font = MARK_IV_Heading_Font)
        # Calling the label method to output to start frame
        label1.grid(column =0,row=8, columnspan=5,sticky = "n")
        label2 = tk.Label(self, text = "Monash IT Deparment Marking Software",bg = "white",fg = "black", font = Headline_Font)
        label2.grid(column=0,row=9, columnspan=5, sticky="n")
        label3 =  tk.Label(self, text = "", bg="white")
        label3.grid(column=0, row=10)
        label4 =  tk.Label(self, text = "", bg="white")
        label4.grid(column=0, row=14)
        # label for unit names and student id
        unit_name =  tk.Label(self, text = "Unit Name: ",bg = "white",fg = "black", font = Title_Font)
        students_no =  tk.Label(self, text = "Number of Students: " ,bg = "white",fg = "black", font =Title_Font)
        entry_1 = tk.Entry(self) # text box to receive input from user
        
        unit_name.grid(row = 11, column = 0,sticky = "n")
        students_no.grid(row = 12, column = 0, sticky = "n")
        entry_1.grid(row = 11, column = 0, sticky="e")
        
        radio_1 = tk.Radiobutton(self, text="4 students", variable=1, value=4,fg = "black",bg="white" , font = Title_Font )
        radio_2 = tk.Radiobutton(self, text="5 students", variable=1, value=5,fg = "black",bg="white" , font = Title_Font)
        radio_1.grid(row=12,column=0, sticky="e")
        radio_2.grid(row=13,column=0, sticky="e")
        
        ttk.Style().configure('white/black.TButton', foreground='Black', background='white')
        # moves to student page by calling frame PageOne
        button1 = ttk.Button(self, text = "SAVE RECORDS", style = 'white/black.TButton', 
                            command =lambda: (controller.show_frame("StudentPage"), popMessage("Added the record!"))) # moves to student page by calling frame PageOne
        button1.grid(row=15,column=0, sticky="n")


        button2 = ttk.Button(self, text = "EXIT", style = 'white/black.TButton')
        button2.grid(row=15,column=0, sticky="ne")
    
        # creating a canvas to insert an image        
        self.original = Image.open('monash-university-malaysia.png')
        self.image = ImageTk.PhotoImage(self.original)
        self.display = tk.Canvas(self, height = 130,width = 450,bd=-1, highlightthickness=1) #resizing canvas to img size
        self.display.create_image(0, 0, image=self.image, anchor="n", tags="img") 
        self.display.grid(row=1 ,sticky="nwes")
        self.grid(row=0,column=1)
        self.bind("<Configure>", self.resize)

    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize((450,160),Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("img")
        self.display.create_image(0, 0, image=self.image, anchor="nw", tags="IMG")


class StudentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        ########################################
        #####        CODE GOES HERE       ######
        ########################################

        
        # create an object and assign to label
        # basically an initializer for a label
        label = tk.Label(self, text= "Student Information Page",font=MARK_IV_Heading_Font,bg="white")
        # Calling the label method to output to first page
        label.pack(pady=10, padx=10)
    
        nextButton = ttk.Button(self, text = "Go to marking page",
                            command = lambda: controller.show_frame("MarkingPage")) # moves to page one by calling fframe StartPage
        nextButton.pack()



class MarkingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        ########################################
        #####        CODE GOES HERE       ######
        ########################################

        
        # create an object and assign to label
        # basically an initializer for a label
        label = tk.Label(self, text= "Marks allocation page",font=MARK_IV_Heading_Font,bg="white")
        # Calling the label method to output to first page
        label.pack(pady=10, padx=10)
        
        backButton = ttk.Button(self, text = "Back to student page",
                            command = lambda: controller.show_frame("StudentPage")) # moves to page one by calling fframe StartPage
        backButton.pack()



markingSoftware = Mark()
markingSoftware.mainloop()
