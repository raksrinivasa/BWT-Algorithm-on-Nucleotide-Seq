def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def burrows_wheeler_transform(line):
    line = '$' + line + '^'
    length = len(line)
    rotations = []

    for i in range(length):
        rotation = list(line) 
        for x in range(i):  
            element = rotation.pop(length-1)  
            rotation.insert(0, element)  
        rotations.append(''.join(rotation))  

    rotations.sort()
    bwt = ''.join(rotation[-1] for rotation in rotations)

    return bwt


def inverse_burrows_wheeler_transform(line):
    last_column = list(line)
    first_column = sorted(last_column)

    table = [''] * len(line)
    for x in range(len(line)):
        new_table = [''] * len(line)
        for i, c in enumerate(last_column):
            new_table[i] = c + table[i]
        table = sorted(new_table)

    for row in table:
        if row.endswith('^'):
            return row[1:-1]

def run_length_encoding(line):
    encoded = []
    count = 1
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{line[i - 1]}")
            count = 1
    encoded.append(f"{count}{line[-1]}")
    return ''.join(encoded)

def main():
    bwt_file_path = "/work2/07475/vagheesh/stampede2/forOthers/forBIO321G/bwt.txt"
    ibwt_file_path = "/work2/07475/vagheesh/stampede2/forOthers/forBIO321G/ibwt.txt"

    bwt_lines = read_file(bwt_file_path)
    ibwt_lines = read_file(ibwt_file_path)

    max_length = max(len(bwt_lines), len(ibwt_lines))

    for i in range(max_length):
        if i < len(bwt_lines):
            line = bwt_lines[i]
            bwt = burrows_wheeler_transform(line)
            bwt_rle = run_length_encoding(bwt)
            line_rle = run_length_encoding(line)
            print(f"{bwt}\n{line_rle}\n{bwt_rle}")
        if i < len(ibwt_lines):
            line = ibwt_lines[i]
            ibwt = inverse_burrows_wheeler_transform(line)
            print(f"{ibwt}")

if __name__ == "__main__":
    main()
