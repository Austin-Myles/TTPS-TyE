
# Length between 3 and 200 chars.
# Begins and end with a Slash.  

# Notes with it's length
notes = {
    "W" : 1,
    "H" : 1/2,
    "Q" : 1/4,
    "E" : 1/8,
    "S" : 1/16,
    "T" : 1/32,
    "X" : 1/64
}

while(True):
    try:
        jingle = input()
        cant = 0
        aux = 0
        firstslash = True

        if((jingle.startswith("/") and jingle.endswith("/"))and (len(jingle)>=3 and len(jingle)<=200)):
            for x in jingle:
                if(x == "/"):
                    if firstslash:
                        firstslash = False
                    if aux == 1:
                        cant += 1
                    aux = 0
                else:
                    aux = aux + notes[x]
            print(cant)
    except EOFError:
        break