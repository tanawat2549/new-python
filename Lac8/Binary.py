import struct
record = (1, 'john Doe', 20 , 3.5)
with open("records.dat", "wb") as file:
    data = struct.pack('i20sif', record [0], record[1].encode('utf-8'), record[2], record[3])
    file.write(data)
