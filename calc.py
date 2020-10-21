from tkinter import *
import re




class Example(Frame):
    m = {"плюс": ["+", 0], "минус": ["-", 1], "делить": ["/", 2], "умножить": ["*", 3], "на": ["*", 3]}
    a = {"один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
         "ноль": 0}
    b = {"десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
         "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19}
    c = {"двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70,
         "восемьдесят": 80,
         "девяносто": 90}

    def __init__(self, parent):
        Frame.__init__(self, parent, background="white")
        self.parent = parent
        self.parent.title("Калькулятор")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.initUI()

    def initUI(self):
        self.entry = Entry(self, width=50)
        self.entry.grid(row=0, columnspan=4)
        self.button_plus = Button(self, text='плюс')
        self.button_plus.grid(row=1, column=0)
        self.button_minus = Button(self, text='минус')
        self.button_minus.grid(row=1, column=1)
        self.button_multiply = Button(self, text='умножить')
        self.button_multiply.grid(row=1, column=2)
        self.button_erase = Button(self, text='очистить')
        self.button_erase.grid(row=1,column=3)
        self.button_equally = Button(self, text='равно')
        self.button_equally.grid(row=2, column=2)
        self.button_cnk = Button(self, text='C из n по k')
        self.button_cnk.grid(row=2, column=3)
        self.button_division = Button(self, text='делить')
        self.button_division.grid(row=2, column=1)
        self.pack()
        self.button_erase.bind('<Button-1>', self.button_erase_clicked)
        self.button_plus.bind('<Button-1>', self.button_plus_clicked)
        self.button_minus.bind('<Button-1>', self.button_minus_clicked)
        self.button_multiply.bind('<Button-1>', self.button_multiply_clicked)
        self.button_division.bind('<Button-1>', self.button_division_clicked)
        self.button_cnk.bind('<Button-1>', self.button_cnk_clicked)
        self.button_equally.bind('<Button-1>', self.button_equally_clicked)

    def button_erase_clicked(self, event):
        print('очистились')
        self.entry.delete(0, END)

    def button_plus_clicked(self, event):
        print('плюс')
        self.entry.insert(END, ' плюс ')

    def button_minus_clicked(self, event):
        print('минус')
        self.entry.insert(END, ' минус ')

    def button_multiply_clicked(self, event):
        print('умножить')
        self.entry.insert(END, ' умножить ')

    def button_division_clicked(self, event):
        print('поделили')
        self.entry.insert(END, ' делить ')

    def button_cnk_clicked(self, event):
        print('c из n по k')
        self.entry.delete(0, END)
        self.entry.insert(END, ' C из n=  по k= ')

    def button_equally_clicked(self, event):
        print('равно')
        if 'C из' in self.entry.get():
            str = self.entry.get()
            str_com = str.split()
            c = []
            for var in str_com:
                if var.isdigit():
                    c.append(var)
            print(c)
            print(self.entry.get())
            n = int(c[0])
            k = int(c[1])
            if 0 <= k <= n:
                nn = 1
                kk = 1
                for t in range(1, min(k, n-k)+1):
                    nn *= n
                    kk *= t
                    n -= 1
                self.entry.delete(0, END)
                self.entry.insert(0, nn // kk)
                print(nn // kk)
            else:
                self.entry.delete(0, END)
                self.entry.insert(0, '0')
        if 'плюс' or 'минус' or 'умножить' in self.entry.get():
            s = self.entry.get()
            s.strip()
            ind = 0
            s1, s2 = (1, 1)
            res = int()
            s = re.split(r'\s', s)
            for i in range(len(s)):
                if s[i] in self.m:
                    ind = i
            s1 = self.inp(s[:ind])
            s2 = self.inp(s[ind + 1:])

            self.entry.insert(END, res)
                #s = input()
                #s.strip()

    def inp(self, s):

        # if re.search(r'[a-z]|[0-9]', s,re.I):
        #    return "Введен неверный символ"
        k = self.dd(s)
        if k > 0:
            return k
        k = -1
        for i in self.c:
            if i in s:
                k += c[i]
                break
        for i in self.a:
            if i in s:
                k += self.a[i]
                break
        if k == -1:
            return "Введено неверные числа"
        k += 1
        return k

    def output1(self):
        s = self.entry.get()
        ind = 0
        s1 = self.inp(s[:ind])
        s2 = self.inp(s[ind + 1:])
        if self.m[s[ind]][1] == 0:
            print(s1 + s2)
            self.entry.insert(END, (s1+s2))
            return s1 + s2
        if self.m[s[ind]][1] == 1:
            print(s1 - s2)
            return s1 - s2
        if self.m[s[ind]][1] == 2:
            print(s1 / s2)
            return s1 / s2

        if self.m[s[ind]][1] == 3:
            print(s1 * s2)
            return s1 * s2


    def dd(self, s):
        for i in self.b:
            if i in s:
                print(b[i])
                return b[i]
        return 0

    def centerWindow(self):
        w = 390
        h = 150

        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


def main():
    root = Tk()
    ex = Example(root)
    root.mainloop()

class Calculator(Example):
    def dd(self, s):
        for i in self.b:
            if i in s:
                print(b[i])
                return b[i]
        return 0
if __name__ == '__main__':
    main()

m = {"плюс": ["+", 0], "минус": ["-", 1], "делить": ["/", 2], "умножить": ["*", 3], "на": ["*", 3]}
a = {"один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "ноль": 0}
b = {"десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
     "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19}
c = {"двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80,
     "девяносто": 90}


def dd(s):
    global b
    for i in b:
        if i in s:
            return b[i]
    return 0

def output1():
    global m, s, s1, s2
    if m[s[ind]][1] == 0:
        return s1 + s2
    if m[s[ind]][1] == 1:
        return s1 - s2
    if m[s[ind]][1] == 2:
        return s1 / s2
    if m[s[ind]][1] == 3:
        return s1 * s2

def inp(s):
    global a, b
    # if re.search(r'[a-z]|[0-9]', s,re.I):
    #    return "Введен неверный символ"
    k = dd(s)
    if k > 0:
        return k
    k = -1
    for i in c:
        if i in s:
            k += c[i]
            break
    for i in a:
        if i in s:
            k += a[i]
            break
    if k == -1:
        return "Введено неверные числа"
    k += 1
    return k

s = input()
s.strip()
ind = 0
s1, s2 = (1, 1)
res = int()
while s != "кон" and s != "end":
    s = re.split(r'\s', s)
    if len(s) > 4 or len(s) < 2:
        print("Смотрите шаблон ввода")
        s = input()
        s.strip()
        continue
    for i in range(len(s)):
        if s[i] in m:
            ind = i
    if ind == 0:
        print("Смотрите шаблон ввода")
        s = input()
        s.strip()
        continue
    s1 = inp(s[:ind])
    s2 = inp(s[ind + 1:])
    res = output1()
    print(inp(s[:ind]), m[s[ind]][0], inp(s[ind + 1:]), "=", res)
    print("Ответ: ", res)
    s = input()
    s.strip()