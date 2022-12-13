from itertools import cycle
import base64
from filenkey import *

def main():
    rot13 = str.maketrans(
    'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
    'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    encodedkey = key.translate(rot13)
    print("The encoded key is: " + encodedkey)
    print("xor the key with the encoded text once you decode the key.")
    xor_flag(flag)

def xor_flag(aflag):
    aflag_bytes = aflag.encode("ascii")
    flag64_bytes = base64.b64encode(aflag_bytes)
    flag64_string = flag64_bytes.decode("ascii")
    xorflag = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in zip(flag64_string, cycle(key)))
    print("The encoded flag is: " + xorflag)
    print("You will also need to decode base64 when xoring with the key.")
    return xorflag
    
main()