import streamlit as st

# Fonction de chiffrement Rail Fence
def encrypt_rail_fence(plaintext, k):
    plaintext = plaintext.replace(" ", "").lower()
    rail = [['' for _ in range(len(plaintext))] for _ in range(k)]
    direction_down = False
    row, col = 0, 0

    for char in plaintext:
        rail[row][col] = char
        col += 1

        if row == 0 or row == k - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1

    ciphertext = ''.join(''.join(rail[i]) for i in range(k))
    return ciphertext

# Fonction de déchiffrement Rail Fence
def decrypt_rail_fence(ciphertext, k):
    rail = [['' for _ in range(len(ciphertext))] for _ in range(k)]
    direction_down = False
    row, col = 0, 0

    for i in range(len(ciphertext)):
        rail[row][col] = '*'
        col += 1

        if row == 0 or row == k - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1

    idx = 0
    for i in range(k):
        for j in range(len(ciphertext)):
            if rail[i][j] == '*':
                rail[i][j] = ciphertext[idx]
                idx += 1

    plaintext = []
    row, col = 0, 0
    for i in range(len(ciphertext)):
        plaintext.append(rail[row][col])
        col += 1

        if row == 0 or row == k - 1:
            direction_down = not direction_down

        row += 1 if direction_down else -1

    return ''.join(plaintext)

# Interface Streamlit
st.title("Chiffrement et Déchiffrement Rail Fence")

# Saisie de texte
plaintext = st.text_input("Texte clair (pour chiffrer) :", "")
ciphertext = st.text_input("Texte chiffré (pour déchiffrer) :", "")
k = st.number_input("Nombre de rails (k) :", min_value=1, step=1, value=2)

# Boutons pour chiffrer et déchiffrer
if st.button("Chiffrer"):
    if plaintext:
        encrypted_text = encrypt_rail_fence(plaintext, k)
        st.text_area("Texte chiffré :", encrypted_text, height=100)
    else:
        st.warning("Veuillez entrer un texte clair pour le chiffrement.")

if st.button("Déchiffrer"):
    if ciphertext:
        decrypted_text = decrypt_rail_fence(ciphertext, k)
        st.text_area("Texte déchiffré :", decrypted_text, height=100)
    else:
        st.warning("Veuillez entrer un texte chiffré pour le déchiffrement.")
