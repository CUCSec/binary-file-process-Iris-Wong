import struct
import os

def tamper(student_id):
    name=os.path.abspath(__file__)
    list_id=os.path.dirname(name)
    global full_id
    full_id=os.path.join(list_id,"lenna.bmp")
    f=open(full_id, "r+b")
    f.seek(54)
    for i in range(0,12):
        point=int(student_id[i])
        if point==0:
            point=10
        f.seek(point*3,1)
        f.write(bytes([0,0,0]))
        f.seek(-3,1)
    f.close()


def detect():
    with open(full_id, 'rb') as f:
        bmp_file_header = f.read(14)

        bm, size, r1, r2, offset = struct.unpack('<2sIHHI', bmp_file_header)

        f.seek(offset)

        count = 12
        offset = 0
        last_offset = 0
        while count > 0:
            color = f.read(3)

            if color == b'\x00\x00\x00':

                if offset - last_offset == 10:
                    print(0)
                else:
                    print(offset - last_offset)

                last_offset = offset
                count -= 1

            offset += 1


if __name__ == '__main__':
    import sys
    tamper(sys.argv[1])

    detect()