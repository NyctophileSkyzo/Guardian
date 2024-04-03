import os
import sys
import platform


def clear():
    os.system("cls" if "win" in sys.platform.lower() else "clear")


from random import randint, choice
from datetime import date
import secrets
import string
import codecs
import zlib
import marshal
import base64

# Set maximum recursion depth
sys.setrecursionlimit(5000)

watermark = f'''"""\n  --  Guardian Protector\n       {date.today().strftime('%d/%m/%Y')}                                                                                                                                           \n"""\n'''


def string_enc(string):
    f = ""
    m = randint(3, 12)

    for letter in string:
        f += str(ord(letter) * m) + ","
    f = f[:-1]

    return f"''.join(chr(int(i/{m})) for i in [{f}])"


# Encrypt string using custom algorithm
def encrypt_string(string):
    encrypted_str = ""
    multiplier = randint(3, 12)

    for letter in string:
        encrypted_str += str(ord(letter) * multiplier) + ","
    encrypted_str = encrypted_str[:-1]

    return f"''.join(chr(int(i/{multiplier})) for i in [{encrypted_str}])"


def split_string(input_string):
    DIFENT_STACK = {}
    reconstruction = []

    for char in input_string:
        if char not in DIFENT_STACK:
            var_name = choice(string.ascii_lowercase) + choice(string.ascii_uppercase)
            while var_name in DIFENT_STACK.values():
                var_name = (
                    choice(string.ascii_lowercase)
                    + choice(string.ascii_uppercase)
                    + choice(string.ascii_lowercase)
                )
            DIFENT_STACK[char] = var_name
        reconstruction.append(DIFENT_STACK[char])
    difen_stak_str = ";".join([f'{var}="{chr(char)}"' for char, var in DIFENT_STACK.items()])
    reconstruction_string = "+".join([var for var in reconstruction])

    return difen_stak_str, reconstruction_string


clear()
input_file = input(f"Masukkan nama file input (contoh: input.py): ")
output_file = input(f"Masukkan nama file output (contoh: output.py): ")

with open(input_file, "rb") as file:
    code_to_obfuscate = file.read()
randxor = "".join(
    secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30)
)

memestrings = [
    randxor,
    "".join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30)),
    "".join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30)),
    "".join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30)),
    "".join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30)),
    "".join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(30)),
]

for i in range(len(memestrings)):
    memestrings[i] = string_enc(memestrings[i])
# Definisi variabel ptt
ptt = "4637192805"


def random_math(_sum):
    try:
        f = randint(-_sum, randint(-_sum, 999))
        f1 = randint(-_sum, randint(-_sum, 999))
        f2 = randint(-_sum, randint(-_sum, 999))
        return f"{_sum-f-f1+f2}+{f}+{f1}-{f2}"
    except Exception as e:
        print(e)
        return str(_sum)


xor = lambda message, key: "".join(
    chr(ord(c) ^ ord(k)) for c, k in zip(message, __import__("itertools").cycle(key))
)


def enc(x, use_xor=True):
    final = ""
    if use_xor == True:
        x = xor(x, randxor)
    for letter in x:
        fl = "{}".format(ord(letter))
        for character in fl:
            final += ptt[int(character)]
        final += "​"
    return final[:-1]


# print(enc("exec",False))


