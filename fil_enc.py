# DEVA THAKUR BOLTI PUBLIC 
import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))