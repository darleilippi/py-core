from lib.main import dec_app
from lib.tests.test2 import test


@dec_app
def main(app):
    print("Test 1")
    print("Test 12")
    print("Test 13")

    print(app)

    test('ABC')


if __name__ == '__main__':
    main()
