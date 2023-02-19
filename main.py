from src.app import app

host = 'localhost'
port = 4000
debug = True

if(__name__ == '__main__'):
    app.run(host, port, debug)