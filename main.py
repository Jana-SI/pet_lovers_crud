from src.app import app

host = 'localhost'
port = 4000
debug = true

if(__name__ == '__main__'):
    app.run(host, port, debug)