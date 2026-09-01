#!/usr/bin/env python3
"""Tokenize text using GPT-2 BPE and output binary token IDs.

Usage:
    python tokenize.py "text to tokenize" -o tokens.bin
    echo "text" | python tokenize.py - -o tokens.bin
    python tokenize.py -f input.txt -o tokens.bin

The binary format is:
    4 bytes: magic "TKID"
    4 bytes: number of tokens (uint32 LE)
    N * 4 bytes: token IDs (int32 LE)
"""

import sys
import struct
import argparse

def main():
    parser = argparse.ArgumentParser(description='Tokenize text to binary IDs')
    parser.add_argument('text', nargs='?', default=None, help='Text to tokenize (use - for stdin)')
    parser.add_argument('-f', '--file', help='Read text from file')
    parser.add_argument('-o', '--output', default='tokens.bin', help='Output binary file')
    parser.add_argument('--print-ids', action='store_true', help='Print token IDs to stdout')
    parser.add_argument('--decode', action='store_true', help='Read binary file and decode token IDs')
    args = parser.parse_args()

    try:
        import tiktoken
        enc = tiktoken.get_encoding('gpt2')
    except ImportError:
        print("ERROR: tiktoken not installed. Run: pip install tiktoken", file=sys.stderr)
        sys.exit(1)

    if args.decode:
        # Read binary and print token IDs
        with open(args.output, 'rb') as f:
            magic = f.read(4)
            if magic != b'TKID':
                print(f"ERROR: Bad magic {magic!r}", file=sys.stderr)
                sys.exit(1)
            n_tokens = struct.unpack('<I', f.read(4))[0]
            ids = struct.unpack(f'<{n_tokens}i', f.read(n_tokens * 4))
            print(f"Token IDs ({n_tokens} tokens): {list(ids)}")
            decoded = enc.decode(list(ids))
            print(f"Decoded: {decoded!r}")
        return

    # Get input text
    if args.text == '-':
        text = sys.stdin.read()
    elif args.text:
        text = args.text
    elif args.file:
        with open(args.file, 'r') as f:
            text = f.read()
    else:
        text = sys.stdin.read()

    # Tokenize
    ids = enc.encode(text)

    # Write binary
    with open(args.output, 'wb') as f:
        f.write(b'TKID')
        f.write(struct.pack('<I', len(ids)))
        for tok_id in ids:
            f.write(struct.pack('<i', tok_id))

    if args.print_ids:
        print(f"Tokens ({len(ids)}): {ids}")
        print(f"Written to: {args.output}")

if __name__ == '__main__':
    main()
