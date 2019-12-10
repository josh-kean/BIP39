#this is an implementation of BIP 39
#it takes in a set amount of words from the BIP 39 word list to create a 512 bit number
import hashlib as hsh
import tkinter as tk
import random as rand
import sys

#class containing all the hashing functions
class HashingFunctions:
    def __init__(self, entropy = hsh.sha256('hello'.encode('utf-8')).hexdigest(), word_list = None):
        self.word_list = open('words.txt', 'r').readlines()
        self.word_list = [word[:-1] for word in self.word_list]
        self.word_list_length = len(self.word_list)
        self.entropy = entropy #need to determine the number of bits stored in entropy
        self.result_word_list = word_list
        self.binary_seed = None
        self.passphrase = 'TREZOR'
        self.check_sum = None
    
    def get_input(self):
        self.entropy = input('type whatever you want into the keyboard: ')

    #checksum is created by taking the first len(ent) (in this case 256 bits)/32 bits of sha256 of entropy
    def create_check_sum(self):
        entropy_hash = hsh.sha256(self.entropy.encode('utf-8')).hexdigest()
        entropy_hash = entropy_hash[2:]
        #entropy is input as a hex value
        ent_length = sys.getsizeof(int(self.entropy, 16))
        #takes the first to len(binary)//32 bits of the hash of the initial entropy
        self.check_sum = entropy_hash[:ent_length//32]
        self.check_sum = bin(int(self.check_sum, 16))[2:]

    def create_word_list(self):
        self.entropy = bin(int(self.entropy, 16))[2:]
        ent_and_chk = self.entropy+self.check_sum #the initial entropy with the checksum appended to end
        list_length = len(ent_and_chk)//11
        self.result_word_list = [self.word_list[int(self.entropy[11*x:11*(x+1)],2)]+' ' for x in range(list_length)]

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
    test1.create_check_sum()
    test1.create_word_list()
    test1.create_binary_seed()
    print(test1.result_word_list)
    print(test1.binary_seed)
    test2 = HashingFunctions('1', 'abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about')
    test2.create_binary_seed()
    print('test2', test2.binary_seed)
    test3 = HashingFunctions('', 'legal winner thank year wave sausage worth useful legal winner thank yellow')
    test3.create_binary_seed()
    print('test3', test3.binary_seed)
