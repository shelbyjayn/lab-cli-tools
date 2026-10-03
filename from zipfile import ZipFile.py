from zipfile import ZipFile
with ZipFile('guido_secrets.zip') as zf:
    password = 'BFDL'.encode('ascii')
    zf.extractall(pwd=password)