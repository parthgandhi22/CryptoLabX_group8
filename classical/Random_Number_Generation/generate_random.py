
import os

size = 1024 * 1024

with open("linux_urandom.bin", "wb") as f:
    f.write(os.urandom(size))

print("Linux random data generated successfully!")
print("File size:", os.path.getsize("linux_urandom.bin"), "bytes")
