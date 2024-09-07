import sys

def find_sequences(file_path):
    # The sequence we're looking for, in bytes
    #target_sequence = b'\x73\x12\xcc'
    target_sequence = b'\x91\x7c\x29'

    with open(file_path, 'rb') as file:
        # Read the entire file content
        content = file.read()

        # Find all occurrences of the target sequence
        start = 0
        while True:
            start = content.find(target_sequence, start)
            if start == -1:  # No more occurrences
                break

            # Get the length byte (the byte after the sequence)
            length_byte = content[start + len(target_sequence)]

            # Extract the specified number of bytes
            extracted = content[start + len(target_sequence) + 1:start + len(target_sequence) + 1 + length_byte]

            # Decode the bytes to ASCII, replacing non-printable characters
            try:
                print(extracted.decode('ascii', errors='replace'))
            except UnicodeDecodeError:
                print(''.join([chr(b) if 32 <= b < 127 else '?' for b in extracted]))

            # Move past this occurrence
            start += len(target_sequence) + 1 + length_byte

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <filename>")
        sys.exit(1)

    find_sequences(sys.argv[1])
