import time


class MyStr(str):
    def __new__(cls, st, author_s_name):
        instance = super().__new__(cls, st)
        instance.author_s_name = author_s_name
        instance.time_now = time.strftime("%H:%M:%S", time.localtime())
        return instance
    def __init__(self, st, author_s_name):
        self.st = st
        self.author_s_name = author_s_name




if __name__ == '__main__':
    m_1 = MyStr('Я люблю ', 'парень')
    m_2 = MyStr('python', 'парень')
    m_3 = m_1 + m_2
    print(m_3)
    print(m_1.time_now)