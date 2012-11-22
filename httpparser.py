from base64 import b64decode

class HttpParser():
    def __init__(self):
        ""
    def __repr__(self):
        return "HttpParser helper"
    def ParseHeaders(self, data):
        data = str(data)
        data = data.split('\r\n') #its going to hurt in case there is no both CR+LF
        header = {}
        for i in range(len(data)):
            line = data[i].split(': ')
            if len(str(line[0])): # prevent adding empty header
                key = str(line[0])
                value = str(line[1:][0])
                header[key] = value
        return header
    def HasHeader(self, header, headers):
        try:
            return str(headers[header])
        except KeyError:
            return ""
    def ParseB64Credentials(self, data):
        data = data.replace('Basic ', '') #leave only the B64 creds. 
        try: #short creds not decoded properly - investigate.
            cred = b64decode(data)
        except TypeError:
            cred = "unabletodecodeb64:" + data
        cred = cred.split(':')
        username = cred[0]
        password = cred[1]
        return username, password