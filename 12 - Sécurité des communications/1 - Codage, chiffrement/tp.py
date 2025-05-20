def code_ascii(texte):
    """ str -> [int] """
    return [ord(c) for c in texte]
#     tab = []
#     for c in texte:
#         tab.append(ord(c))
#     return tab

def decode_ascii(codes):
    return "".join([chr(c) for c in codes])
    
#     chaine = ''
#     for c in codes:
#         chaine += chr(c)
#     return chaine
#     
#     chaine = chr(codes[0])
#     for i in range(1, len(codes)):
#         chaine += chr(codes[i])
#     return chaine