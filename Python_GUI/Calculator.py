import tkinter as tk


class Calculator:

    def op_plus(self):
        print('Plus button clicked')

    def op_minus(self):
        print('Minus button clicked')

    def op_multiply(self):
        print('Multiply button clicked')

    def op_divide(self):
        print('Divide button clicked')

    def op_percentile(self):
        print('Percentile button clicked')

    def op_CE(self):
        print('CE button clicked')

    def op_clear(self):
        print('C button clicked')

    def op_backspace(self):
        print('Backspace button clicked')

    def op_dot(self):
        print('. button clicked')

    def op_equal(self):
        print('= button clicked')

    def addNum1(self):
        print('Button 1 clicked')

    def addNum2(self):
        print('Button 2 clicked')

    def addNum3(self):
        print('Button 3 clicked')

    def addNum4(self):
        print('Button 4 clicked')

    def addNum5(self):
        print('Button 5 clicked')

    def addNum6(self):
        print('Button 6 clicked')

    def addNum7(self):
        print('Button 7 clicked')

    def addNum8(self):
        print('Button 8 clicked')

    def addNum9(self):
        print('Button 9 clicked')

    def addNum0(self):
        print('Button 0 clicked')



window = tk.Tk()
window.title('Python Basic Calculator')

obj = Calculator()
frame_label = tk.Frame(master=window)
frame_label.pack(fill=tk.X, side=tk.TOP)
frame_1 = tk.Frame(master=window)
frame_1.pack(fill=tk.X, side=tk.LEFT)
frame_2 = tk.Frame(master=window)
frame_2.pack(fill=tk.X, side=tk.LEFT)
frame_3 = tk.Frame(master=window)
frame_3.pack(fill=tk.X, side=tk.LEFT)
frame_4 = tk.Frame(master=window)
frame_4.pack(fill=tk.X, side=tk.LEFT)
frame_5 = tk.Frame(master=window)
frame_5.pack(fill=tk.X, side=tk.LEFT)

entry = tk.Entry(master=frame_label, width=38)
entry.insert(0, 0)
entry.pack()
"""
but_1 = tk.Button(master=frame_1, text='1', width=7, height=2, command=obj.addNum1)
but_1.pack()
but_2 = tk.Button(master=frame_2, text='2', width=7, height=2, command=obj.addNum2)
but_2.pack()
but_3 = tk.Button(master=frame_3, text='3', width=7, height=2, command=obj.addNum3)
but_3.pack()
but_4 = tk.Button(master=frame_1, text='4', width=7, height=2, command=obj.addNum4)
but_4.pack()
but_5 = tk.Button(master=frame_2, text='5', width=7, height=2, command=obj.addNum5)
but_5.pack()
but_6 = tk.Button(master=frame_3, text='6', width=7, height=2, command=obj.addNum6)
but_6.pack()
but_7 = tk.Button(master=frame_1,text='7', width=7, height=2, command=obj.addNum7)
but_7.pack()
but_8 = tk.Button(master=frame_2, text='8', width=7, height=2, command=obj.addNum8)
but_8.pack()
but_9 = tk.Button(master=frame_3, text='9', width=7, height=2, command=obj.addNum9)
but_9.pack()

but_baksp = tk.Button(master=frame_1, text='cls', width=7, height=2, command=obj.op_backspace)
but_baksp.pack()
but_0 = tk.Button(master=frame_2, text='0', width=7, height=2, command=obj.addNum0)
but_0.pack()
but_dot = tk.Button(master=frame_3, text='.', width=7, height=2, command=obj.op_dot)
but_dot.pack()
but_equal = tk.Button(master=frame_4, text='=', width=7, height=2, command=obj.op_equal)
but_equal.pack()

but_plus = tk.Button(master=frame_4, text='+', width=7, height=2, command=obj.op_plus)
but_plus.pack()
but_minus = tk.Button(master=frame_4, text='-', width=7, height=2, command=obj.op_minus)
but_minus.pack()
but_mult = tk.Button(master=frame_4, text='X', width=7, height=2, command=obj.op_multiply)
but_mult.pack()


but_prcnt = tk.Button(master=frame_1, text='%', width=7, height=2, command=obj.op_percentile)
but_prcnt.pack()
but_CE = tk.Button(master=frame_2, text='CE', width=7, height=2, command=obj.op_CE)
but_CE.pack()
but_C = tk.Button(master=frame_3, text='C', width=7, height=2, command=obj.op_clear)
but_C.pack()
but_divid = tk.Button(master=frame_4, text='÷', width=7, height=2, command=obj.op_divide)
but_divid.pack()
"""
but_prcnt = tk.Button(master=frame_1, text='%', width=7, height=2, command=obj.op_percentile)
but_prcnt.pack()
but_CE = tk.Button(master=frame_2, text='CE', width=7, height=2, command=obj.op_CE)
but_CE.pack()
but_C = tk.Button(master=frame_3, text='C', width=7, height=2, command=obj.op_clear)
but_C.pack()
but_baksp = tk.Button(master=frame_4, text='cls', width=7, height=2, command=obj.op_backspace)
but_baksp.pack()

but_7 = tk.Button(master=frame_1,text='7', width=7, height=2, command=obj.addNum7)
but_7.pack()
but_8 = tk.Button(master=frame_2, text='8', width=7, height=2, command=obj.addNum8)
but_8.pack()
but_9 = tk.Button(master=frame_3, text='9', width=7, height=2, command=obj.addNum9)
but_9.pack()
but_mult = tk.Button(master=frame_4, text='X', width=7, height=2, command=obj.op_multiply)
but_mult.pack()

but_4 = tk.Button(master=frame_1, text='4', width=7, height=2, command=obj.addNum4)
but_4.pack()
but_5 = tk.Button(master=frame_2, text='5', width=7, height=2, command=obj.addNum5)
but_5.pack()
but_6 = tk.Button(master=frame_3, text='6', width=7, height=2, command=obj.addNum6)
but_6.pack()
but_minus = tk.Button(master=frame_4, text='-', width=7, height=2, command=obj.op_minus)
but_minus.pack()

but_1 = tk.Button(master=frame_1, text='1', width=7, height=2, command=obj.addNum1)
but_1.pack()
but_2 = tk.Button(master=frame_2, text='2', width=7, height=2, command=obj.addNum2)
but_2.pack()
but_3 = tk.Button(master=frame_3, text='3', width=7, height=2, command=obj.addNum3)
but_3.pack()
but_plus = tk.Button(master=frame_4, text='+', width=7, height=2, command=obj.op_plus)
but_plus.pack()

but_divid = tk.Button(master=frame_1, text='÷', width=7, height=2, command=obj.op_divide)
but_divid.pack()
but_0 = tk.Button(master=frame_2, text='0', width=7, height=2, command=obj.addNum0)
but_0.pack()
but_dot = tk.Button(master=frame_3, text='.', width=7, height=2, command=obj.op_dot)
but_dot.pack()
but_equal = tk.Button(master=frame_4, text='=', width=7, height=2, command=obj.op_equal, bg="blue")
but_equal.pack()



window.mainloop()