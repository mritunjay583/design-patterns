class Main:
    def __init__(self):
        self._context = 'this is main'
        print('a')
        print('b')
        print('c')
        pass

    def run(self):
        print('x')
        print('A')
        print('B')
        print('c')
        print('D')
        print(self._context)


if __name__ == '__main__':
    main = Main()
    main.run()
