import tkinter as Tk
import sqlite3


conn = sqlite3.connect('FOC.db')

root = Tk.Tk()
root.title("FOC Project")
root.geometry('500x500')
#Tk.Label(root, text="Railway Reservation System",font=('Slab Serif',17),bg='Blue').place(x=60,y=60)

def input_query1():
    iq1=sqlite3.connect('FOC.db')
    iq1_cur=iq1.cursor()
    iq1_cur.execute("SELECT TRAIN.Train_Number, TRAIN.Train_Name FROM TRAIN JOIN BOOKED ON TRAIN.Train_Number = BOOKED.Train_Number JOIN PASSENGERS ON PASSENGERS.Ssn = BOOKED.Passenger_ssn WHERE PASSENGERS.Last_name = ? AND PASSENGERS.First_name = ?", (Last_name.get(), First_name.get()))
    records=iq1_cur.fetchall()
  
    print_records=''
    for record in records:
        print_records+=str(record[0] +" "+record[1]+"\n")
    iq1_label=Tk.Label(root,text=print_records)
    iq1_label.grid(row=15,column=0,columnspan=2)
    iq1.commit()
    iq1.close()
def input_query2():
    idate=Train_Date.get()
    print(idate)
    iq2=sqlite3.connect('FOC.db')

    iq2_cur=iq2.cursor()
    
    iq2_cur.execute(f'''SELECT p.First_name, p.Last_name, t.Train_Name, b.Ticket_Types, b.Status
FROM PASSENGERS p 
JOIN BOOKED b ON p.Ssn = b.Passenger_ssn 
JOIN TRAIN t ON t.Train_Number = b.Train_Number 
JOIN TRAIN_STATUS ts ON t.Train_Name = ts.Train_Name 
WHERE ts.Train_Date = '{idate}' AND b.Status = 'Booked';''')
    

    records=iq2_cur.fetchall()
    print_records=''
    for record in records:
        print_records+=record[0]+"\t"+record[1]+"\t"+record[2]+"\t"+record[3]+"\t"+record[4] +"\n"
    iq2_label=Tk.Label(root,text=print_records)
    iq2_label.grid(row=16,column=0,columnspan=2)
    iq2.commit()
    iq2.close()
def input_query3():
    age=age_input.get()
    iq2=sqlite3.connect('FOC.db')

    iq2_cur=iq2.cursor()
    
    iq2_cur.execute(f'''select t.Train_Name, t.Train_Number,t.Source_Station,t.Destination_Station,p.First_name, p.Last_name, strftime('%Y', date('now'))-strftime('%Y',Bdate) as A, {age} as iage  
    from passengers p, TRAIN t where A between 50 and 60 and iage = A;
                    ''')
    

    records=iq2_cur.fetchall()
    print_records=''
    print(records)
    for record in records:
        print_records+=str(record[0])+record[1]+str(record[2])+str(record[3])+str(record[4])+str(record[5]) +"\n"
    iq2_label=Tk.Label(root,text=print_records)
    iq2_label.grid(row=30,column=0,columnspan=2)
    iq2.commit()
    iq2.close()

def input_query4():
    
    
    
    iq4=sqlite3.connect('FOC.db')

    iq4_cur=iq4.cursor()
    
    iq4_cur.execute("SELECT t.Train_Name,COUNT(*) FROM Train t INNER JOIN Booked b ON t.Train_Number=b.Train_Number GROUP BY t.Train_Name;")
    

    records=iq4_cur.fetchall()
    print_records=''
    for record in records:
        print_records+=record[0]+ str(record[1]) +"\n"
    iq4_label=Tk.Label(root,text=print_records)
    iq4_label.grid(row=18,column=0,columnspan=2)
    iq4.commit()
    iq4.close()
