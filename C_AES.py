
class AES_Crypto:
    def __init__(self, sandi, mod, iv):
        mode = [AES.MODE_CBC, AES.MODE_OFB, AES.MODE_CFB]
        self.aes = AES.new(sandi, mode[mod], iv)
    def encrypt(self, data):
        try:
            data = data.encode("utf-8")
        except:
            pass
        if (len(data) % 16) != 0:
            while True:
                if (len(data) % 16) == 0:
                    break
                data += b"\x00"
        data = self.aes.encrypt(data)
        return data
    def decrypt(self, data):
        data = self.aes.decrypt(data)
        data = data.rstrip(b"\x00")
        return data


