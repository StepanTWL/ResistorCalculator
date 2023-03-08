import struct

# Generate the CRC-32/JAMCRC lookup table
def generate_crc_table():
    crc_table = []
    for i in range(256):
        crc = i
        for j in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0xEDB88320
            else:
                crc >>= 1
        crc_table.append(crc)
    return crc_table

# Calculate the CRC-32/JAMCRC value of a given data using the lookup table
def crc32_jamcrc(data):
    crc_table = generate_crc_table()
    crc = 0xFFFFFFFF
    for byte in data:
        crc = (crc >> 8) ^ crc_table[(crc ^ byte) & 0xFF]
    return crc ^ 0xFFFFFFFF

# Example usage
data = b"0c 00 00 00 00 00 00 00"
crc = crc32_jamcrc(data)
print(hex(crc))