def obfuscate(code):
    b = compile(code, "", "exec")

    code_bytes = marshal.dumps(b)
    encoded_code = base64.b64encode(code_bytes)

    difen_stak_str, recon_str = split_string(encoded_code)
    code2 = f"""__builtins__.eval("".join(chr(i) for i in [101,120,101,99]))(__import__({string_enc("marshal")}).loads(__import__({string_enc("base64")}).b64decode({recon_str})))"""

    return (
        watermark
        + r"_f4_, __vars__={}, [];"
        + f"""{difen_stak_str};__vars__.append({string_enc(choice(memestrings))});eval({string_enc('setattr(__builtins__,"______",compile)')});_f4_["ꀀ"]="0";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀁ"]="1";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀂ"]="2";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀃ"]="3";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀄ"]="4";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀅ"]="5";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀆ"]="6";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀇ"]="7";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀈ"]="8";_f4_["ꀉ"]="9";_f4_["ꀊ"]="A";_f4_["ꀋ"]="B";_f4_["ꀌ"]="C";_f4_["ꀍ"]="D";__vars__.append({string_enc(randxor)});_f4_["ꀎ"]="E";_f4_["ꀏ"]="F";_f4_["ꀐ"]="G";_f4_["ꀑ"]="H";_f4_["ꀒ"]="I";_f4_["ꀓ"]="J";_f4_["ꀔ"]="K";_f4_["ꀕ"]="L";_f4_["ꀖ"]="M";_f4_["ꀗ"]="N";_f4_["ꀘ"]="O";_f4_["ꀙ"]="P";_f4_["ꀚ"]="Q";_f4_["ꀛ"]="R";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀜ"]="S";_f4_["ꀝ"]="T";_f4_["ꀞ"]="U";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀟ"]="V";__=lambda _:''.join(chr(int(''.join(str('{ptt}'.index(j))for j in i)))for i in _.split('​'));_f4_["ꀠ"]="W";_f4_["ꀡ"]="X";_f4_["ꀢ"]="Y";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀣ"]="Z";_f4_["ꀤ"]="a";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀥ"]="b";_f4_["ꀦ"]="c";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀧ"]="d";_f4_["ꀨ"]="e";_f4_["ꀩ"]="f";__vars__.append({string_enc(choice(memestrings))});_f4_[" "]="g";_f4_["ꀫ"]="h";_f4_["ꀬ"]="i";_f4_["ꀭ"]="j";_f4_["ꀮ"]="k";_f4_["ꀯ"]="l";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀰ"]="m";_f4_["ꀱ"]="n";_f4_["ꀲ"]="o";_f4_["ꀳ"]="p";_f4_["ꀴ"]="q";_f4_["ꀵ"]="r";_f4_["ꀶ"]="s";_f4_["ꀷ"]="t";__vars__.append({string_enc(choice(memestrings))});_f4_["ꀸ"]="u";_f4_["ꀹ"]="v";_f4_["ꀺ"]="w";_f4_["ꀻ"]="x";_f4_["ꀼ"]="y";_f4_["ꀽ"]="z";__vars__.append({string_enc(choice(memestrings))});eval({string_enc('setattr(__builtins__,"____",eval)')});__vars__.append({string_enc(choice(memestrings))});eval({string_enc('setattr(__builtins__,"_____",exec)')});__vars__.append({string_enc(choice(memestrings))});__vars__.append({string_enc(choice(memestrings))});____({string_enc("__builtins__")}).__dict__[__('{enc("_____",False)}')](____({string_enc('''____(____(_f4_["ꀦ"]+_f4_["ꀲ"]+_f4_["ꀰ"]+_f4_["ꀳ"]+_f4_["ꀬ"]+_f4_["ꀯ"]+_f4_["ꀨ"])('compile','','eval'))''')})(____((lambda x,y: ''.join(chr(ord(c)^ord(k)) for c,k in zip(x, __import__({string_enc("itertools")}).cycle(y))))(__({string_enc(enc(f"(lambda x,y: ''.join(chr(ord(c)^ord(k)) for c,k in zip(x, __import__({string_enc('itertools')}).cycle(y))))"))}),__vars__[{random_math(9)}]))(__(____(__import__({string_enc("codecs")}).decode(__import__({string_enc("zlib")}).decompress({ str(zlib.compress(codecs.encode(string_enc(enc(code2))), 9))})))),__vars__[{random_math(9)}]),'',{string_enc("exec")}));__vars__[1],__vars__[3],__vars__[4],__vars__[5],__vars__[6],__vars__[9]=1,2,3,4,5,6;_____({string_enc('obfuscated_with_guardian = __vars__[5]')}); __vars__[9] = 32 if obfuscated_with_guardian == __vars__[5] else 0;____({string_enc('print(chr(__vars__[9]))')}) ##end"""
    )


with open(output_file, "w", encoding="utf-8") as f:
    f.write(obfuscate(code_to_obfuscate))
print("Obfuscated")
