import codecs


def create_table_crc32_bzip2_mpeg():
    a = []
    for i in range(256):
        k = i << 24
        for _ in range(8):
            k = (k << 1) ^ 0x4c11db7 if k & 0x80000000 else k << 1
        a.append(k & 0xffffffff)
    return a


def create_table_crc32_base_jamcrc():
    a = []
    for i in range(256):
        k = i
        for _ in range(8):
            k = (k >> 1) ^ 0xEDB88320 if k & 0x00000001 else k >> 1
        a.append(k)
    return a


def crc32_jamcrc(frame):
    crc_table = create_table_crc32_base_jamcrc()
    crc = 0xffffffff
    for byte in frame:
        crc = (crc >> 8) ^ crc_table[(crc ^ byte) & 0xFF]
    return crc & 0xFFFFFFFF


def crc32_mpeg(frame):
    crc_table = create_table_crc32_bzip2_mpeg()
    crc = 0xffffffff
    for byte in frame:
        crc = (crc << 8) ^ crc_table[((crc >> 24) ^ byte) & 0xFF]
    return crc & 0xFFFFFFFF


def crc32(frame):
    crc_table = create_table_crc32_base_jamcrc()
    crc = 0xffffffff
    for byte in frame:
        crc = (crc >> 8) ^ crc_table[(crc ^ byte) & 0xFF]
    return crc ^ 0xFFFFFFFF

def crc32_bzip2(frame):
    crc_table = create_table_crc32_bzip2_mpeg()
    crc = 0xffffffff
    for byte in frame:
        crc = (crc << 8) ^ crc_table[((crc >> 24) ^ byte) & 0xFF]
    return crc ^ 0xFFFFFFFF


def ascii_to_hex(s: str):
    s1 = bytes.fromhex(s).decode()
    return str.encode(s1)

s1 = hex(crc32_bzip2(ascii_to_hex('0c 00 00 00 00 00 00 00')))
s = str(hex(crc32_bzip2(ascii_to_hex('0c 00 00 00 00 00 00 00'))))[2:].zfill(8)
chunks = [s[i - 1:i + 1] for i in range(7, 0, -2)]
print(chunks)

"""
CRC-32 0c 00 00 00 00 00 00 00 - 0x328DCA26 - 26 CA 8D 32
CRC-32 0c - 0xDBB4A3A6 - A6 A3 B4 DB
width=32 poly=0x04c11db7 init=0xffffffff refin=true refout=true xorout=0xFFFFFFFF check=0xCBF43926 residue=0x00000000 name="CRC-32"
"""

"""
CRC-32/BZIP2 0c 00 00 00 00 00 00 00 - 0x2831F707 - 07 F7 31 28
CRC-32 0c - 0x84FBDB2F - 2F DB FB 84
width=32 poly=0x04c11db7 init=0xffffffff refin=false refout=false xorout=0xFFFFFFFF check=0xFC891918 residue=0x00000000 name="CRC-32/BZIP2"
"""

"""
CRC-32/MPEG-2 0c 00 00 00 00 00 00 00 - 0xD7CE08F8 - F8 08 CE D7
CRC-32/MPEG-2 0c - 0x7B0424D0 - D0 24 04 7B
width=32 poly=0x04c11db7 init=0xffffffff refin=false refout=false xorout=0x00000000 check=0x0376e6e7 residue=0x00000000 name="CRC-32/MPEG-2"
"""

"""
CRC-32/JAMCRC 0c 00 00 00 00 00 00 00 - 0xCD7235d9 - D9 35 72 CD
CRC-32/JAMCRC 0c - 0x244B5C59 - 59 5C 4B 24
width=32 poly=0x04c11db7 init=0xffffffff refin=true refout=true xorout=0x00000000 check=0x340BC6D9 residue=0x00000000 name="CRC-32/JAMCRC"
"""

"""
def crc32_mpeg(frame):
    crc_table = create_table_mgep()
    crc = 0xffffffff
    for byte in frame:
        lookup_index = ((crc >> 24) ^ byte) & 0xff
        crc = ((crc & 0xffffff) << 8) ^ crc_table[lookup_index]
    return crc & 0xFFFFFFFF
"""
