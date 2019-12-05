#this is an implementation of BIP 39
#it takes in a set amount of words from the BIP 39 word list to create a 512 bit number
import hashlib as hsh
import tkinter as tk
import random as rand

#class containing all the hashing functions
class HashingFunctions:
    def __init__(self, entropy = '1', word_list = None):
        self.word_list_length = 2048
        self.word_list = open('words.txt', 'r').readlines()
        self.word_list = [word[:-1] for word in self.word_list]
        self.entropy = bin(int(hsh.sha256(entropy.encode('utf-8')).hexdigest(), 16))[2:]
        self.result_word_list = word_list
        self.binary_seed = None
        self.passphrase = 'TREZOR'
    
    def get_input(self):
        self.entropy = input('type whatever you want into the keyboard: ')

    #generates entropy based on user input. it is output as the result of a sha256 hash and the entripy is given as 256 random bits
    def create_entropy(self):
        entropy_hash = hsh.sha256(self.entropy.encode('utf-8')).hexdigest()
        ent = bin(int(ent, 16))
        self.entropy = ent[2:] #removes the prefix '0b' from binary string
        
    #checksum is created by taking the first len(ent) (in this case 256 bits)/32 bits of sha256 of entropy
    def check_sum(self):
        self.check_sum = self.entropy[:len(self.entropy)//32]

    def create_word_list(self):
        ent_and_chk = self.entropy+self.check_sum #the initial entropy with the checksum appended to end
        list_length = len(ent_and_chk)//11
        self.result_word_list = [self.word_list[int(self.entropy[11*x:11*(x+1)],2)] for x in range(list_length)]

    def create_binary_seed(self):
        word_list = ''.join(self.result_word_list)
        print(word_list)
        self.binary_seed = hsh.pbkdf2_hmac('sha512', str.encode(word_list), str.encode('mnemonic'+self.passphrase), 2048).hex()

    def master_key(self):
        entropy = self.get_input()
        entropy = self.create_entropy()
        chk_sum = self.check_sum()
        word_list = self.create_word_list()
        master_k = self.create_master_key()


if __name__ == '__main__':
    test1 = HashingFunctions('00000000000000000000000000000000')
    test1.check_sum()
    test1.create_word_list()
    test1.create_binary_seed()
    #print(test1.result_word_list)
    #print(test1.binary_seed)
    test2 = HashingFunctions('1', 'abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about')
    test2.create_binary_seed()
    print('test2', test2.binary_seed)
    test3 = HashingFunctions('', 'legal winner thank year wave sausage worth useful legal winner thank yellow')
    test3.create_binary_seed()
    print('test3', test3.binary_seed)
