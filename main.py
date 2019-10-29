#this is an implementation of BIP 39
#it takes in a set amount of words from the BIP 39 word list to create a 512 bit number
import hashlib as hsh

word_list_length = 2048
word_list = open('words.txt', 'r').readlines()
word_list = [word[:-1] for word in word_list]

def create_entropy():
    ent = input('type whatever you want into the keyboard: ')
    ent = hsh.sha256(ent.encode('utf-8')).hexdigest()
    ent = bin(int(ent, 16))
    return ent[2:]
    
def check_sum(ent):
    initial_entropy = ent[:32]
    return ent+initial_entropy

def create_word_list(ent):
    ent = ent[2:]
    list_length = len(ent)//11
    return [word_list[int(ent[11*x:11*(x+1)],2)] for x in range(list_length)]

def create_master_key(word_list):
    word_list = ''.join(word_list)
    master_key = hsh.sha256(word_list.encode('utf-8')).hexdigest()
    return master_key

def master_key():
    entropy = create_entropy()
    chk_sum = check_sum(entropy)
    word_list = create_word_list(chk_sum)
    master_k = create_master_key(word_list)
    return [word_list, master_k]

if  __name__ == '__main__':
    a = master_key()
    print(a[0])
    print(a[1])
