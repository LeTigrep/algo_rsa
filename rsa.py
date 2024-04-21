from OpenSSL import crypto
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


# fonction auxiliaire utilsé 

def string_to_binary_ascii(input_string):
    binary_result = ""
    for char in input_string:
        ascii_value = ord(char)
        binary_representation = bin(ascii_value)[2:].zfill(8)
        binary_result += binary_representation
    return binary_result

def binary_to_ascii(binary_str):
    # Ensure the binary string is a multiple of 8
    binary_str = binary_str.zfill((len(binary_str) + 7) // 8 * 8)
    
    temp = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    ascii_chars = [chr(int(temp, 2)) for temp in temp]
    ascii_string = ''.join(ascii_chars)
    return ascii_string


                       

#                        +----------------------------------+
#                        |       Fonction de chiffrement    |
#                        +----------------------------------+


def chiffrement_rsa(message, n=None, e=None):
    if n is None or e is None:
        cle_publique, cle_privee = generer_cle_rsa()
        n = cle_publique.public_numbers().n
        e = cle_publique.public_numbers().e
        print(f"Clé publique générée : e={e}, n={n}")

    m = string_to_binary_ascii(message)
    
    # Ensure the binary string is a multiple of 8
    m = m.zfill((len(m) + 7) // 8 * 8)
    
    m_int = int(m, 2)
    c = pow(m_int, e, n)
    return c



#                        +----------------------------------+
#                        |      Fonction de déchiffrement   |
#                        +----------------------------------+


def dechiffrement_rsa(c, d, n):
    m = pow(c, d, n)
    m_bin = bin(m)[2:]
    temp = len(m_bin) // 8 + 1
    m_result = (temp - len(m_bin)) * '0' + m_bin
    plaintexte = binary_to_ascii(m_result)
    return plaintexte




#                        +----------------------------------+
#                        |       Génération de la clé       |
#                        +----------------------------------+


def generer_cle_rsa():
    cle_privee = crypto.PKey()
    cle_privee.generate_key(crypto.TYPE_RSA, 2048)
    
    cle_publique = cle_privee.to_cryptography_key().public_key()
    
    # Extract private key in PEM format
    cle_privee_pem = crypto.dump_privatekey(crypto.FILETYPE_PEM, cle_privee).decode('utf-8')

    # Use cryptography to load the private key and obtain private numbers
    cle_privee_cryptography = serialization.load_pem_private_key(
        cle_privee_pem.encode('utf-8'),
        password=None,
        backend=default_backend()
    )
    
    private_numbers = cle_privee_cryptography.private_numbers()

    print("Clé privée générée   : d={}, n={}".format(private_numbers.d, private_numbers.public_numbers.n))

    return cle_publique, cle_privee



#   action de l'utilisateur 

def demander_action():
    print("Choisissez une action :")
    print("1. Chiffrer un message")
    print("2. Déchiffrer un message")
    choix = input("Entrez 1 ou 2 : ")
    return choix

choix = demander_action()

if choix == '1':
    # Chiffrement d'un nouveau message
    message = input("Entrez le message à chiffrer : ")
    
    choix_cle_publique = input("Voulez-vous utiliser votre propre clé publique? (Oui/Non): ").lower()
    
    if choix_cle_publique == 'oui':
        e = int(input("Entrez la clé publique 'e' : "))
        n = int(input("Entrez la clé publique 'n' : "))
        message_chiffre = chiffrement_rsa(message, n, e)
    else:
        message_chiffre = chiffrement_rsa(message)
        
    print("Message chiffré (n'oubliez pas de garder les clés pour un futur besoin comme pour le decryptage) :", message_chiffre)

elif choix == '2':
    # Déchiffrement d'un message existant
    message_chiffre = int(input("Entrez le message chiffré (un nombre entier) : "))
    # Prompt user for private key values
    d_decrypt = int(input("Entrez la clé privée 'd' : "))
    n_decrypt = int(input("Entrez la clé publique 'n' : "))
    message_dechiffre = dechiffrement_rsa(message_chiffre, d_decrypt, n_decrypt)
    print("Message déchiffré:", message_dechiffre)

else:
    print("Choix non valide.")
