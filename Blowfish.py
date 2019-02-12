from Crypto.Cipher import Blowfish


def pad(data):
 try:
  data = data.encode("utf-8")
 except:
  pass
 if (len(data) % 16) != 0:
  while True:
   if (len(data) % 16) == 0:
    break
   data += b"\x00"
 return data

def depad(data):
 return data.rstrip(b"\x00")


def encrypt(data, password):
 return Blowfish.new(password).encrypt(pad(data))
def decrypt(data, password):
 return depad(Blowfish.new(password).decrypt(data))

oke = encrypt("datadata", "pass")
print(oke)
print(decrypt(oke, "pass"))

