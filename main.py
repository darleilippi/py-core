import sys
import io
import builtins


class PrintWrapper(io.StringIO):
    def __call__(self, *args, **kwargs):
        # Pass the object instance (self) as the file
        sys.stdout.write("Wrapper: " + str(args[0]) + '\n')
        Application.class_function()
        return builtins.print(*args, file=self, **kwargs)


class WebSocketClient():
    def __init__(self) -> None:
        sys.stdout.write('Instanciado\n')

    def send(self):
        return 'Sended'


class Application():

    print_wrapper = PrintWrapper()
    websocket_client = WebSocketClient()

    def __init__(self) -> None:
        pass

    @classmethod
    def class_function(cls):
        sys.stdout.write(cls.websocket_client.send() + '\n')

    def run(self, func):
        func()

        sys.stdout.write('\nOutput: \n' + self.print_wrapper.getvalue())


print = Application.print_wrapper
