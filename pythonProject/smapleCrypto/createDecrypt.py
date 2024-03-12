from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA


### 복호화 하기 ###
class customdecrypt:
    def __init__(self):
        self.decrypt()

    def decrypt(self):
        file_in = open("encrypted_data.bin", "rb")
        infile = open("private.pem").read()
        private_key = RSA.import_key(infile)

        enc_session_key, nonce, tag, ciphertext = [
            file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)
        ]

        # 개인 RSA 키로 세션 키를 해독합니다.
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # AES 세션 키를 사용하여 데이터 암호 해독
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
        print("복호화된 데이터:", data.decode("utf8"))