def input_query5():
    
    name=Train_Name.get()
    print(name)
    
    iq5=sqlite3.connect('FOC.db')

    iq5_cur=iq5.cursor()
    
    iq5_cur.execute(f'''SELECT p.*,b.Ticket_Types,b.Train_Number FROM PASSENGERS p INNER JOIN BOOKED b ON p.Ssn=b.Passenger_ssn INNER JOIN TRAIN t ON t.Train_Number=b.Train_Number INNER JOIN TRAIN_STATUS ts ON ts.Train_Name=t.Train_Name WHERE b.Status='Booked' AND ts.Train_Name='{name}';''')
    

    records=iq5_cur.fetchall()
    print_records=''
    for record in records:
        print_records+=record[0]+"\t"+ record[1] +str(record[2])+record[3]+record[4]+str(record[5])+str(record[6])+str(record[7])+str(record[8])+str(record[9])+"\n"
    iq5_label=Tk.Label(root,text=print_records)
    iq5_label.grid(row=20,column=0,columnspan=2)
    iq5.commit()
    iq5.close()
    
def input_query6():
    iq6=sqlite3.connect('FOC.db')
    iq6_cur=iq6.cursor()
    # iq1_cur.execute(f'''delete from booked where passanger_ssn = {ssn};''', new_box.get())
    ssn = Passenger_ssn.get()
    iq6_cur.execute(f'''delete from booked where Passenger_ssn = {ssn};''')
    to_be_updated = iq6_cur.execute(f'''select * from booked where status = "WaitL" group by status;''').fetchall()  #no change here
    iq6_cur.execute(f'''update booked set status = "Booked" where Passenger_ssn = {to_be_updated[0][0]};''') #no change here
    records=iq6_cur.execute('''select * from booked''').fetchall()
    #print(records)
    print_records=''
    for record in records:
        print_records+=str(record[0] +record[1]+ record[2] +record[3]+"\n")
    iq6_label=Tk.Label(root,text=print_records)
    iq6_label.grid(row=15,column=0,columnspan=2)
    iq6.commit()
    iq6.close()
    
First_name=Tk.Entry(root,width=30)
First_name.grid(row=0,column=1)
Last_name=Tk.Entry(root,width=30)
Last_name.grid(row=1,column=1)
Train_Date=Tk.Entry(root,width=30)
Train_Date.grid(row=2,column=1)
Train_Name=Tk.Entry(root,width=30)
Train_Name.grid(row=3,column=1)
age_input = Tk.Entry(root,width=30)
age_input.grid(row=4,column=1)
Passenger_ssn = Tk.Entry(root,width=30)
Passenger_ssn.grid(row=5,column=1)

First_name_Label = Tk.Label(root, text='First_name: ')
First_name_Label.grid(row=0,column=0)
Last_name_Label = Tk.Label(root, text='Last_name: ')
Last_name_Label.grid(row=1,column=0)
Train_Date_Label=Tk.Label(root,text='Train_Date')
Train_Date_Label.grid(row=2,column=0)
Train_Name_Label=Tk.Label(root,text='Train_Name')
Train_Name_Label.grid(row=3,column=0)
age_Label=Tk.Label(root,text='AGE')
age_Label.grid(row=4,column=0)
Passenger_ssn_label=Tk.Label(root,text='Ssn')
Passenger_ssn_label.grid(row=5,column=0)

iq_button=Tk.Button(root,text='Query1_Show Records_FN_LN',command=input_query1)
iq_button.grid(row=0,column=3,columnspan=2,pady=10,padx=10,ipadx=100)

iq_button1=Tk.Button(root,text='Query2_Show Records_TD',command=input_query2)
iq_button1.grid(row=1,column=3,columnspan=2,pady=10,padx=10,ipadx=100)

iq_button2=Tk.Button(root,text='Query3_Show Records_Age',command=input_query3)
iq_button2.grid(row=2,column=3,columnspan=2,pady=10,padx=10,ipadx=100)

iq_button3=Tk.Button(root,text='Query4_Show Records_DC',command=input_query4)
iq_button3.grid(row=3,column=3,columnspan=2,pady=10,padx=10,ipadx=100)

iq_button4=Tk.Button(root,text='Query5_Show Records_TN',command=input_query5)
iq_button4.grid(row=4,column=3,columnspan=2,pady=10,padx=10,ipadx=100)

iq_button5=Tk.Button(root,text='Query6_Show Records',command=input_query6)
iq_button5.grid(row=5,column=3,columnspan=2,pady=10,padx=10,ipadx=100)

print("code ran successfully")
root.mainloop()