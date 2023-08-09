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
if __name__ == '__main__':
    help(Archive)