from zipfile import ZipFile, BadZipFile
import zlib

with open('Ashley-Madison.txt') as f:
    passwords = []
    for line in f:
        passwords.append(line.strip())


with ZipFile('whitehouse_secrets.zip') as zf:
    for i, password in enumerate(passwords):
        if i % 10000 == 0:
            print(i, password)

        try:
            zf.extractall(pwd=password.encode())
            print('Password:', password)
            break
        except (RuntimeError, BadZipFile, zlib.error):
            continue