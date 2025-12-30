def caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

msg = "Hackers do Bem - Fundamental"
chave = 10

cifrado = caesar(msg, chave)
decifrado = caesar(cifrado, -chave)

print(f"Original: {msg}")
print(f"Cifrado (+10): {cifrado}")
print(f"Decifrado (-10): {decifrado}")