import struct
with open("records.dat", "rb") as file:
    record_size = struct.calcsize('i20sif')
    while True:
        data = file.read(record_size)
        if not data:
            break
    record = struct.unpack('i20sif', data)
    record = (record[0], record[1].decode('utf-8').rstrip('\x00'), record[2], record[3])
   