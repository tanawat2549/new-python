import struct
record_format = 'i20sif'
record_size = struct.calcsize(record_format)
with open("records.dat", "rb") as file:
    file.seek(record_size * 2)
    data = file.read(record_size)
    if data:
        record = struct.unpack(record_format, data)
        record = (record[0], record[1].decode('utf-8').rstrip('\x00'), record[2], record[3])
        print(f"ID: {record[0]}, Name: {record[1]}, Age: {record[2]}, GPA: {record[3]}")