alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
key=6

plaintext="meet me at the bridge"
ciphertext=""

for x in range(0,len(plaintext)):
    for y in range(0,len(alphabets)):
        if (plaintext[x]==alphabets[y]):
            ciphertext+=alphabets[(y+key)%26]

print('=============================================CAESAR CIPHER====================================')
print('plaintext')
print(plaintext)
print('key:',key)
print('ciphertext')
print(ciphertext)

print('=============================================CRYPTANALYSIS OF CAESAR CIPHER====================================')
plaintext=""
ciphertext="skkzskgzznkhxojmk"

for keys in range(0,26):
    for x in range(0,len(ciphertext)):
        for y in range(0,len(alphabets)):
            if (ciphertext[x]==alphabets[y]):
                plaintext+=alphabets[(y-keys)%26]
    print(keys)
    print(plaintext)
    plaintext=""
