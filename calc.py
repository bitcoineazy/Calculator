from tkinter import *
import re




class Example(Frame):

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
        button_plus = Button(self, text='плюс')
        button_plus.grid(row=1, column=0)
        button_minus = Button(self, text='минус')
        button_minus.grid(row=1, column=1)
        button_multiply = Button(self, text='умножить')
        button_multiply.grid(row=1, column=2)
        self.button_erase = Button(self, text='очистить')
        self.button_erase.grid(row=1,column=3)
        button_equally = Button(self, text='равно')
        button_equally.place()
        self.button_erase.bind('<Button-1>', self.button_erase_clicked)
        self.pack()



    def button_erase_clicked(self, event):
        print('очистились')
        self.entry.delete(0, END)


    def calc(self, input):
        if input == 'равно':
            input_str = r'\D+'


    def centerWindow(self):
        w = 290
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


if __name__ == '__main__':
    main()

m = {"плюс": ["+", 0], "минус": ["-", 1], "делить": ["/", 2], "умножить": ["*", 3], "на": ["*", 3]}
a = {"один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9, "ноль": 0}
b = {"десять": 10, "одиyнадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,
     "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19}
c = {"двадцать": 20, "тридцать": 30, "сорок": 40, "дтьдесят": 50, "шестьдесят": 60, "семьдесят": 70, "восемьдесят": 80,
     "десяносто": 90}


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