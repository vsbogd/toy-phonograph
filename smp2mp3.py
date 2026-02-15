import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='smp2mp3',
                 description='Decode/encode .smp files from the toy phonograph')
    parser.add_argument('input_file', help='.smp to decode, .mp3 to encode')
    parser.add_argument('output_file', help='.mp3 to decode, .smp to encode')
    args = parser.parse_args()
    with open(args.input_file, "rb") as input:
        with open(args.output_file, "wb") as output:
            while True:
                data = bytearray(input.read(4096))
                if not data:
                    break
                for i in range(len(data)):
                    data[i] ^= 0x88
                output.write(data)


