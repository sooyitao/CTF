with open('flag_dump.bin', 'rb') as f:
    data = f.read()
flags = [int.from_bytes(data[i*8:(i+1)*8], 'little') for i in range(40)]
print(flags)
