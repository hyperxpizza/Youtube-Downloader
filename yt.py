try:                        
    from tkinter import *   
    from tkinter import filedialog 
except:
    from Tkinter import *
    from Tkinter import filedialog

#pytube
from pytube import YouTube

#Fonts & Colors
FONT = ('Verdana', 20)

class Window():

    def __init__(self):
        self.urls = []
        self.set_tk()
        self.set_widgets()
        

    def set_tk(self):
        self.root = Tk()
        self.root.geometry("400x400")
        self.root.configure(background="white")
        self.root.resizable(False,False)
        self.root.title("Youtube Downloader")
    
    def exit(self):
        quit()

    def add_url(self):
        self.input_url = self.txt_input.get()

        #add url to list
        self.urls.append(self.input_url)
        self.txt_input.delete(0,"end")

    def set_widgets(self):
        self.lbl_text = Label(self.root, text="Youtube Downloader", bg="white", font=FONT)
        self.lbl_text.pack()

        self.lbl_disp = Label(self.root, text="", bg="white")
        self.lbl_disp.pack()

        self.txt_input = Entry(self.root, width=200)
        self.txt_input.pack()

        self.btn_add_url = Button(self.root, text="Add Url", fg="green", bg="white", command=self.add_url)
        self.btn_add_url.pack()

        self.choice = IntVar()
        self.btn_choice = Checkbutton(self.root, text="Audio only?", variable=self.choice)
        self.btn_choice.pack()

        self.btn_download = Button(self.root, text="Download", fg="green", bg="white", command=self.download)
        self.btn_download.pack()

        self.btn_exit = Button(self.root,text="Exit", bg="white", fg="green", command=self.exit)
        self.btn_exit.pack()

    def download(self):
        self.root.directory = filedialog.askdirectory()
        self.dir_path = self.root.directory + "/"
        
        for self.url in self.urls:
            self.yt = YouTube(self.url)
        
            if self.choice.get() == 0:
                self.stream = self.yt.streams.first()
                self.stream.download(self.dir_path)

            else:
                self.stream = self.yt.streams.filter(only_audio=True).first()
                self.stream.download(self.dir_path)


def Main():
    app = Window()
    app.root.mainloop()

if __name__ == "__main__":
    Main()