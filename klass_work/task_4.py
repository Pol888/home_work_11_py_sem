class Archive:
    '''сохраняет в себя данные'''
    _flag = None

    def __new__(cls, n, s):
        """Если класс не был создан - создается экземляр, если ранее это происходило то создается новая ссылка
        где прошлые данные находятся в архиве, а новые являются свойсвами"""
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
        '''hello'''
        self.s = s
        self.n = n
    def __str__(self):
        return 'Класс Archive'

    def __repr__(self):
        return f'Archive({self.n=}, {self.s=}, {self.list_n=}, {self.list_s=}'


if __name__ == '__main__':
    a_1 = Archive(444, 'tty')
    a_2 = Archive(555, 'hyn')
    a_3 = Archive(777, 'iol')
    print(a_3)
    print([a_1, a_2, a_3])