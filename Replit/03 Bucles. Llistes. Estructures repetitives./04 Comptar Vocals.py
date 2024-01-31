num_vocals = 0
vocals = ["a", "e", "i", "o", "u"]

paraula = input("Introdueix una paraula de 8 lletres o més: ")

if len(paraula) < 8:
    print("Ho sento. La paraula té menys de 8 lletres. Has perdut la teva oportunitat.") # Oportunidad de que? Suena muy amenazante lol
else:
    for lletra in paraula:
        if lletra in vocals:
            num_vocals += 1

    print(f"La paraula '{paraula}' té {num_vocals} vocals.")