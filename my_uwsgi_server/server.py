import socket
import sys
import traceback

listener = socket.socket()
listener.setsockopt(socket.SOL_SOCKET,
                    socket.SO_REUSEADDR, 1)
listener.bind(('0.0.0.0', 8080))
listener.listen(1)
print('Serving HTTP on 0.0.0.0 port 8080 ...')

while True:
    try:
        client_connection, client_address = \
            listener.accept()
        print(f'Server received connection'
              f' from {client_address}')
        request = client_connection.recv(1024)
        print(f'request we received: {request}')

        headers_set = None


        def start_response(status, headers):
            global headers_set
            headers_set = [status, headers]


        method, path, _ = request.split(b' ', 2)
        environ = {'REQUEST_METHOD': method.decode('utf-8'),
                   'PATH_INFO': path.decode('utf-8'),
                   'wsgi.version': (1, 0),
                   'wsgi.url_scheme': 'http',
                   'wsgi.input': request,
                   'wsgi.errors': sys.stderr,
                   'wsgi.multithread': False,
                   'wsgi.multiprocess': False,
                   'wsgi.run_once': False,
                   'SERVER_NAME': '127.0.0.1',
                   'SERVER_PORT': '8080',}
        from app import simple_app

        app_result = simple_app(environ, start_response)

        response_status, response_headers = headers_set
        response = f'HTTP/1.1 {response_status}\r\n'
        for header in response_headers:
            response += f'{header[0]}: {header[1]}\r\n'
        response += '\r\n'
        response = response.encode('utf-8')
        for data in app_result:
            response += data

        client_connection.sendall(response)
        client_connection.close()
    except:
        traceback.print_exc()