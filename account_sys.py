from tkinter import *
from tkinter import simpledialog
from socket import *

class AccountSystem(object):
    def __init__(self, ok):
        self.ok=ok
        self.root = Tk()
        self.root.title("RE:WORLD | LOGIN")

        self.root.resizable(False, False)

    def home(self):
        self.clear()
        self.login = Button(self.root, text="LOGIN TO RE:WORLD", command=self.login_ac)
        self.login.pack()

        self.create = Button(self.root, text="CREATE AN ACCOUNT", command=self.cr_acc)
        self.create.pack()

        mainloop()

    def login_ac(self):
        self.clear()
        self.title = Label(self.root, text="LOGIN TO RE:WORLD")
        self.title.pack()

        self.uframe = Frame(self.root)
        self.uframe.pack()

        self.userlabel = Label(self.uframe, text="Username : ")
        self.userlabel.pack(side=LEFT)

        self.usernameentry = Entry(self.uframe, width=30)
        self.usernameentry.pack(side=LEFT)

        self.pframe = Frame(self.root)
        self.pframe.pack()

        self.passw = Label(self.pframe, text="Password : ")
        self.passw.pack(side=LEFT)

        self.passwentry = Entry(self.pframe, width=30)
        self.passwentry.configure(show='•')
        self.passwentry.pack(side=LEFT)

        self.confirm = Button(self.root, text="LOGIN", command=self.login_action)
        self.confirm.pack()

    def login_action(self):
        try:
            #do login request
            ...
        except Exception as e:
            #network error
            simpledialog.messagebox.showerror(f"Failed to login", "An error occured with the auth server. Please report this to the discord server.\n{e}")
        finally:
            if "requete" == "success":  #template... :-(
                simpledialog.messagebox.showinfo("Login", "You succesfully logged in into RE:WORLD !")
                self.root.destroy()
                self.ok()
            else:
                simpledialog.messagebox.showwarning("Failed to login", "Failed to login : Username or password incorrect.")


    def cr_acc(self):
        self.clear()
        self.title = Label(self.root, text="Create an account\nEnter your username here :\n(5 to 15 char max, only letters, numbers or _)")
        self.title.pack()

        self.usernameentry = Entry(self.root, width=30)
        self.usernameentry.pack()

        self.pf1 = Frame(self.root)
        self.pf1.pack()

        self.passw1 = Label(self.pf1, text="Password : ")
        self.passw1.pack(side=LEFT)

        self.passw1entry = Entry(self.pf1, width=30)
        self.passw1entry.configure(show='•')
        self.passw1entry.pack(side=LEFT)

        self.pf2 = Frame(self.root)
        self.pf2.pack()

        self.passw2 = Label(self.pf2, text="Confirm password : ")
        self.passw2.pack(side=LEFT)

        self.passw2entry = Entry(self.pf2, width=30)
        self.passw1entry.configure(show='•')
        self.passw2entry.pack(side=LEFT)

        self.confirm = Button(self.root, text="CONFIRM", command=self.cr_confirm)

        self.confirm.pack()

    def cr_confirm(self):
        username = self.usernameentry.get()
        passw = self.passw1entry.get()
        passw2 = self.passw2entry.get()

        if passw != passw2:
            simpledialog.messagebox.showwarning("Task failed", "The passwords must be the same !")
        else:
            try:
                skt = socket(AF_INET, SOCK_STREAM)
                skt.connect(("127.0.0.1", 9606))    #to change
                skt.send(bytes(f"\x00-{username}-{passw}"), 1024)
                msg =skt.recv(1024).decode()
                if msg.split("-")[0] == "\x00":
                    simpledialog.messagebox.showerror("Task failed", f"[Error code {msg.split('-')[1]}\n{msg.split('-')[2]}")
                if msg.split("-")[0] == "\x01":
                    simpledialog.messagebox.showinfo("Account creation", "You succesfully created an account to RE:WORLD !")
                    self.root.destroy()
                    self.ok()
            except Exception as e:
                simpledialog.messagebox.showerror("Task failed", "Something went wrong. Please report this to the discord server.\n{0}".format(e))

    def clear(self):
        try:
            self.login.destroy()
            self.create.destroy()
        except:
            pass