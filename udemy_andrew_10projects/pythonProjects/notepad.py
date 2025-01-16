import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button


class Notepad:
    def __init__(self,root:Tk)->None: #Tk is like a parent for our root (main window or interface)
        self.root=root
        self.root.title("Oversimplified notepad")

        #Default file path
        self.current_file_path=None

        #Text widget
        self.text_area:Text=Text(self.root,wrap="word") #root stands for the notepad's window (interface)
        self.text_area.pack(expand=True,fill="both") #we use the "pack" method to fill the area. "both" means we can fill the area horizontally and vertically

        #Frame
        self.button_frame:Frame=Frame(self.root) #creates a frame inside our notepad's window
        self.button_frame.pack()

        #Save button
        self.save_button:Button=Button(self.button_frame,text="Save",command=self.save_file) #we use here "self.button_frame" instead of "self.root" because it's inside the root
        self.save_button.pack(side=tk.LEFT) #whereabouts of our "save button"

        #Load button
        self.load_button: Button = Button(self.button_frame, text="Load", command=self.load_file)
        self.load_button.pack(side=tk.RIGHT)

    def save_file(self)->None:
        if self.current_file_path is None:
            self.current_file_path:str=filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files","*.txt")])
        if self.current_file_path:
            with open(self.current_file_path,"w") as file:
                file.write(self.text_area.get(1.0,tk.END))
            print(f"File saved to: {self.current_file_path}") #we use "file_name" instead of "file" for the more human-readable code

    def load_file(self)->None:
        file_name: str = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        with open(file_name, "r") as file:
            content:str=file.read()
            self.text_area.delete(1.0,tk.END)
            self.text_area.insert(tk.INSERT,content)
        self.current_file_path=file_name #to remember the "just loaded file", so we can easier save it later (it won't be asking us every time when we try to save the loaded file)
        print(f"File loaded from: {file_name}")

    def run_notepad(self)->None:
        self.root.mainloop() #mainloop is like a prop that keeps our notepad's window open (without, it would've immediately closed)


def call_notepad()->None:
    root:Tk=tk.Tk() #Tk is a parent for our root
    app:Notepad=Notepad(root=root) #root=notepad's window
    app.run_notepad()


if __name__=="__main__":
    call_notepad()