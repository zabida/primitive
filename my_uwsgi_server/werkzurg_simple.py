from werkzeug import Request, Response
from werkzeug.serving import run_simple


@Request.application
def app(env):
    print(env)
    print(env.method, type(env))
    return Response("200 OK!!")


run_simple("192.168.1.2", 5000, app)
