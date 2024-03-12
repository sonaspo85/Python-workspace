from Crypto.PublicKey import RSA


class createkeyfile:
    def __init__(self):
        self.key = RSA.generate(2048)
        self.privateKey()
        self.publicKey()

    def privateKey(self):
        print("개인키 생성")
        # 개인 키 생성
        private_key = self.key.export_key()
        file_out = open("private.pem", "wb")
        file_out.write(private_key)
        file_out.close()

    def publicKey(self):
        print("공개키 생성")
        # 공개키 생성
        public_key = self.key.publickey().export_key()
        file_out = open("receiver.pem", "wb")
        file_out.write(public_key)
        file_out.close()
