from main import Application, print

from test2 import test2


def main():
    print("Test 1")
    print("Test 12")
    print("Test 13")

    test2()


if __name__ == '__main__':
    app = Application()
    app.run(main)
