import time

# 指定html所在的路径
g_templates_root = "./templates"


def index(file_name):
    
    # ./templates/index.py
    # ./templates/index.html
    file_name = file_name.replace(".py", ".html")
    try:
        f = open(g_templates_root+file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read() 
        f.close()

        return content


def center(file_name):
    file_name = file_name.replace(".py", ".html")
    try:
        f = open(g_templates_root+file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read() 
        f.close()

        return content


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    # 取出浏览器传递给web服务器的url中的 请求资源路径
    # /a/b/c/index.py
    file_name = environ['PATH_INFO']    
    if file_name == "/index.py":
        return index(file_name)
    elif file_name == "/center.py":
        return center(file_name) 
    else:
        return str(environ) + '==404----->%s\n' % time.ctime()
