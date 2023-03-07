import codecs


def create_table_mgep():
    a = []
    for i in range(256):
        k = i << 24
        for _ in range(8):
            k = (k << 1) ^ 0x4c11db7 if k & 0x80000000 else k << 1
        a.append(k & 0xffffffff)
    return a


def create_table_jamcrc():
    a = []
    for i in range(256):
        k = i
        for _ in range(8):
            k = (k >> 1) ^ 0xEDB88320 if k & 0x00000001 else k >> 1
        a.append(k)
    return a

#1499220772
def crc32_jamcrc(frame):
    crc_table = create_table_jamcrc()
    crc = 0xffffffff #3679149222 - 0xDB4B5CA6
    for byte in frame:
        lookup_index = ((crc >> 24) ^ byte) & 0xff
        #crc = (crc >> 8) ^ crc_table[lookup_index]
        crc = ((crc & 0xffffff) << 8) ^ crc_table[lookup_index]
    return crc


def crc32_mpeg(frame):
    crc_table = create_table_mgep()
    crc = 0xffffffff
    for byte in frame:
        lookup_index = ((crc >> 24) ^ byte) & 0xff
        crc = ((crc & 0xffffff) << 8) ^ crc_table[lookup_index]
    return crc


def hex_to_ascii(s: str):
    s1 = bytes.fromhex(s).decode()
    return str.encode(s1)


print(hex(crc32_jamcrc(hex_to_ascii('0c 00 00 00 00 00 00 00'))))

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