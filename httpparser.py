from base64 import b64decode

class HttpParser():
    def __init__(self):
        ""
    def __repr__(self):
        return "HttpParser helper"
    def ParseHeaders(self, data):
        data = str(data)
        data = data.split('\n')
        header = {}
        for i in range(len(data)):
            line = data[i].split(': ')
            key = str(line[0])
            value = str(line[1:])
            header[key] = value
        return header
    def HasHeader(self, header, headers):
        try:
            return str(headers[header])
        except KeyError:
            return ""
    def ParseB64Credentials(self, data):
        data = data.split(' ') #cut off the 'Basic ' prefix. TU JEST JAKIS BLAD!!!!!!! \r'] 
        data = data[1]
        try: #short creds not decoded properly - investigate.
            cred = b64decode(data)
        except TypeError:
            cred = "unabletodecodeb64:" + data
        cred = cred.split(':')
        username = cred[0]
        password = cred[1]
        return username, password