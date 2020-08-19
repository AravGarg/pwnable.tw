from pwn import *
elf=ELF('./silver_bullet')
print(hex(elf.symbols["puts"]))
print(hex(elf.got["puts"]))
print(hex(elf.symbols["_start"]))

