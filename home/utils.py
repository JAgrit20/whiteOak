from Crypto.Cipher import AES
import hashlib
from binascii import hexlify, unhexlify
import base64, re
from Crypto.Cipher import AES
from Crypto import Random
from django.conf import settings

def pad(data):

    """
    ccavenue method to pad data.
    :param data: plain text
    :return: padded data.
    """

    length = 16 - (len(data) % 16)
    data += chr(length)*length
    return data


def unpad(data):

    """
    ccavenue method to unpad data.
    :param data: encrypted data
    :return: plain data
    """
    
    return data[0:-data[-1]]

from Crypto.Cipher import AES
import hashlib
import binascii

from binascii import hexlify, unhexlify

def pad(data):
    length = 16 - (len(data) % 16)
    data += bytes([length]) * length
    return data

def encrypt(plainText,workingKey):
    iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    plainText = pad(plainText.encode())
    encDigest = hashlib.md5()
    encDigest.update(workingKey.encode())
    enc_cipher = AES.new(encDigest.digest(), AES.MODE_CBC, iv)
    encryptedText = hexlify(enc_cipher.encrypt(plainText))
    return encryptedText.decode()

def decrypt(cipherText, workingKey):
    iv = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    decDigest = hashlib.md5()
    decDigest.update(workingKey.encode())
    cipherText = binascii.unhexlify(cipherText.encode())
    dec_cipher = AES.new(decDigest.digest(), AES.MODE_CBC, iv)
    decryptedText = dec_cipher.decrypt(cipherText)
    return decryptedText.rstrip(bytes([decryptedText[-1]])).decode('latin-1')


