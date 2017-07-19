from bottle import route, run, template, request
from bottle import redirect
import os
from operator import itemgetter

@route('/<path>')
def manager(path):
    cur_path = path.replace('--', '/')
    files = dirs = []
    if os.path.exists(cur_path):
        for dirpath, dirnames, filenames in os.walk(cur_path):
            dirs = dirnames
            for dir in dirnames:
                pass
            for f in filenames:
                fp = os.path.join(dirpath, f)
                size = os.path.getsize(fp)
                files.append((f, size))
            break
        dirs.sort(key=lambda x: x[0])
        files.sort(key=lambda x: x[0])
        path_back = path[:path.rindex('--')] if cur_path.replace('/', '\\') != os.getcwd() else ''
        return template('manager', path=path, path_back=path_back, dirs=dirs, files=files)
    else:
        return template('fail')

@route('/')
def start():
    path = os.getcwd().replace('\\', '--')
    return redirect('/{}'.format(path))

run(host='localhost', port=8080)