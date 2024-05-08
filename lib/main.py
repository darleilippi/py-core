import sys
import io
import builtins


class PrintWrapper(io.StringIO):
    def __call__(self, *args, **kwargs):
        # Pass the object instance (self) as the file
        sys.stdout.write("Wrapper: " + str(args[0]) + '\n')
        return builtins.print(*args, file=self, **kwargs)


class WebSocketClient():
    def __init__(self) -> None:
        sys.stdout.write('Instanciado\n')

    def send(self):
        return 'Sended'


class Application():
    print_wrapper = None
    websocket_client = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Application, cls).__new__(cls)
            cls.websocket_client = WebSocketClient()
            cls.print_wrapper = PrintWrapper()

        return cls.instance


def dec_app(func):
    app = Application()

    def closure(*args, **kwargs):
        return func(app, *args, **kwargs)

    return closure
