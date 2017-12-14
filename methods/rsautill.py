# use/bin/env python3
#-*-coding:utf-8-*-
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64
import os
random_generator=Random.new().read
'''
公钥加密
'''
def encryptbypublic(str,publickeypath):
    str=str.encode(encoding="utf-8")
    with open(publickeypath) as f:
        key = f.read()

        rsakey = RSA.importKey(key)

        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(str))
    return cipher_text

'''
私钥解密
'''
def decryptbyprivatekey(str,privatekeypath):
    #str=str.encode("utf-8")
    with open(privatekeypath) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(base64.b64decode(str), random_generator)
    return text

'''
私钥加密
'''
def encryptbyprivate(str,privatekeypath):

    str=str.encode(encoding="utf-8")
    with open(privatekeypath) as f:
        key = f.read()

        rsakey = RSA.importKey(key)

        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = base64.b64encode(cipher.encrypt(str))
    return cipher_text

'''
with open('publicKey.pem') as f:
    key = f.read()
    rsakey = RSA.importKey(key)
    print(rsakey)
    cipher = Cipher_pkcs1_v1_5.new(rsakey)
    text1 = cipher.decrypt(base64.b64decode(cipher_text1), random_generator)
print(text1)
'''
def dosign(str,privatekeypath):
    str=str.encode(encoding="utf-8")
    with open(privatekeypath) as f:
        key = f.read()
        rsakey = RSA.importKey(key)
        signer = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        digest.update(str)
        sign = signer.sign(digest)
        signature = base64.b64encode(sign)
    return signature

def is_verify(str,publickeypath,signature):
    str=str.encode("utf-8")
    with open(publickeypath) as f:#读取公钥
        key = f.read()
        rsakey = RSA.importKey(key)
        verifier = Signature_pkcs1_v1_5.new(rsakey)
        digest = SHA.new()
        # Assumes the data is base64 encoded to begin with
        digest.update(str)
        is_verify = verifier.verify(digest, base64.b64decode(signature))
    return is_verify


if __name__=="__main__":
    str="ueirhfuhufhwuihdei"
    str1="hweuhuiwdhuiwedh"
    path=os.path.abspath("publicKey.pem")
    a=encryptbypublic(str,"publicKey.pem")
    print(decryptbyprivatekey(a,"privateKey.pem"))





















