#!/usr/bin/env python2
#
# Httpthief PoC.
# author: Slawomir Rozbicki (httpthief@rozbicki.eu)
# GPL v3. 
# !!Change dir to directory with bitmap!!

from BaseHTTPServer import HTTPServer
from thiefhandler import ThiefHandler

port = 80

def main():
    try:
        server = HTTPServer(('', port), ThiefHandler)
        print 'Welcome to the HttpThief, listening on %d/TCP...' % port
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()