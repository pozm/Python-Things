import aes,sys,hashlib,shutil,os
def getKey():
    h = hashlib.sha256()
    k = input("Enter the key you want to use:\n")
    h.update(k.encode(encoding="ascii"))
    return h.digest().hex()
def getType():
    typ = input("Would you like to ([E]n/[D]e)crypt?");
    return typ;

def encrypt(sbytes :bytes, key=""):
    if key == "":
        key = getKey()
    enc = aes.encrypt(key, sbytes.hex())
    return enc
def decrypt(sbytes: str, key=""):
    if key == "":
        key = getKey()
    dnc = aes.decrypt(key, sbytes)
    return bytes.fromhex(dnc.decode("utf-8"))


def onLoad():
    typ = (getType()).lower();
    out = {
        "e": encrypt,
        "d": decrypt
    }.get(typ,encrypt)( bytes( typ, "utf8") )
# while True:
#     onLoad();

# ENCRYPTION 
def f_enc(fp :str, keyy : str):

    f = open(fp, mode="r+b")
    b = f.read()
    f.seek(0)
    enc = encrypt(b, key=keyy)
    f.write(bytes(enc))
    f.truncate()
    f.close()
    shutil.move(fp, fp + ".enc")


# DECRYPTION
def f_dnc(fp :str, keyy:str):
    has_ext = fp[-4:] == ".enc"
    f = open( has_ext and fp or fp + ".enc", mode="r+b")
    b = f.read(  )
    f.seek(0)
    enc = decrypt(b, key=keyy)
    f.write(enc)
    f.truncate()
    f.close()
    shutil.move(has_ext and fp or fp + ".enc",has_ext and fp[0:-4] or fp)
p = 1 in sys.argv and sys.argv[1] or "./testenc.txt"

while True:
    i = input("enc or dec?");
    fol = input("folder?")
    f = [];
    if fol != "":
        ex = os.path.exists("./"+fol)
        if not ex:
            print("Entered invalid directory")
            continue;
        f = os.listdir("./"+fol)
    else: 
        f.append(p)
    key = getKey()
    if i == "dec":
        for file in f:
            print("doing //" +file)
            f_dnc((fol and fol+ "/" or "") +file,key);
            print("done // "+file)
    else:
        for file in f:
            print("doing //" +file)
            f_enc((fol and fol+ "/" or "") +file,key);
            print("done // "+file)
    # print(getKey())
