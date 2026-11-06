import ctypes
from pathlib import Path

SIZE = 1024 * 1024

bcrypt = ctypes.WinDLL("bcrypt.dll")

BCryptGenRandom = bcrypt.BCryptGenRandom

BCryptGenRandom.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(ctypes.c_ubyte),
    ctypes.c_ulong,
    ctypes.c_ulong
]

BCryptGenRandom.restype = ctypes.c_long

buffer = (ctypes.c_ubyte * SIZE)()

status = BCryptGenRandom(
    None,
    buffer,
    SIZE,
    0x00000002
)

if status != 0:
    raise RuntimeError(f"Error: {status}")

output = Path(__file__).with_name("windows_cng.bin")
output.write_bytes(bytes(buffer))

print("Windows CNG random data generated successfully!")
print("File size:", output.stat().st_size, "bytes")