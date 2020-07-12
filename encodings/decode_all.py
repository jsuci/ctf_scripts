#!/usr/bin/env python3

from base64 import b64decode, b32decode, b16decode


def main():
    s = input("Enter a string: ").encode()

    try:
        decode64 = b64decode(s)
        print(f"b64decode: {decode64}")

        decode32 = b32decode(s)
        print(f"b32decode: {decode32}")

        decode16 = b16decode(s)
        print(f"b16decode: {decode16}")

    except Exception:
        pass


if __name__ == "__main__":
    main()
