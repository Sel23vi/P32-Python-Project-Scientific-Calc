import tkinter as tk
import math
import random
import time

root = tk.Tk()

root.title("Scientific Calculator")
root.configure(background="#E0FFFF")
root.resizable(width=False, height=True)
root.geometry("275x605+0+0")

class Calc():
    def __init__(self, root):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.operator = ""
        self.result = False
        self.button_dottwond_state = 0
        self.button_hyp_state = 0
        self.button_trig_state = 1
        self.button_rad_state = 0
        self.button_2nd_state = 0
        self.counter = 0
        self.func_mode = False
        self.fe_mode = False  # False for Fixed, True for Exponential
        self.create_widgets(root)

    def create_widgets(self, root):
        self.button_rad = tk.Button(root, text="DEG", width=12, height=2, font=("Helvetica", 10, 'bold'),
                            bd=4, bg="#E6E6FA", command=self.toggle_rad)
        self.button_rad.grid(row=12, column=0, pady=1,columnspan=2)
        self.button_fe = tk.Button(root, text="F-E", width= 12, height=2,font =("Helvetica", 10, 'bold'),
                  bd = 4, bg = "#E6E6FA",command=self.toggle_fe)
        self.button_fe.grid(row=12, column=2, pady=1, columnspan=2)
        self.button_trig = tk.Button(root, text="Trignometry", width=12, height=2, font=("Helvetica", 10, 'bold'),
                             bd=4, bg="#E6E6FA", command=lambda: self.toggle_trig(3))
        self.button_trig.grid(row=13, column=0, pady=1,columnspan=2)
        self.button_func = tk.Button(root, text="Functions", width=12, height=2, font=("Helvetica", 10, 'bold'),
                                bd=4, bg="#E6E6FA", command=self.toggle_func)
        self.button_func.grid(row=13, column=2, pady=1, columnspan=2)
        self.button_2nd = tk.Button(root, text="2\u207f\u1d48", width=3, height=1, font=("Helvetica", 15, 'bold'),
                               bd=4, bg="#E6E6FA", command=self.toggle_2nd)
        self.button_2nd.grid(row=4, column=0, pady=1)
        self._2nd_buttons0 = {
            'xpow2': tk.Button(root, text="x\u00b2", width=3, height=1, font=("Helvetica", 15, 'bold'), bd=4, bg="#E6E6FA", command=self.xpow2).grid(row=5, column=0, pady=1),
            '2sqrtx': tk.Button(root, text="\u00B2\u221Ax", width=3, height=1, font=("Helvetica", 15, 'bold'),bd=4, bg="#E6E6FA", command=self.SqRx).grid(row=6, column=0, pady=1),
            'xpowy': tk.Button(root, text="𝑥ʸ ", width=3, height=1, font=("Helvetica", 15, 'bold'), bd=4, bg="#E6E6FA", command=lambda: self.operation("**")).grid(row=7, column=0, pady=1),
            '10powx': tk.Button(root, text="10\u02E3", width=3, height=1, font=("Helvetica", 15, 'bold'), bd=4, bg="#E6E6FA", command=self.tenpowx).grid(row=8, column=0, pady=1),
            'log': tk.Button(root, text="log", width=3, height=1, font=("Helvetica", 15, 'bold'), bd=4, bg="#E6E6FA", command=self.log).grid(row=9, column=0, pady=1),
            "ln": tk.Button(root, text="ln", width=3, height=1, font=("Helvetica", 15, 'bold'), bd=4, bg="#E6E6FA", command=self.ln).grid(row=10, column=0, pady=1)
        }

        self.create_trig_buttons(root)
        self.create_func_buttons(root)
        self.create_2nd_buttons1(root)

    def create_trig_buttons(self, root):
        self.trig_buttons_sin = {
            '2nd': tk.Button(root, text='2nd', width=4, height=2, font=("Helvetica", 10, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585", command=self.toggle_dottwond),
            'hyp': tk.Button(root, text="hyp", width=4, height=2, font=("Helvetica", 10, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self.toggle_hyp),
            'sin': tk.Button(root, text='sin', width=4, height=2, font=("Helvetica", 10, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trig('sin')),
            'cos': tk.Button(root, text='cos', width=4, height=2, font=("Helvetica", 10, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trig('cos')),
            'tan': tk.Button(root, text='tan', width=4, height=2, font=("Helvetica", 10, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trig('tan')),
            'sec': tk.Button(root, text='sec', width=4, height=2, font=("Helvetica", 10, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trig('sec')),
            'csc': tk.Button(root, text='csc', width=4, height=2, font=("Helvetica", 10, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trig('csc')),
            'cot': tk.Button(root, text='cot', width=4, height=2, font=("Helvetica", 10, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trig('cot'))
        }

        self.trig_buttons_asin = {
            '2nd': tk.Button(root, text='2nd', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0",fg = "#C71585",command=self.toggle_dottwond),
            'hyp': tk.Button(root, text="hyp", width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0",fg = "#C71585",command=self.toggle_hyp),
            'asin': tk.Button(root, text='sin⁻¹', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0",fg = "#C71585",command=lambda: self.calculate_trig('asin')),
            'acos': tk.Button(root, text='cos⁻¹', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0",fg = "#C71585",command=lambda: self.calculate_trig('acos')),
            'atan': tk.Button(root, text='tan⁻¹', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0",fg = "#C71585",command=lambda: self.calculate_trig('atan')),
            'asec': tk.Button(root, text='sec⁻¹', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0",fg = "#C71585",command=lambda: self.calculate_trig('asec')),
            'acsc': tk.Button(root, text='csc⁻¹', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0",fg = "#C71585",command=lambda: self.calculate_trig('acsc')),
            'acot': tk.Button(root, text='cot⁻¹', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0",fg = "#C71585",command=lambda: self.calculate_trig('acot'))
        }

        self.trig_buttons_sinh = {
            '2nd': tk.Button(root, text='2nd', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=self.toggle_dottwond),
            'hyp': tk.Button(root, text="hyp", width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=self.toggle_hyp),
            'sinh': tk.Button(root, text='sinh', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('sinh')),
            'cosh': tk.Button(root, text='cosh', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('cosh')),
            'tanh': tk.Button(root, text='tanh', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('tanh')),
            'sech': tk.Button(root, text='sech', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('sech')),
            'csch': tk.Button(root, text='csch', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('csch')),
            'coth': tk.Button(root, text='coth', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('coth'))
        }

        self.trig_buttons_asinh = {
            '2nd': tk.Button(root, text='2nd', width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=self.toggle_dottwond),
            'hyp': tk.Button(root, text="hyp", width=4, height=2, font=("Helvetica", 10, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=self.toggle_hyp),
            'asinh': tk.Button(root, text='sinh⁻¹', width=4, height=2, font=("Helvetica", 7, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('asinh')),
            'acosh': tk.Button(root, text='cosh⁻¹', width=4, height=2, font=("Helvetica", 7, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('acosh')),
            'atanh': tk.Button(root, text='tanh⁻¹', width=4, height=2, font=("Helvetica", 7, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('atanh')),
            'asech': tk.Button(root, text='sech⁻¹', width=4, height=2, font=("Helvetica", 7, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('asech')),
            'acsch': tk.Button(root, text='csch⁻¹', width=4, height=2, font=("Helvetica", 7, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('acsch')),
            'acoth': tk.Button(root, text='coth⁻¹', width=4, height=2, font=("Helvetica", 7, 'bold'), bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.calculate_trigh('acoth'))
        }

    def create_func_buttons(self, root):
        self.func_buttons = {
            'absx': tk.Button(root, text='|x|', width=3, height=1, font=("Helvetica", 15, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self.modx),
            'floorx': tk.Button(root, text='└x┘', width=3, height=1, font=("Helvetica", 15, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self.floorx),
            'cielx': tk.Button(root, text='┌x┐', width=3, height=1, font=("Helvetica", 15, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self.cielx),
            'rand': tk.Button(root, text='rand', width=4, height=2, font=("Helvetica", 11, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self.random),
            '>dms': tk.Button(root, text='>dms', width=4, height=2, font=("Helvetica", 11, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self.todms),
            '>deg': tk.Button(root, text='>deg', width=4, height=2, font=("Helvetica", 11, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self.todeg)
        }

    def create_2nd_buttons1(self, root):
        self._2nd_buttons1 = {
            'xcube': tk.Button(root, text='x\u00b3', width=3, height=1, font=("Helvetica", 15, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self.xcube),
            'cbrtx': tk.Button(root, text='\u00B3\u221Ax', width=3, height=1, font=("Helvetica", 15, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self.cbrtx),
            'yrtx': tk.Button(root, text='y\u221Ax', width=3, height=1, font=("Helvetica", 14, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=lambda: self.operation("***")),
            '2powx': tk.Button(root, text='2^x', width=3, height=1, font=("Helvetica", 14, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self._2powx),
            'logxtobasey': tk.Button(root, text='logₐx', width=4, height=2, font=("Helvetica", 10, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self.logxtobasey),
            'epowx': tk.Button(root, text='e^x', width=3, height=1, font=("Helvetica", 14, 'bold'),bd=4, bg="#FFFFE0", fg = "#C71585",command=self.epowx)
        }

    def numberEnter(self, num):
        self.result = False
        firstnum = e.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == ".":
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(e.get())

    def display(self, value):
        e.delete(0, tk.END)
        e.insert(0, value)

    def valid_function(self):
        if self.operator == "+":
            self.total += self.current
        if self.operator == "-":
            self.total -= self.current
        if self.operator == "*":
            self.total *= self.current
        if self.operator == "/":
            self.total /= self.current
        if self.operator == "mod":
            self.total %= self.current
        if self.operator == "**":
            self.total **= self.current
        if self.operator == "10**":
            self.total = self.total * (10**self.current)
        if self.operator == "***":
            self.total = self.total ** (1/self.current)
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, operator):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.operator = operator
        self.result = False

    def Clear_Entry(self):
        self.result = False
        firstnum = str(e.get())
        self.current = firstnum[0:len(firstnum)-1]
        e.delete(0, tk.END)
        self.numberEnter(self.current)

    def all_Clear_Entry(self):
        et.delete(0,tk.END)
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def display(self, value):
        e.delete(0, tk.END)
        e.insert(tk.END, str(value))

    def toggle_dottwond(self):
        self.button_dottwond_state = 1 - self.button_dottwond_state  # Toggle between 0 and 1
        new_color = "#FFD700" if self.button_dottwond_state == 1 else "#FFFFE0"
        self.trig_buttons_sin['2nd'].config(bg=new_color)
        self.trig_buttons_asin['2nd'].config(bg=new_color)
        self.trig_buttons_sinh['2nd'].config(bg=new_color)
        self.trig_buttons_asinh['2nd'].config(bg=new_color)
        self.toggle_trig(1)

    def toggle_hyp(self):
        self.button_hyp_state = 1 - self.button_hyp_state  # Toggle between 0 and 1
        new_color = "#FFD700" if self.button_hyp_state == 1 else "#FFFFE0"
        self.trig_buttons_sin['hyp'].config(bg=new_color)
        self.trig_buttons_asin['hyp'].config(bg=new_color)
        self.trig_buttons_sinh['hyp'].config(bg=new_color)
        self.trig_buttons_asinh['hyp'].config(bg=new_color)
        self.toggle_trig(1)

    def toggle_rad(self):
        self.button_rad_state = (self.button_rad_state + 1) % 3
        if self.button_rad_state == 0:
            self.button_rad.config(text="DEG")
        elif self.button_rad_state == 1:
            self.button_rad.config(text="RAD")
        elif self.button_rad_state == 2:
            self.button_rad.config(text="GRAD")

    def toggle_fe(self):
        self.fe_mode = not self.fe_mode
        if self.fe_mode:
            # Conversion to scientific notation
            try:
                ip = float(e.get())
                self.display(f"{ip:.6e}")
            except ValueError:
                self.diaplay("Invalid Input")
        else:
            # Conversion to fixed-point notation
            try:
                ip = float(e.get())
                self.display(f"{ip:.6f}")
            except ValueError:
                self.diaplay("Invalid Input")

    def toggle_trig(self, num):
        for btn in self.trig_buttons_sin.values():
            btn.grid_remove()
        for btn in self.trig_buttons_asin.values():
            btn.grid_remove()
        for btn in self.trig_buttons_sinh.values():
            btn.grid_remove()
        for btn in self.trig_buttons_asinh.values():
            btn.grid_remove()
        if num == 3:
            self.counter +=1
        if self.counter <= 1:
            # Define grid positions and sizes for trig buttons
            if self.button_dottwond_state == 0 and self.button_hyp_state == 0:
                self.trig_buttons_sin['2nd'].grid(row=14, column=0, pady=1, padx=0)
                self.trig_buttons_sin['hyp'].grid(row=15, column=0, pady=1, padx=0)
                self.trig_buttons_sin['sin'].grid(row=14, column=1, pady=1, padx=0)
                self.trig_buttons_sin['cos'].grid(row=14, column=2, pady=1, padx=0)
                self.trig_buttons_sin['tan'].grid(row=14, column=3, pady=1, padx=0)
                self.trig_buttons_sin['sec'].grid(row=15, column=1, pady=1, padx=0)
                self.trig_buttons_sin['csc'].grid(row=15, column=2, pady=1, padx=0)
                self.trig_buttons_sin['cot'].grid(row=15, column=3, pady=1, padx=0)

            elif self.button_dottwond_state == 1 and self.button_hyp_state == 0:
                self.trig_buttons_asin['2nd'].grid(row=14, column=0, pady=1, padx=0)
                self.trig_buttons_asin['hyp'].grid(row=15, column=0, pady=1, padx=0)
                self.trig_buttons_asin['asin'].grid(row=14, column=1, pady=1, padx=0)
                self.trig_buttons_asin['acos'].grid(row=14, column=2, pady=1, padx=0)
                self.trig_buttons_asin['atan'].grid(row=14, column=3, pady=1, padx=0)
                self.trig_buttons_asin['asec'].grid(row=15, column=1, pady=1, padx=0)
                self.trig_buttons_asin['acsc'].grid(row=15, column=2, pady=1, padx=0)
                self.trig_buttons_asin['acot'].grid(row=15, column=3, pady=1, padx=0)

            elif self.button_dottwond_state == 0 and self.button_hyp_state == 1:
                self.trig_buttons_sinh['2nd'].grid(row=14, column=0, pady=1, padx=0)
                self.trig_buttons_sinh['hyp'].grid(row=15, column=0, pady=1, padx=0)
                self.trig_buttons_sinh['sinh'].grid(row=14, column=1, pady=1, padx=0)
                self.trig_buttons_sinh['cosh'].grid(row=14, column=2, pady=1, padx=0)
                self.trig_buttons_sinh['tanh'].grid(row=14, column=3, pady=1, padx=0)
                self.trig_buttons_sinh['sech'].grid(row=15, column=1, pady=1, padx=0)
                self.trig_buttons_sinh['csch'].grid(row=15, column=2, pady=1, padx=0)
                self.trig_buttons_sinh['coth'].grid(row=15, column=3, pady=1, padx=0)

            elif self.button_dottwond_state == 1 and self.button_hyp_state == 1:
                self.trig_buttons_asinh['2nd'].grid(row=14, column=0, pady=1, padx=0)
                self.trig_buttons_asinh['hyp'].grid(row=15, column=0, pady=1, padx=0)
                self.trig_buttons_asinh['asinh'].grid(row=14, column=1, pady=1, padx=0)
                self.trig_buttons_asinh['acosh'].grid(row=14, column=2, pady=1, padx=0)
                self.trig_buttons_asinh['atanh'].grid(row=14, column=3, pady=1, padx=0)
                self.trig_buttons_asinh['asech'].grid(row=15, column=1, pady=1, padx=0)
                self.trig_buttons_asinh['acsch'].grid(row=15, column=2, pady=1, padx=0)
                self.trig_buttons_asinh['acoth'].grid(row=15, column=3, pady=1, padx=0)

        elif self.counter > 1:
            self.counter = 0
            # Hide trig buttons
            for btn in self.trig_buttons_sin.values():
                btn.grid_remove()
            for btn in self.trig_buttons_asin.values():
                btn.grid_remove()
            for btn in self.trig_buttons_sinh.values():
                btn.grid_remove()
            for btn in self.trig_buttons_asinh.values():
                btn.grid_remove()

    def toggle_func(self):
        self.func_mode = not self.func_mode
        if self.func_mode:
            # Define grid positions and sizes for func buttons
            self.func_buttons['absx'].grid(row=14, column=2, pady=1, padx=0)
            self.func_buttons['floorx'].grid(row=14, column=3, pady=1, padx=0)
            self.func_buttons['cielx'].grid(row=14, column=4, pady=1, padx=0)
            self.func_buttons['rand'].grid(row=15, column=2, pady=1, padx=0)
            self.func_buttons['>dms'].grid(row=15, column=3, pady=1, padx=0)
            self.func_buttons['>deg'].grid(row=15, column=4, pady=1, padx=0)
        else:
            # Hide func buttons
            for btn in self.func_buttons.values():
                btn.grid_remove()

    def toggle_2nd(self):
        self.button_2nd_state = not self.button_2nd_state
        if self.button_2nd_state:
            self.button_2nd.config(bg="#7B68EE")
            # for btn in self._2nd_buttons0.values():
            #     btn.grid_remove()
            self._2nd_buttons1['xcube'].grid(row=5, column=0, pady=1, padx=0)
            self._2nd_buttons1['cbrtx'].grid(row=6, column=0, pady=1, padx=0)
            self._2nd_buttons1['yrtx'].grid(row=7, column=0, pady=1, padx=0)
            self._2nd_buttons1['2powx'].grid(row=8, column=0, pady=1, padx=0)
            self._2nd_buttons1['logxtobasey'].grid(row=9, column=0, pady=1, padx=0)
            self._2nd_buttons1['epowx'].grid(row=10, column=0, pady=1, padx=0)

        else:
            self.button_2nd.config(bg="#E6E6FA")
            for btn in self._2nd_buttons1.values():
                btn.grid_remove()

    def maths_plus_minus(self):
        self.result = False
        self.current = -(float(e.get()))
        self.display(self.current)

    def nfact(self):
        self.result = False
        num = float(e.get())
        self.current = math.gamma(num+1)
        self.display(self.current)

    def ln(self):
        self.result = False
        num = float(e.get())
        self.current = math.log(num)
        self.display(self.current)

    def log(self):
        self.result = False
        num = float(e.get())
        self.current = math.log10(num)
        self.display(self.current)

    def tenpowx(self):
        self.result = False
        num = float(e.get())
        self.current = 10**num
        self.display(self.current)

    def SqRx(self):
        self.result = False
        self.current = math.sqrt (float(e.get()))
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def modx(self):
        self.result = False
        self.current = math.fabs(float(e.get()))
        self.display(self.current)

    def onedivx(self):
        self.result = False
        self.current = 1/(float(e.get()))
        self.display(self.current)

    def xpow2(self):
        self.result = False
        self.current = (float(e.get()))**2
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def xcube(self):
        self.result = False
        self.current = float(e.get())**3
        self.display(self.current)

    def cbrtx(self):
        self.result = False
        self.current = math.cbrt(float(e.get()))
        self.display(self.current)

    def _2powx(self):
        self.result = False
        self.current = math.pow(2,float(e.get()))
        self.display(self.current)

    def logxtobasey(self):
        et.insert(tk.END, "Enter x,y")
        self.result = False
        ip = str(e.get())
        lst = ip.split(',')
        x = float(lst[0])
        y = float(lst[1])
        self.current = math.log(x,y)
        self.display(self.current)

    def epowx(self):
        self.result = False
        self.current = math.e**float(e.get())
        self.display(self.current)

    def calculate_trig(self, func):
        ip = float(e.get())
        if self.button_rad_state == 0:  # Degrees
            ip = math.radians(ip)
        elif self.button_rad_state == 2:  # Gradians
            ip = math.pi * ip / 200

        if func == 'sin':
            self.current = math.sin(ip)
        elif func == 'cos':
            self.current = math.cos(ip)
        elif func == 'tan':
            self.current = math.tan(ip)
        elif func == 'sec':
            if ip != 0:
                self.current = 1/ math.cos(ip)
            else:
                self.current = "cos(0) is undefined"
        elif func == 'csc':
            if ip != 0:
                self.current = 1/ math.sin(ip)
            else:
                self.current = "sin(0) is undefined"
        elif func == 'cot':
            try:
                self.current = 1/math.tan(ip)
            except ZeroDivisionError:
                self.current = "sin(0) is undefined"
        elif func == 'asin':
            self.current = math.degrees(math.asin(ip)) if self.button_rad_state == 0 else math.asin(ip)
        elif func == 'acos':
            self.current = math.degrees(math.acos(ip)) if self.button_rad_state == 0 else math.acos(ip)
        elif func == 'atan':
            self.current = math.degrees(math.atan(ip)) if self.button_rad_state == 0 else math.atan(ip)
        elif func == 'acsc':
            try:
                self.current = math.degrees(math.asin(1/ip)) if self.button_rad_state == 0 else math.asin(1/ip)
            except ValueError:
                self.current = "Invalid Input"
        elif func == 'asec':
            try:
                self.current = math.degrees(math.acos(1/ip)) if self.button_rad_state == 0 else math.acos(1/ip)
            except ValueError:
                self.current = "Invalid Input"
        elif func == 'acot':
            self.current = math.degrees(math.atan(1/ip)) if self.button_rad_state == 0 else math.atan(1/ip)
        self.display(self.current)

    def calculate_trigh(self, func):
        ip = float(e.get())
        if func == 'sinh':
            self.current = math.sinh(ip)
        if func == 'cosh':
            self.current = math.cosh(ip)
        if func == 'tanh':
            self.current = math.tanh(ip)
        if func == 'sech':
            self.current = 1/math.cosh(ip)
        if func == 'csch':
            if ip != 0:
                self.current = 1 / math.sinh(ip)
            else:
                self.current = "csch(0) is undefined"
        if func == 'coth':
            if ip != 0:
                self.current = 1 / math.tanh(ip)
            else:
                self.current = "coth(0) is undefined"
        if func == 'asinh':
            self.current = math.asinh(ip)
        if func == 'acosh':
            if ip >= 1:
                self.current = math.acosh(ip)
            else:
                self.current = "acosh(x) is undefined for x < 1"
        if func == 'atanh':
            if -1 < ip < 1:
                self.current = math.atanh(ip)
            else:
                self.current = "atanh(x) is undefined for |x| >= 1"
        if func == 'acsch':
            if ip != 0:
                self.current = math.asinh(1 / ip)
            else:
                self.current = "acsch(0) is undefined"
        if func == 'asech':
            if 0 < ip <= 1:
                self.current = math.acosh(1 / ip)
            else:
                self.current = "asech(x) is undefined for x <= 0 or x > 1"
        if func == 'acoth':
            try:
                self.current = math.atanh(1 / ip)
            except ValueError:
                self.current = ""
                et.insert(0,"acoth(x) is undefined for x = 0, 1, or -1")
            except ZeroDivisionError:
                et.insert(0, "acoth(x) is undefined for x = 0, 1, or -1")
        self.display(self.current)

    def modx(self):
        self.result = False
        self.current = math.fabs(float(e.get()))
        self.display(self.current)

    def floorx(self):
        self.result = False
        self.current = math.floor(float(e.get()))
        self.display(self.current)

    def cielx(self):
        self.result = False
        self.current = math.ceil(float(e.get()))
        self.display(self.current)

    def random(self):
        self.result = False
        self.current = random.uniform(-1, 1)
        self.display(self.current)

    def todms(self):
        self.result = False
        decimal_degrees = (float(e.get()))
        degrees = int(decimal_degrees)
        minutes_full = (decimal_degrees - degrees) * 60
        minutes = int(minutes_full)
        seconds = (minutes_full - minutes) * 60
        self.display(f"{degrees}°{minutes}'{seconds:.3f}\"")


    def todeg(self):
        self.result = False
        dms = (float(e.get()))
        degrees = int(dms)
        papd = str(dms).split(".")
        minutes = papd[1][:2]
        seconds = papd[1][2:4]
        secdeci = papd[1][4:]
        self.current = eval(f'{degrees} + ({int(minutes)} / 60) + ({int(seconds)}.{int(secdeci)} / 3600)')
        self.display(self.current)


value = Calc(root)

et = tk.Entry(root,width=50, borderwidth=5, font=("Arial", 6, "italic"), bg = "#E0FFFF", fg = "#DB7093", justify="right")
et.grid(row=0, column=0, columnspan=5, rowspan=1, pady=1)
e = tk.Entry(root,width=23, borderwidth=5, font=("Arial", 15, "italic"), bg = "#E0FFFF", fg = "#DB7093", justify="right")
e.grid(row=1, column=0, columnspan=5, rowspan=2, pady=1)
e.insert(tk.END, 0)

numberpad = "789456123"
i = 0
button = []
for j in range(7,10):
    for k in range(1,4):
        button.append(tk.Button(root, width=3, height =1, font=("Helvetica", 15, 'bold'),bg = "#FFFFE0", fg = "#C71585", bd = 4, text = numberpad[i]))
        button[i].grid(row=j, column = k, padx =0,pady=1)
        button[i]['command'] = lambda x = numberpad[i]: value.numberEnter(x)
        i += 1


button_pi = tk.Button(root, text="\u03C0", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command=value.pi).grid(row=4, column=1, pady=1)
button_e = tk.Button(root, text="e", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command=value.e).grid(row=4, column=2, pady=1)
button_del1 = tk.Button(root, text= "\u232b", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command=value.Clear_Entry).grid(row=4, column=4, pady=1)
button_1divx = tk.Button(root, text="1/x", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command=value.onedivx).grid(row=5, column=1, pady=1)
button_modx = tk.Button(root, text="|x|", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command=value.modx).grid(row=5, column=2, pady=1)
button_exp = tk.Button(root, text="exp", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command =lambda: value.operation("10**")).grid(row=5, column=3, pady=1)
button_mod = tk.Button(root, text="mod", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command = lambda: value.operation("mod")).grid(row=5, column=4, pady=1)
button_openPar = tk.Button(root, text="(", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command = lambda: value.numberEnter("(")).grid(row=6, column=1, pady=1)
button_closePar = tk.Button(root, text=")", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command = lambda: value.numberEnter(")")).grid(row=6, column=2, pady=1)
button_decimal = tk.Button(root, text=".", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command = lambda: value.numberEnter(".")).grid(row=10, column=3, pady=1)
button_nfact = tk.Button(root, text="n!", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command=value.nfact).grid(row=6, column=3, pady=1)
button_plus_minus = tk.Button(root, text="+/-", width= 3, height=1,font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command=value.maths_plus_minus).grid(row=10, column=1, pady=1)
button_0 = tk.Button(root, text="0", width= 3, height=1, font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command = lambda: value.numberEnter(0)).grid(row=10, column=2, pady=1)
button_add = tk.Button(root, text="+", width= 3, height=1, font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command = lambda: value.operation("+")).grid(row=9, column=4, pady=1)
button_sub = tk.Button(root, text="-", width= 3, height=1, font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command = lambda: value.operation("-")).grid(row=8, column=4, pady=1)
button_mul = tk.Button(root, text="x", width= 3, height=1, font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command = lambda: value.operation("*")).grid(row=7, column=4, pady=1)
button_div = tk.Button(root, text="÷", width= 3, height=1, font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command = lambda: value.operation("/")).grid(row=6, column=4, pady=1)
button_equal = tk.Button(root, text="=", width= 3, height=1, font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command=value.sum_of_total).grid(row=10, column=4, pady=1)
button_comma = tk.Button(root, text=",", width= 3, height=1, font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command=lambda: value.numberEnter(",")).grid(row=12, column=4, pady=1)
button_clear = tk.Button(root, text= chr(67)+chr(69), width= 3, height=1, font =("Helvetica", 15, 'bold'),
                  bd = 4, bg = "#E6E6FA",command=value.all_Clear_Entry).grid(row=4, column=3, pady=1)


root.mainloop()

