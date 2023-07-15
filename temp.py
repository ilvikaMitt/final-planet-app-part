from tkinter import*
from PIL import ImageTk,Image
from tkinter import ttk
root=Tk()

root.title("arrow")
root.geometry("1000x1200")
root.configure(background="green")

earth_img=ImageTk.PhotoImage(Image.open("earth.jpg"))
venus_img=ImageTk.PhotoImage(Image.open("venus.jpg"))
mercury_img=ImageTk.PhotoImage(Image.open("mercury.jpg"))

label_p=Label(root,text="planet")
label_p.place(relx=0.3,rely=0.1,anchor=CENTER)

planet=["Mercury","Venus","Earth"]
slected_val=StringVar()
planet_dd=ttk.Combobox(root,values=planet,textvariable=slected_val)
planet_dd.place(relx=0.5,rely=0.1,anchor=CENTER)

planet_name=Label(root)
planet_name.place(relx=0.5,rely=0.4,anchor=CENTER)

planet_img=Label(root)
planet_img.place(relx=0.5,rely=0.6,anchor=CENTER)

planet_info=Label(root)
planet_info.place(relx=0.5,rely=0.9,anchor=CENTER)

def info1():
    planet1=slected_val.get()
    if planet1=="Mercury":
        planet_name["text"]="Mercury"
        planet_img["image"]=mercury_img
        planet_info["text"]="Gravity and radius - Gravity : 3.7 m/s² \n Radius - 2,439.7 km \n Information - Mercury is the smallest planet in our solar system. It's just a little bigger than Earth's moon"
        
    elif planet1=="Venus":
        planet_name["text"]="Venus"
        planet_img["image"]=venus_img
        planet_info["text"]="Gravity and radius - Gravity : 8.87 m/s² \n Radius : 6,051.8 km \n Information - Venus is the brightest object in the sky after the Sun and the Moon, and sometimes looks like a bright star in the morning or evening sky."
        
    elif planet1=="Earth":
        planet_name["text"]="Earth"
        planet_img["image"]=earth_img
        planet_info["text"]="Gravity and radius - Gravity : 9.807 m/s² \n Radius : 6,371 km \n Information - Earth is the only place in the known universe confirmed to host life and it's the only one known for sure to have liquid water on its surface."
             
        
        
    

info=Button(root,text="show planet info",command=info1)
info.place(relx=0.5,rely=0.2,anchor=CENTER)



root.mainloop()

