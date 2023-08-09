# class Archive:
#    __list_ar = []
#
#    def __init__(self, n:int, s:str):
#        self.n = n
#        self.s = s
#        self.list_arch_n = [i[0] for i in Archive.__list_ar]
#        self.list_arch_s = [i[1] for i in Archive.__list_ar]
#        Archive.__list_ar.append([n, s])
# if __name__ == '__main__':
#    a_1 = Archive(444, 'tty')
#    a_2 = Archive(555, 'hyn')
#    a_3 = Archive(777, 'iol')
#    print(a_3.list_arch_s, a_3.list_arch_n)


# или другой вариант

class Archive:
    _flag = None

    def __new__(cls, n, s):
        if cls._flag == None:
            cls._flag = super().__new__(cls)
            cls._flag.n = n
            cls._flag.s = s
            cls._flag.list_n = []
            cls._flag.list_s = []
            return cls._flag

        cls._flag.list_n.append(cls._flag.n)
        cls._flag.list_s.append(cls._flag.s)
        cls._flag.n = n
        cls._flag.s = s
        return cls._flag

    def __init__(self, n, s):
        self.s = s
        self.n = n


if __name__ == '__main__':
    a_1 = Archive(444, 'tty')
    a_2 = Archive(555, 'hyn')
    a_3 = Archive(777, 'iol')
    print(a_1.n)
