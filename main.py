class Main:
    def __init__(self):
        self._context = 'this is main'
        print('a')
        pass

    def run(self):
        print(self._context)


if __name__ == '__main__':
    main = Main()
    main.run()
