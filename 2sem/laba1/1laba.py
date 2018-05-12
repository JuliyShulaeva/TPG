import base64
import zlib
import sys


class IDecoding(object):
    def decode_it(self, stroka):
        pass


class PlainText(IDecoding):
    def __init__(self):
        pass

    def decoders(self, stroka):
        return stroka


class Base64(IDecoding):
    def __init__(self, stroka=None):
        self.stroka = stroka

    def decoders(self, stroka):
        new_str = base64.b64decode(stroka)
        return new_str.decode()


class ZipBase64(IDecoding):
    def __init__(self, stroka=None):
        self.stroka = stroka

    def decoders(self, stroka):
        base = base64.decodestring(stroka.encode())
        modified_base = zlib.decompress(base)
        return modified_base.decode()


specified_decoders = {'1': PlainText(), '2': Base64(), '3': ZipBase64()}

for n in sys.stdin:
    decoders_id = n[0]
    decoder = specified_decoders[decoders_id]
    answer = decoder.decoders(n[1:])
    print(answer.strip())
