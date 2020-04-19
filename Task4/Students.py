import tkinter as tk
# import tkMessageBox
import smtplib
from email.mime.text import MIMEText
import json
HEIGHT = 500
WIDTH = 600
recipients=[]
dbp=[]
dbm=[]
dap=[]
dam=[]
dabp=[]
dabm=[]
dop=[]
dom=[]
with open("students.json", "r") as read_file:
        data = json.load(read_file)
def get_names(entry):
    for i in range(len(data)):
        if data[i]['u'] != "":
            if data[i]['b'] == 'B+':
                dbp.append(data[i]['n'])
            if data[i]['b'] == 'B-':
                dbm.append(data[i]['n'])
            if data[i]['b'] == 'A+':
                dap.append(data[i]['n'])
            if data[i]['b'] == 'A-':
                dam.append(data[i]['n'])
            if data[i]['b'] == 'AB+':
                dabp.append(data[i]['n'])
            if data[i]['b'] == 'AB-':
                dabm.append(data[i]['n'])
            if data[i]['b'] == 'O+':
                dop.append(data[i]['n'])
            if data[i]['b'] == 'O-':
                dom.append(data[i]['n'])
    if entry == 'B+':
        recipients = dbp+dbm+dop
    elif entry == 'B-':
        recipients = dbm+dom
    elif entry == 'A+':
        recipients = dap+dam+dop
    elif entry == 'A-':
        recipients = dam+dom
    elif entry=='AB+':
        recipients = dabp+dabm+dap+dbp+dop+dam+dbm+dom
    elif entry=='AB-':
        recipients = dabm+dam+dom+dbm
    elif entry=='O+':
        recipients = dop+dom
    elif entry=='O-':
        recipients = dom
    else:
        p = tk.Tk()
        p.wm_title("Please enter a valid blood type")
        label = tk.Label(p, text="Enter a valid blood type")
        label.place(relx=0.1, rely=0.1, relheight=0.2,relwidth=0.8)
        B = tk.Button(p, text="Okay", command = p.destroy)
        B.place(relx=0.4, rely=0.3, relwidth =0.2, relheight = 0.1)
        popup.mainloop()
    print(recipients)    
def send_mails(entry):
    for i in range(len(data)):
        if data[i]['u'] != "":
            if data[i]['b'] == 'B+':
                dbp.append(data[i]['u']+"@iitk.ac.in")
            if data[i]['b'] == 'B-':
                dbm.append(data[i]['u']+"@iitk.ac.in")
            if data[i]['b'] == 'A+':
                dap.append(data[i]['u']+"@iitk.ac.in")
            if data[i]['b'] == 'A-':
                dam.append(data[i]['u']+"@iitk.ac.in")
            if data[i]['b'] == 'AB+':
                dabp.append(data[i]['u']+"@iitk.ac.in")
            if data[i]['b'] == 'AB-':
                dabm.append(data[i]['u']+"@iitk.ac.in")
            if data[i]['b'] == 'O+':
                dop.append(data[i]['u']+"@iitk.ac.in")
            if data[i]['b'] == 'O-':
                dom.append(data[i]['u']+"@iitk.ac.in")
    if entry == 'B+':
        recipients = dbp+dbm+dop
    elif entry == 'B-':
        recipients = dbm+dom
    elif entry == 'A+':
        recipients = dap+dam+dop
    elif entry == 'A-':
        recipients = dam+dom
    elif entry=='AB+':
        recipients = dabp+dabm+dap+dbp+dop+dam+dbm+dom
    elif entry=='AB-':
        recipients = dabm+dam+dom+dbm
    elif entry=='O+':
        recipients = dop+dom
    elif entry=='O-':
        recipients = dom
    else:
        popup = tk.Tk()
        popup.wm_title("Please enter a valid blood type")
        label = tk.Label(popup, text="Enter a valid blood type")
        label.place(relx=0.1, rely=0.1, relheight=0.2,relwidth=0.8)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy)
        B1.place(relx=0.4, rely=0.3, relwidth =0.2, relheight = 0.1)
        popup.mainloop()
    # print(recipients)
    username = ""
    password = ""
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(username, password)


    subject = "Blood donation:Emergency"
    body = "Dear Students, Mukesh is in dire need of blood transfusion and your blood group makes you an eligible donor. Please contact Dr. Mohan at the health centre if you wish to donate."
    msg = 'Subject: {subject}\n\n{body}'

    s.sendmail(username, recipients, msg)
    s.quit()



root = tk.Tk()
root.wm_title("Blood Donation Database")
canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bd=5, bg='#F4B89B')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

label = tk.Label(frame, font=20, text="Enter Blood Type:", bd=2)
label.place(relheight=1, relwidth=0.4)

entry = tk.Entry(frame, font=20)
entry.place(relx=0.45, relheight=1, relwidth=0.55)

button = tk.Button(root, text="Get Names", font=20, command=lambda: get_names(entry.get()))
button.place(relx=0.40,rely=0.25, relheight=0.08, relwidth=0.20)

button2 = tk.Button(root, text="Send Mails", font=20, command=lambda: send_mails(entry.get()))
button2.place(relx=0.38, rely=0.35, relheight=0.08, relwidth=0.24)
root.mainloop()
