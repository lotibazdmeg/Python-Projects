from tkinter import *
from tkinter import font

screen = Tk()
screen.title('Unit Converter')
screen.geometry("600x600")
font_welcome_text = font.Font(screen, family='Helvetica', size=30)
text_font = font.Font(screen, family='Helvetica', size=15)


def validate_input(new_value, meter_entry):
    if len(new_value) > 8:
        return False
    
    try:
        float(new_value)
    except ValueError:
        return False

    return True


def main():
    global meter_entry
    global mm_box
    global cm_box
    global dm_box
    global km_box
    global inch_box
    global foot_box
    global yard_box
    global mile_box

    welcome_text = Label(screen, text="Length Converter", font=font_welcome_text)
    welcome_text.place(relx=0.515, rely=0.1, anchor="center")
    enter_text = Label(screen, text="Enter the length in meters:", font=text_font)
    enter_text.place(relx=0.30, rely=0.25)
    meter_entry = Entry(screen, validate="key", validatecommand=(screen.register(validate_input), "%P"), font=text_font, width=18) 
    meter_entry.bind("<Return>", meter_button_click)
    meter_entry.place(relx=0.3256, rely=0.315)
    mm_box = Label(screen, text="", font=text_font, relief="solid", borderwidth=0)
    cm_box = Label(screen, text="", font=text_font, relief="solid", borderwidth=0)
    dm_box = Label(screen, text="", font=text_font, relief="solid", borderwidth=0)
    km_box = Label(screen, text="", font=text_font, relief="solid", borderwidth=0)
    inch_box = Label(screen, text="", font=text_font, relief="solid", borderwidth=0)
    foot_box = Label(screen, text="", font=text_font, relief="solid", borderwidth=0)
    yard_box = Label(screen, text="", font=text_font, relief="solid", borderwidth=0)
    mile_box = Label(screen, text="", font=text_font, relief="solid", borderwidth=0)
    mm_box.place(relx=0.1, rely=0.5)
    cm_box.place(relx=0.1, rely=0.6)
    dm_box.place(relx=0.1, rely=0.7)
    km_box.place(relx=0.1, rely=0.8)
    inch_box.place(relx=0.65, rely=0.5)
    foot_box.place(relx=0.65, rely=0.6)
    yard_box.place(relx=0.65, rely=0.7)
    mile_box.place(relx=0.65, rely=0.8)


def meter_button_click(event):
    meter_value = meter_entry.get()
    if validate_input(meter_value, meter_entry):
        mm = float(meter_value) * 1000
        cm = float(meter_value) * 100
        dm = float(meter_value) * 10
        km = float(meter_value) / 1000
        inch = float(meter_value) * 39.3701
        foot = float(meter_value) * 3.28084
        yard = float(meter_value) * 1.09361
        mile = float(meter_value) / 1609.344

        mm_box.config(text = f"{mm:.4f} mm")
        cm_box.config(text = f"{cm:.4f} cm")
        dm_box.config(text = f"{dm:.4f} dm")
        km_box.config(text = f"{km:.4f} km")
        inch_box.config(text = f"{inch:.4f} inch")
        foot_box.config(text = f"{foot:.4f} foot")
        yard_box.config(text = f"{yard:.4f} yard")
        mile_box.config(text = f"{mile:.4f} mile")
    else:
        mm_box.config(text="")
        cm_box.config(text="")
        dm_box.config(text="")
        km_box.config(text="")
        inch_box.config(text="")
        foot_box.config(text="")
        yard_box.config(text="")
        mile_box.config(text="")


main()  
screen.mainloop()