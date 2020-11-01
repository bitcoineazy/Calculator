import re


def calc(var):
    a = {"один": 1, "два": 2, "три": 3, "четыре": 4, "пять": 5, "шесть": 6, "семь": 7, "восемь": 8,

         "девять": 9, "ноль": 0}

    b = {"десять": 10, "одиннадцать": 11, "двенадцать": 12, "тринадцать": 13, "четырнадцать": 14, "пятнадцать": 15,

         "шестнадцать": 16, "семнадцать": 17, "восемнадцать": 18, "девятнадцать": 19}

    c = {"двадцать": 20, "тридцать": 30, "сорок": 40, "пятьдесят": 50, "шестьдесят": 60, "семьдесят": 70,

         "восемьдесят": 80, "девяносто": 90}

    d = {100: "сто", 200: "двести", 300: "триста", 400: "четыреста", 500: "пятьсот", 600: "шестьсот", 700: "семьсот",

         800: "восемьсот", 900: "девятьсот"}
    th = {1: ['', "один", "два", 'три', 'четыре'],
          1000: ['тысяч ', 'одиа тысячя ', 'две тысячи ', 'три тысячи ', 'четыре тысячи '],
          1000000: ['миллионов ', 'один миллион', 'два миллиона ', 'три миллиона ', 'четыре миллиона '],
          1000000000: ['миллиардов ', 'один миллиард ', 'два миллиарда ', 'три миллиарда ', 'четыре миллиарда ']}

    def intg(a, b, c, d, th, var):
        kts = 1
        res = str()
        while var // kts:
            rch = (var % (kts * 1000)) // kts  # Делит число на тысячи

            if rch != 0:
                if rch % 100 > 19 or rch % 100 < 10:  # Проверка от 10 до 19

                    if rch % 10 > 0 and rch % 10 < 5:  # Проверка от 1 до 4

                        res = th[kts][rch % 10] + res

                    else:  # Проверка на оставшиеся значения
                        res = th[kts][0] + res

                        for k, v in a.items():  # Проверка цифр
                            if v == rch % 10 and rch % 10 not in [0, 1, 2, 3, 4]:
                                res = str(k) + " " + res

                    for k, v in c.items():  # Проверка десятков
                        if v == rch % 100 // 10 * 10:
                            res = str(k) + " " + res


                else:  # Проверка на значения от 10 до 19
                    res = th[kts][0] + res
                    for k, v in b.items():
                        if v == rch % 100:
                            res = str(k) + " " + res

                # if rch % 100 == 0 and rch//100 !=0:
                # res = th[kts][0]+res
                for k, v in d.items():  # Проверка сотен
                    if k == rch // 100 * 100:
                        res = str(v) + " " + res

            kts *= 1000
        return res

    def flo(a, b, c, d, th, var):
        des = {1: ' десятых', 3: ' тысячных', 4: ' десьтитысячных', 2: ' сотых', 5: ' стотысячных'}
        f = int(var)
        var = var - int(var)
        var = round(var, 4)
        var = str(var).replace("0.", '')
        vard = re.sub(r'^0+', '', var)
        rez = ""
        if vard == "":
            rez = intg(a, b, c, d, th, f)
        else:
            if f % 100 > 20 or f % 100 < 10:
                if f == 0:
                    rez = "ноль целых "
                if f % 10 == 1:
                    rez = "одна целая "
                    f -= 1
                elif f % 10 == 2:
                    rez = "две целых "
                    f -= 2
            if rez == "":

                rez = intg(a, b, c, d, th, f) + 'целых '
            else:
                rez = intg(a, b, c, d, th, f) + rez
            dopp = len(var)
            rez1 = ''

            vard = int(vard)
            if vard % 100 > 20 or vard % 100 < 10:
                if vard % 10 == 1:
                    rez1 = "одна"
                    var = var[0:len(var) - 1] + "0"
                elif vard % 10 == 2:
                    rez1 = "две"
                    var = var[0:len(var) - 1] + "0"
            var = re.sub(r'^0+', '', var)
            if var == "":
                var = 0
            var = int(var)
            rez = rez + intg(a, b, c, d, th, var) + rez1 + des[dopp]
        return rez

    def dd(s, b):  # Функция проверки и нахождния от 10 - 19

        for i in b:
            if i in s:
                return b[i]
        return 0

    def inp(s, a, b, c):  # Проверка от 0 - 9 и 20 - 99

        k = dd(s, b)  # Проверка от 10-19
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
            return "В словах допущена ошибка!"  # Ни одного сова не найдено - неверн введенные сова
        k += 1
        return k

    # def outp(var):
    #    if var

    if type(var) == str:
        var.strip()
        if re.search(r'[a-z]|[0-9]', var, re.I):
            return "Введен неверный символ"
        var = re.split(r'\s+', var)
        return inp(var, a, b, c)
    elif type(var) == int:
        return intg(a, b, c, d, th, var)
    elif type(var) == float:
        return flo(a, b, c, d, th, var)

var = 'девять целых одна десятых'
print(calc(var))