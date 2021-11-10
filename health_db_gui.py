import tkinter as tk
from tkinter import ttk 
from PIL import Image, ImageTk

from health_db_client import add_patient_to_sere
def create_output(name, id, blood_letter, rh_factor):
    out_string = 'Patient name: {}\n'.format(name)
    out_string += 'Blood type: {}{}\n'.format(blood_letter, rh_factor)
    out_string += "Donation Center: {}".format(center)
    answer = add_patient_to_server_name(name, id,
                               "{}{}".format(blood_letter, rh_factor))
    return out_string, answer

def design_window():

    def ok_button_cmd():
        # Get needed data form GUI
        name = name_data.get()
        id = id_data.get()
        blood_letter = blood_letter_data.get()
        rh_factor = rh_data.get()
        center = donation_center_data.get()

        # Call external function to do the work that can be tested
        outstring, answer = create_output(name, id, blood_letter, rh_factor)

        #update GUI
        print(out_string)
        output_string.configure(text=answer) #reference label you created and configure allows you to change parameters

        def cancel_button():
            root.destroy()

    root = tk.Tk()
    root.title("Health Database GUI")
    root.geometry("10x2")

    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0, columnspan=2, sitcky='w')

    ttk.Label(root, text="Name").grid(column=0, row=1, sticky='e')

    name_data = tk.StringVar()
    name_entry_box = ttk.Entry(root, width=40, textvariable=name_data)
    name_entry_box.grid(column=1, row=1, sticky='w', columnspan=2)



    ttk.Label(root, text="ID").grid(column=0, row=2)

    id_data = tk.StringVar()
    id_entry_box = ttk.Entry(root, width=10, textvariable=id_data)
    id_entry_box.grid(column=1, row=2)


    blood_letter_data = tk.StringVar()
    blood_letter_data.set('AB')
    blood2 = tk.StringVar() #different sets of radio buttons that dont interact with each other
    ttk.Radiobutton(root, text='A', variable=blood_letter_data,
                     value='A').grid(column=0, row=3, sticky=tk.W)
    ttk.Radiobutton(root, text='B', variable=blood_letter_data,
                     value='B').grid(column=0, row=4, sticky=tk.W)
    ttk.Radiobutton(root, text='O', variable=blood2,
                     value='O').grid(column=0, row=6, sticky=tk.W)
    ttk.Radiobutton(root, text='AB', variable=blood_letter_data,
                     value='AB').grid(column=0, row=5, sticky=tk.W)
   

    rh_data = tk.StringVar()
    rh_data.set('-') #initialize button with off value so if you dont touch it will give you negative
    rh_checkbox = ttk.Checkbutton(root, text="Rh Positive",
                                  variable=rh_data, onvalue='+',
                                  offvalue='-')
    rh_checkbox.grid(column=1, row=4)

    tk.Label(root, text="Nearest Donation CEnter").grid(column=2, row=0)

    combo_box = ttk.Combobox(root, textvariable=donation_center_data)
    combo_box['values'] = ("Durham", "Raleigh", "Cary")
    combo_box.state(["readonly"])
    combo_box.grid(column=3, row=1)

    output_string = ttk.Label(root)
    output_string.grid(column=0, row=10)

    ok_button = ttk.Button(root, text='Ok', command=ok_button_cmd)
    ok_button.grid(column=1, row=6)

    cancel_button = ttk.Button(root, text="cancel", command=cancel_cmd)
    cancel_button.grid(column=2, row=6)

    pil_image = Image.open("image/blank_pic.jpeg") #put URL
    tk_image = ImageTk.PhotoImage(pil_image)
    image_label = ttk.Label(root, image=tk_image)
    image_label.grid(column=0, row=7)


    root.mainloop()

if __name__ == "__main__":
    design_window()
