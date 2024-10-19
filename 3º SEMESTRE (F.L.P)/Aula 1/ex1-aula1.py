s = input()
i = 1
while s != "#":
    if s == "HELLO": print(f"Case {i}: ENGLISH")
    elif s == "HOLA": print(f"Case {i}: SPANISH")
    elif s == "HALLO": print(f"Case {i}: GERMAN")
    elif s == "BONJOUR": print(f"Case {i}: FRENCH")
    elif s == "CIAO": print(f"Case {i}: ITALIAN")
    elif s == "ZDRAVSTVUJTE": print(f"Case {i}: RUSSIAN")
    else: print(f"case {i}: UNKNOWN")
    s = input()
    i += 1  