from lib.main import dec_app


@dec_app
def test(app, abc):
    print(app)
    print(abc)
