import tkinter as tk 

class Ui:
    def __init__(self):
        self.ui= tk.Tk() 
        self.ui.minsize(width=500,height=500)
        self.frame_grid = tk.Frame(self.ui)
        self.frame_grid.pack(side='left', fill='both', expand=True)
        self.frame_pack = tk.Frame(self.ui)
        self.frame_pack.pack(side='right', fill='both', expand=True)
        self.canvas=[]
        self.inputs = [] 
        self.buttons=[]
        
    def make_label(self,**kwargs):
        self.label = tk.Label(self.frame_grid, text=kwargs.get('name', 'Hello there'), font=("Arial", kwargs.get("size",16), "bold"))
        self.label.grid(column=kwargs.get('column', 0), row=kwargs.get('row', 0))
        
    def try_catch_button(self, **kwargs):
        self.button = tk.Button(self.frame_grid, text=kwargs.get('name', 'Click me'), width=kwargs.get('width', 25), command=self.get_inputs)
        self.button.grid(column=kwargs.get('column', 0), row=kwargs.get('row', 0))

    def make_buttons(self, **kwargs):
        self.button = tk.Button(self.frame_grid, text=kwargs.get('name', 'Click me'), width=kwargs.get('width', 25), command=kwargs.get('event', self.get_inputs))
        self.button.grid(column=kwargs.get('column', 0), row=kwargs.get('row', 0))
        self.buttons.append(self.button)
        
    def get_buttons(self,index):
        self.buttons[index]
    
    def make_input(self, **kwargs):
        self.input = tk.Entry(self.frame_grid)
        self.input.grid(column=kwargs.get('column', 1), row=kwargs.get('row', 0))
        self.inputs.append(self.input)


    def sphere(self, x=10, y=10):
        canva = tk.Canvas(self.frame_pack)
        oval = canva.create_oval(x, y, x+70, y+70, outline = "black", fill = "white", width = 2)
        canva.pack()
        return (canva, oval)
   
    def position_canvas(self,index,x=0,y=0):
        self.canvas[index].place(x=x, y=y)
        
    
    def try_catch_if(self,intems):
        intems=[int(i) for i in intems]
        if (intems[0] != 0):
            delta=intems[2]-intems[1]
            x=delta/intems[0]
            print(x)
			
   
    def try_catch(self,intems):
       try:
           intems=[int(i) for i in intems]
           delta=intems[2]-intems[1]
           x=delta/intems[0]
           print(x)
       except ZeroDivisionError:
           self.make_label(name="Don t divide with 0 🤦‍♂️",row=6,column=2)
       except ValueError:
           self.make_label(name="Don t write character 💀",row=6,column=2)
    
    
    def get_inputs(self):
        fill_intem=[]
        for i, input_field in enumerate(self.inputs):
            input_text = input_field.get()
            fill_intem.append(input_text)
        self.try_catch(fill_intem)
        


    def main(self):
 
        self.ui.mainloop()
