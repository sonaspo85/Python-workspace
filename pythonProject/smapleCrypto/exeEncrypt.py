from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes


### 암호화 하는 코드 작성 하기 ###
class customencrypt:
    def __init__(self):
        self.encrypt()

    def encrypt(self):
        # 암호화할 데이터 입력
        strkey = "son min chan"
        # strkey = open('private.pem').read()
        data = strkey.encode("utf-8")

        # 암호화 하기
        infile = open("receiver.pem").read()
        recipient_key = RSA.import_key(infile)
        session_key = get_random_bytes(16)

        # 공개 RSA 키로 세션 키를 암호화합니다.
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        # AES 세션 키로 데이터 암호화
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)

        # 암호문과 추가적인 데이터 저장
        file_out = open("encrypted_data.bin", "wb")
        [
            file_out.write(x)
            for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)
        ]
        file_out.close()
