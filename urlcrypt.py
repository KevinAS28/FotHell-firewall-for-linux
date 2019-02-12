import urllib.parse
#print(urllib.parse.unquote("oke%20%2B%20wow"))
def encrypt(data):
        return urllib.parse.quote(data)
def decrypt(data):
        return urllib.parse.unquote(data)

