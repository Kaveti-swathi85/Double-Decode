import base64

encoded = "YUdWc2JHOD0="

first_decode = base64.b64decode(encoded)
second_decode = base64.b64decode(first_decode)

print("Decoded message:", second_decode.decode())