import tkinter as tk

class App(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = MainFrame(self)
        self._frame.pack()
        

class MainFrame(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.rowconfigure(1, minsize=400, weight=1)
        self.columnconfigure(0, minsize=800, weight=1)
        self.fr_tool_bar = ToolBar(self)
        self.fr_tool_bar.grid(row=0,column=0,sticky="nsew")
        self.fr_canvas = OptionsFrame(self)
        self.fr_canvas.grid(row=1,column=0,stick="nsew")

    def switch_frame(self,frame_class):
        new_frame = frame_class(self)
        if self.fr_canvas is not None:
            self.fr_canvas.destroy()
        self.fr_canvas = new_frame
        self.fr_canvas.grid(row=1,column=0,stick="nsew")
        
class ToolBar(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.btn_main = tk.Button(self,text="MAIN",command=lambda: master.switch_frame(SecondFrame))
        self.btn_main.pack(side=tk.LEFT)

class OptionsFrame(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master,background="blue")

class SecondFrame(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master,background="red")


if __name__ == "__main__":
    app = App()
    app.mainloop()
