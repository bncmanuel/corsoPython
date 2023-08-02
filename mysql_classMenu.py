import mysql.connector
from tkinter import messagebox
from tkinter import *
from tkinter import font
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Menu:
  def __init__(self, prezzo):
    self.prezzo = prezzo

  def __str__(self):
    return f"{self.prezzo}"

menu_carne = Menu(25)
menu_pesce = Menu(30)
menu_bambini = Menu(20)

def invia_email(destinatario, oggetto, corpo):
    # Configura il server SMTP per inviare l'email (in questo esempio utilizzo Gmail)
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "bianconemanuel@gmail.com"  # Inserisci il tuo indirizzo email
    sender_password = "hlalxfooofbrlntd"  # Inserisci la tua password email

    # Messaggio email
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = destinatario
    message["Subject"] = oggetto
    message.attach(MIMEText(corpo, "plain"))

    # Connessione e invio dell'email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, destinatario, message.as_string())
        print("Email inviata con successo!")
    except Exception as e:
        print("Errore nell'invio dell'email:", str(e))
    finally:
        server.quit()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="CorsoPython2206",
  database="ristorante"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE Staff (Username VARCHAR(255), Password VARCHAR(255))")
# user = "Manuel"
# pwd = "admin"
#
# sql = "INSERT INTO staff (Username, Password) VALUES (%s, %s)"
# val = (user, pwd)
# mycursor.execute(sql, val)
# mydb.commit()



# HO CREATO LA TABELLA PER AGGIUNGERE GLI ORDINI NEL DATABASE "ristorante"
# mycursor.execute("CREATE TABLE ordini (email VARCHAR(255), menu VARCHAR(255), prezzo VARCHAR(255))")

# scelta = input("...")
# email = input("Inserisci la tua email per registrare l'ordine: ")

# while scelta != 0:
#   scelta = input("""
#   Scegli un menù:
#   1) Menù di carne - 25€
#   2) Menù di pesce - 30€
#   3) Menù bambini - 20€
#
#   0) Annullare l'ordine
#
#   ...""")
#
#   if scelta == "1":
#     sql = "INSERT INTO ordini (email, menu, prezzo) VALUES (%s, %s, %s)"
#     values = (email, "Menù carne", menu_carne.prezzo)
#     mycursor.execute(sql, values)
#     mydb.commit()
#     print("Hai scelto il menù di carne.\nLa tua scelta è stata aggiunta agli ordini.")
#   if scelta == "2":
#     sql = "INSERT INTO ordini (email, menu, prezzo) VALUES (%s, %s, %s)"
#     values = (email, "Menù pesce", menu_pesce.prezzo)
#     mycursor.execute(sql, values)
#     mydb.commit()
#     print("Hai scelto il menù di pesce.\nLa tua scelta è stata aggiunta agli ordini.")
#   if scelta == "3":
#     sql = "INSERT INTO ordini (email, menu, prezzo) VALUES (%s, %s, %s)"
#     values = (email, "Menù bambini", menu_bambini.prezzo)
#     mycursor.execute(sql, values)
#     mydb.commit()
#     print("Hai scelto il menù bambini.\nLa tua scelta è stata aggiunta agli ordini.")
#   if scelta == "0":
#     mycursor.execute("SELECT * FROM ordini")
#     myresult = mycursor.fetchall()
#     sum = 0
#     for x in myresult:
#       sum += int(x[2])
#       print(x)
#     print("\nIl totale incassi del ristorante è:", sum)
#     break


#creo una finestra

win = Tk()
win.title('Login')

#centro la finestra
width = 360
height = 180
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
win.geometry('%dx%d+%d+%d' % (width, height, x, y))

#creo un font personalizzato per le entry, necessario importare font prima
custom_font = font.Font(size=11)

#aggiungo le entry e le posiziono
e1 = Entry(win, font=custom_font)
e1.place(relx=0.5, rely=0.4, anchor=CENTER)

def admin_access():
    # creo una finestra login admin
    win.withdraw()
    admin_page = Toplevel(win)
    admin_page.title("Area admin")
    # per centrare la finestra login admin
    width = 480
    height = 360
    screen_width = admin_page.winfo_screenwidth()
    screen_height = admin_page.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    admin_page.geometry('%dx%d+%d+%d' % (width, height, x, y))
    # aggiungo le entry e le posiziono
    admin_user_lbl = Label(admin_page, text="Admin username", font=custom_font)
    admin_user_lbl.place(relx=0.445, rely=0.36, anchor=CENTER)
    admin_user = Entry(admin_page, font=custom_font)
    admin_user.place(relx=0.50, rely=0.42, anchor=CENTER)
    admin_psw_lbl = Label(admin_page, text="Admin password", font=custom_font)
    admin_psw_lbl.place(relx=0.445, rely=0.51, anchor=CENTER)
    admin_psw = Entry(admin_page, font=custom_font, show="*")
    admin_psw.place(relx=0.50, rely=0.57, anchor=CENTER)
    # pulsante per accedere all'area admin
    btn_admin = Button(admin_page, text="Accedi", font=custom_font, width=5, height=1) #manca command
    btn_admin.place(relx=0.5, rely=0.68, anchor=CENTER)
    # pulsante per chiudere tutto (area accesso admin)
    btn_esci2 = Button(admin_page, text="Esci", command=esci, font=custom_font)
    btn_esci2.place(relx=0.15, rely=0.9, anchor=CENTER)

    # # vado a controllare l'username specifico fornito dall'utente
    # sql_user = f"SELECT * FROM staff WHERE Username ='{username}'"  # seleziona dall'indirizzo specifico
    # mycursor.execute(sql_user)
    # myresult = mycursor.fetchall()
    # if e1.get() == username and e2.get() == password:
    #     # creo una seconda finestra
    #     new_window = Toplevel(root)
    #     new_window.title("Nuova Finestra")
    #     lbl = Label(new_window, text="Login effettuato con successo!", justify=CENTER)
    #     lbl.grid()
    #     # per centrare la seconda finestra
    #     width = 400
    #     height = 300
    #     screen_width = new_window.winfo_screenwidth()
    #     screen_height = new_window.winfo_screenheight()
    #     x = (screen_width / 2) - (width / 2)
    #     y = (screen_height / 2) - (height / 2)
    #     new_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    # else:
    #     messagebox.showinfo("Alert", "Accesso negato.")

