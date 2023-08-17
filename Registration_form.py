from tkinter import *
import PIL
from PIL import Image, ImageTk

import mysql.connector as mc


#Function
def Database():
    try:
        mydb = mc.connect(
            host = "localhost",
            user = "root",
            passwd = "tiger",
            database = "user_info_tt"
        )
        
        mycursor = mydb.cursor()
        # # Add a column called "serial_number" to the table
        # mycursor.execute("ALTER TABLE mytable ADD COLUMN serial_number INT")

        # # Update the serial_number column with a unique number for each record
        # mycursor.execute("SET @count = 0")
        # mycursor.execute("UPDATE mytable SET serial_number = @count:= @count + 1")
        
        # # Create the table
        # mycursor.execute("CREATE TABLE user (id INT PRIMARY KEY, name VARCHAR(255), age INT, address VARCHAR(255))")
        
        if food_services_val.get() == 1:
            food_services_value = 'Yes'
        else:
            food_services_value = 'No'
        # mycursor.execute("CREATE TABLE cust (name VARCHAR(255), phone VARCHAR(255), gender VARCHAR(255), emergency_contact VARCHAR(255), payment VARCHAR(255), food_service VARCHAR(255));")
        sql = "INSERT INTO user (name, phone, gender, emergency_contact, payment_mode, food_service) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (nameval.get(), phoneval.get(), genderval.get(), emergency_val.get(), payment_val.get(), food_services_value)
        mycursor.execute(sql, val)
        
        mycursor.execute("SELECT * from user;")
        for x in mycursor:
            print(x) 

        print(mycursor.rowcount, "record inserted.")
        # mycursor.commit()
        mydb.commit()

        GetVal()
        
    except Exception as e:
        print(e)



def GetVal():
    # Database()              # Records storing in database
    print("Name= ", nameval.get())
    print("Phone= ", phoneval.get())
    print("Gender= ", genderval.get())
    print("Emergency Contact= ", emergency_val.get())
    print("Payment Mode= ", payment_val.get())
    # if food_services_val.get() == 1:
    #     food_services_value = 'Yes'
    # else:
    #     food_services_value = 'No'
    print("Food Services= ", food_services_val.get())


    # with open("Records.txt","a") as f:
    #     f.write(f"\nName= {nameval.get()}\nPhone= {phoneval.get()}\nGender= {genderval.get()}\nEmergency Contact= {emergency_val.get()}\nPayment Mode= {payment_val.get()}\n")
    #     if food_services_val.get() == 1:
    #         f.write("Food Services= YES\n")
    #     else:
    #         f.write("Food Services= NO\n")
        
if __name__ == '__main__':
    root = Tk()

    root.geometry("600x400")
    root.minsize(500,350)
    root.maxsize(600,400)

    #Background Frame
    main_frame = Frame(root, width=600, height=400)
    main_frame.grid()

    # img_1 = Image.open("nature_2.png")
    # resize_image_1 = img_1.resize((600, 400)) 
    # photo_1 = ImageTk.PhotoImage(image=resize_image_1)
    # image_1 = Label(main_frame, image=photo_1)
    # image_1.grid()


    Label(main_frame, text="Welcome to Tours and Travels", pady=20, font=("comicsansms", 12, "bold")).grid(row=0, column=3)

    name = Label(main_frame, text="Name")
    phone = Label(main_frame, text="Phone")
    gender = Label(main_frame, text="Gender")
    emergency_contact = Label(main_frame, text="Emergency Contact")
    payment_mode = Label(main_frame, text="Payment Mode",)

    name.grid(row=1, column=2)
    phone.grid(row=2, column=2)
    gender.grid(row=3, column=2)
    emergency_contact.grid(row=4, column=2)
    payment_mode.grid(row=5, column=2)

    nameval = StringVar()
    phoneval = StringVar()
    genderval = StringVar()
    emergency_val = StringVar()
    payment_val = StringVar()
    food_services_val = IntVar()

    name_entry = Entry(main_frame, textvariable=nameval)
    phone_entry = Entry(main_frame, textvariable=phoneval)
    gender_entry = Entry(main_frame, textvariable=genderval)
    emergency_contact_entry = Entry(main_frame, textvariable=emergency_val)
    payment_mode_entry = Entry(main_frame, textvariable=payment_val)

    name_entry.grid(row=1,column=3)
    phone_entry.grid(row=2,column=3)
    gender_entry.grid(row=3,column=3)
    emergency_contact_entry.grid(row=4,column=3)
    payment_mode_entry.grid(row=5,column=3)

    #CheckBox
    food_services = Checkbutton(main_frame, text="Want to preorder your meals", variable=food_services_val)
    food_services.grid(row=6, column=3)

    #Button
    Button(main_frame, text="Submit", bg="red", fg="white", borderwidth=3, relief=SUNKEN, command=Database).grid(row=7, column=3)



    root.mainloop()