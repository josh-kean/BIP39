#this is an implementation of BIP 39
#it takes in a set amount of words from the BIP 39 word list to create a 512 bit number
import hashlib as hsh
import tkinter as tk
import random as rand
import sys

#class containing all the hashing functions
class HashingFunctions:
    def __init__(self, entropy = None, result_word_list = None):
        self.word_list = open('words.txt', 'r').readlines()
        self.word_list = [word[:-1] for word in self.word_list]
        self.word_list_length = len(self.word_list)
        self.entropy = entropy
        self.entropy_bin = None
        self.result_word_list = result_word_list
        self.binary_seed = None
        self.passphrase = 'TREZOR'
        self.check_sum = None
    
    def create_binary_ent(self):
        b = len(self.entropy)*4
        if b <= 128:
            self.entropy_bin = format(int(self.entropy, 16), "0128b")
        elif b <= 160:
            self.entropy_bin = format(int(self.entropy, 16), "0160b")
        elif b <= 192:
            self.entropy_bin = format(int(self.entropy, 16), "0192b")
        elif b <= 224:
            self.entropy_bin = format(int(self.entropy, 16), "0224b")
        elif b <= 256:
            self.entropy_bin = format(int(self.entropy, 16), "0256b")

    def get_input(self, user_input):
        self.entropy = user_input
        #need cases to ensure binary is 128, 160, 192, 224, or 256 bits long
        self.create_binary_ent()

    #checksum is created by taking the first len(ent) (in this case 256 bits)/32 bits of sha256 of entropy
    def create_check_sum(self):
        entropy_hash = hsh.sha256(bytes.fromhex(self.entropy)).hexdigest()
        entropy_hash = format(int(entropy_hash,16), "0256b")#converts entropy hash to binary
        self.check_sum = entropy_hash[:len(self.entropy_bin)//32]

    def create_word_list(self):
        ent_and_chk = f'{self.entropy_bin}{self.check_sum}'
        list_length = len(ent_and_chk)//11
        self.result_word_list = ' '.join([self.word_list[int(ent_and_chk[11*x:11*(x+1)],2)] for x in range(list_length)])

    def create_binary_seed(self):
        word_list = self.result_word_list
        self.binary_seed = hsh.pbkdf2_hmac('sha512', str.encode(word_list), str.encode('mnemonic'+self.passphrase), 2048).hex()

    def master_key(self):
        entropy = self.get_input()
        entropy = self.create_entropy()
        chk_sum = self.check_sum()
        word_list = self.create_word_list()
        master_k = self.create_master_key()


if __name__ == '__main__':
    test1 = HashingFunctions('00000000000000000000000000000000')
    test1.create_check_sum()
    test1.create_word_list()
    test1.create_binary_seed()
    print(test1.result_word_list)
    print(test1.binary_seed)
