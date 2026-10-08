from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

block_size=16
queries=0

# this key is known only to oracle
key=get_random_bytes(16)


# checking whether PKCS#7 padding is valid
def valid_padding(data):

    if len(data)==0 or len(data) % block_size!=0:
        return False

    n=data[-1]

    if n<1 or n>block_size:
        return False

    if data[-n:]!=bytes([n]) * n:
        return False

    return True


# this decrypts data without removing padding
def decrypt_data(iv, cipher_text):

    cipher=AES.new(key, AES.MODE_CBC, iv)

    return cipher.decrypt(cipher_text)


# this is padding oracle
def oracle(data):

    global queries

    queries+=1

    iv = data[:block_size]
    cipher_text=data[block_size:]

    plain_text=decrypt_data(iv, cipher_text)

    return valid_padding(plain_text)


# this recovers one plaintext block
def decrypt_block(prev, curr):

    intermediate=[0]*block_size
    plain=[0]*block_size

    for pos in range(block_size-1, -1, -1):

        padding=block_size-pos

        modified = bytearray(prev)
        # modified creates copy of prev that we are allowed to change

        # Set known bytes to the current padding
        for j in range(pos + 1, block_size):
            modified[j] = intermediate[j] ^ padding

        found = False

        # Try every possible value
        for guess in range(256):

            modified[pos]=guess

            test = bytes(modified) + curr

            if not oracle(test):
                continue

            # Check for false positive on last byte
            if pos == block_size-1:

                check = bytearray(modified)

                check[pos - 1] ^= 1

                test2 = bytes(check) + curr

                if not oracle(test2):
                    continue

            intermediate[pos] = guess ^ padding
            # guess is C' we get for required pos

            plain[pos] = intermediate[pos] ^ prev[pos]

            found=True

            break

        if not found:
            raise Exception("Could not recover byte " + str(pos))

    return bytes(plain)


# adding PKCS#7 padding
def pad(data):

    n=block_size-(len(data)%block_size)

    return data + bytes([n]) * n


# removing PKCS#7 padding
def unpad(data):

    n = data[-1]

    if n < 1 or n > block_size:
        raise Exception("Invalid padding")

    if data[-n:] != bytes([n]) * n:
        raise Exception("Invalid padding")

    return data[:-n] # gives whole data from start to last except last n bytes


message=input("Enter plaintext: ").encode()
# .encode() convert this plaintext to bytes

# generate random IV
iv=get_random_bytes(block_size)

# add PKCS#7 padding
padded=pad(message)

# encrypt message
cipher=AES.new(key, AES.MODE_CBC, iv)

cipher_text=cipher.encrypt(padded)


# split ciphertext into 16 byte blocks
blocks = []

for i in range(0, len(cipher_text), block_size):
    blocks.append(cipher_text[i:i + block_size])


# recover every plaintext block
plain_text = b""
# b means in bytes, after this we decode to string

prev=iv

for curr in blocks:

    block=decrypt_block(prev,curr)
    plain_text+=block
    prev=curr


# Removing final padding
plain_text=unpad(plain_text)


print()
print("Original plaintext:")
print(message.decode())

print()
print("Recovered plaintext:")
print(plain_text.decode())

print()
print("Total oracle queries:", queries)