def esci():
    messagebox.showinfo("Annullato", "Sei uscito. Alla prossima!")
    exit(1)
def click():
    # email = e1.get()
    spesa = []
    spesa_print = []
    # creo una seconda finestra
    win.withdraw()
    new_win = Toplevel(win)
    new_win.title("Scelta menù")
    # per centrare la seconda finestra
    width = 480
    height = 360
    screen_width = new_win.winfo_screenwidth()
    screen_height = new_win.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    new_win.geometry('%dx%d+%d+%d' % (width, height, x, y))
    lbl = Label(new_win, text="Scegli cosa vuoi ordinare", font=custom_font)
    lbl.place(relx=0.5, rely=0.15, anchor=CENTER)
    totale = Label(new_win, text="Totale: 0€", font=custom_font)
    totale.place(relx=0.5, rely=0.6, anchor=CENTER)

    # # vado a controllare l'username specifico fornito dall'utente
    # sql_check = f"SELECT * FROM accounts WHERE username ='{username}'"  # seleziona dall'indirizzo specifico
    # mycursor.execute(sql_check)
    # myresult = mycursor.fetchall()

    def update():
        totale.config(text=f"Totale: {sum(spesa)}€")

    def carne():
      sql = "INSERT INTO ordini (email, menu, prezzo) VALUES (%s, %s, %s)"
      values = (e1.get(), "Menù carne", menu_carne.prezzo)
      mycursor.execute(sql, values)
      mydb.commit()
      # aggiungo il prezzo alla lista per il totale e il menù da inviare per email
      spesa.append(int(menu_carne.prezzo))
      spesa_print.append("Menù carne")
      totale.config(text="Hai aggiunto menù carne (+25€)") # text temporaneo
      totale.after(1000, update)

    def pesce():
      sql = "INSERT INTO ordini (email, menu, prezzo) VALUES (%s, %s, %s)"
      values = (e1.get(), "Menù pesce", menu_pesce.prezzo)
      mycursor.execute(sql, values)
      mydb.commit()
      # aggiungo il prezzo alla lista per il totale e il menù da inviare per email
      spesa.append(int(menu_pesce.prezzo))
      spesa_print.append("Menù pesce")
      totale.config(text="Hai aggiunto menù pesce (+30€)")  # text temporaneo
      totale.after(1000, update)

    def bambini():
      sql = "INSERT INTO ordini (email, menu, prezzo) VALUES (%s, %s, %s)"
      values = (e1.get(), "Menù bambini", menu_bambini.prezzo)
      mycursor.execute(sql, values)
      mydb.commit()
      # aggiungo il prezzo alla lista per il totale e il menù da inviare per email
      spesa.append(int(menu_bambini.prezzo))
      spesa_print.append("Menù bambini")
      totale.config(text="Hai aggiunto menù bambini (+20€)")  # text temporaneo
      totale.after(1000, update)



    def completa():
      spesa_totale = ", ".join(spesa_print)
      oggetto = "Conferma ordine"
      corpo = f"Grazie per il suo ordine!\n\nIl suo ordine:\n{spesa_totale}\n\nTotale: {sum(spesa)}€\n\nLa aspettiamo nuovamente presso il nostro ristorante!\nBuona giornata"
      invia_email(e1.get(), oggetto, corpo)
      messagebox.showinfo("Ordine completato", f"Ordine completato. Il totale complessivo è: {sum(spesa)}€\nLe abbiamo inviato una mail per la conferma. Grazie!")
      exit(1)

    btn_carne = Button(new_win, text="🥩 Menù carne 25€", command=carne, font=custom_font)
    btn_carne.place(relx=0.5, rely=0.30, anchor=CENTER)

    btn_pesce = Button(new_win, text="🐟 Menù pesce 30€", command=pesce, font=custom_font)
    btn_pesce.place(relx=0.5, rely=0.40, anchor=CENTER)

    btn_bambini = Button(new_win, text="🌭 Menù bambini 20€", command=bambini, font=custom_font)
    btn_bambini.place(relx=0.5, rely=0.50, anchor=CENTER)

    btn_esci = Button(new_win, text="Annulla l'ordine", command=esci, font=custom_font)
    btn_esci.place(relx=0.25, rely=0.88, anchor=SW)

    btn_completa = Button(new_win, text="Completa l'ordine", command=completa, font=custom_font)
    btn_completa.place(relx=0.8, rely=0.88, anchor=SE)

#pulsante di login sulla main page
btn_login = Button(win, text="Accedi", command=click, height=1, width=10)
btn_login.place(relx=0.5, rely=0.55, anchor=CENTER)

#pulsante per andare sulla pagina admin login
btn_gestore = Button(win, text="Gestore", command=admin_access, height=1, width=8)
btn_gestore.place(relx=0.80, rely=0.85, anchor=CENTER)

#pulsante per chiudere tutto
btn_esci1 = Button(win, text="Esci", command=esci, font=custom_font)
btn_esci1.place(relx=0.20, rely=0.85, anchor=CENTER)

win.mainloop()