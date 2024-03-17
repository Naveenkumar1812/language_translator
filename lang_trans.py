#importing all file/modules
from tkinter import*
import tkinter
from tkinter import ttk
from tkinter import PhotoImage
from googletrans import Translator , LANGUAGES  

#creating page
root=Tk() 
root.geometry('1100x320')
root.resizable(0,0) 


#inserting bg picture
image_path=PhotoImage(file=r"C:\Users\NAVEEN KUMAR\Pictures\Saved Pictures\GT.png")
bg_image=tkinter.Label(root,image=image_path)
bg_image.pack()

#giving tittle
root.title('Language translator')
Label(root,text="LANGUAGE TRANSLATOR",fg='black', font="Arial 20 bold").pack()

#giving all req text(input)
Label(root,text ="Enter text",font='arial 14 bold',fg='blue',bg='white smoke').place(x=110,y=90)
Input_text=Entry(root,width=40)
Input_text.place(x=30,y=130)
Input_text.get()

#giving all req text(output)
Label(root,text ='output', font ='arial 14 bold',fg='blue',bg ='white smoke').place(x=760,y=90)
output_text=Text(root,font='arail 13',height=1,wrap=WORD,padx=5,pady=5,width=40)
output_text.place(x=600,y=150)

#importing languages from google
language= list(LANGUAGES.values())
dest_lang=ttk.Combobox(root,values=language,width=22)
dest_lang.place(x=130,y=180)
dest_lang.set('choose language')

#running the main function
def Translate():
    translator = Translator()
    translated = translator.translate(text=Input_text.get(), dest=dest_lang.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)

trans_btn=Button(root,text='Translate',font='arial 12 bold',pady=5,command=Translate,bg='orange',activebackground='green')
trans_btn.place(x=445,y=220)
    
root.mainloop()
