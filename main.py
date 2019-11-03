#this is an implementation of BIP 39
#it takes in a set amount of words from the BIP 39 word list to create a 512 bit number
import hashlib as hsh
import tkinter as tk
import random as rand

#class containing all the hashing functions
class HashingFunctions:
    def __init__(self):
        self.word_list_length = 2048
        self.word_list = open('words.txt', 'r').readlines()
        self.word_list = [word[:-1] for word in self.word_list]
    
    def get_input(self):
        ent = input('type whatever you want into the keyboard: ')
        return ent

    def create_entropy(self, ent):
        ent = hsh.sha256(ent.encode('utf-8')).hexdigest()
        ent = bin(int(ent, 16))
        return ent[2:]
        
    def check_sum(self, ent):
        initial_entropy = ent[:32]
        return ent+initial_entropy

    def create_word_list(self, ent):
        ent = ent[2:]
        list_length = len(ent)//11
        return [self.word_list[int(ent[11*x:11*(x+1)],2)] for x in range(list_length)]

    def create_master_key(self, word_list):
        word_list = ''.join(word_list)
        master_key = hsh.sha256(word_list.encode('utf-8')).hexdigest()
        return master_key

    def master_key(self ):
        entropy = self.get_input()
        entropy = self.create_entropy(entropy)
        chk_sum = self.check_sum(entropy)
        word_list = self.create_word_list(chk_sum)
        master_k = self.create_master_key(word_list)
        return [word_list, master_k]

class Display(HashingFunctions):
    #make a GUI with the following elements
    #Top box is an input box that can
    #   1. display the mnemonic phrase generated by the user
    #   2. have the user input a memonic phrase
    #Bottom left will have 2 buttons
    #   1. one button to start collecting entropy
    #   2. one button to generate mnemonic phrase and key
    #Bottom right will have a display showing master key
    def __init__(self):
        HashingFunctions.__init__(self)
        self.win1 = tk.Tk()
        self.win1.wm_title('Mnemonic Phrase Generator')
        self.win1.resizable(width=False, height=False)
        self.mnemonicLabel = tk.Label(self.win1, text = 'Mnemonic Phrase')
        self.mnemonicBox = tk.Text(self.win1, height=5)
        self.keyLabel = tk.Label(self.win1, text = 'private_key')
        self.keyBox = tk.Text(self.win1, height=5)
        pass

    def user_provided_entropy(self):
        ent = rand.randrange(1,10**256-1)
        entropy = self.create_entropy(str(ent))
        check_sum = self.check_sum(entropy)
        mnemonic = self.create_word_list(check_sum)
        mnemonic = ' '.join(mnemonic)
        print(type(mnemonic))
        self.keyBox.delete('1.0', tk.END)
        self.mnemonicBox.delete('1.0', tk.END)
        self.mnemonicBox.insert('1.0', mnemonic)
        mnemonic = self.mnemonicBox.get('1.0', tk.END)
        key = self.create_master_key(mnemonic)
        self.keyBox.insert('1.0', key)

    def user_provided_mnemonic(self):
        mnemonic = self.mnemonicBox.get('1.0', tk.END)
        print(type(mnemonic))
        key = self.create_master_key(mnemonic)
        self.keyBox.delete('1.0', tk.END)
        self.keyBox.insert('1.0', key)

    def create_buttons(self):
        self.entropyButton = tk.Button(self.win1, text = 'create mnemonic phrase', command = self.user_provided_entropy) #add command from hash class
        self.generateButton = tk.Button(self.win1, text = 'create bitcoin address', command = self.user_provided_mnemonic) #add create_word_list function


    def main_window(self):
        self.label = tk.Label(self.win1, text='entropy')
        self.entry = tk.Entry(self.win1, bd=5)

    def window_elements(self):
        self.mnemonicLabel.grid(row=0, column=1, columnspan=2)
        self.mnemonicBox.grid(column=1, columnspan=2, row=1, padx=10, pady=10)
        self.keyBox.grid(column=1, columnspan=2, row=1, padx=10, pady=10)
        self.entropyButton.grid(column=1, row=2)
        self.generateButton.grid(column =2, row = 2)
        self.keyLabel.grid(column=1, columnspan=2, row=3)
        self.keyBox.grid(column=1, columnspan=2, row=4)

    def display_window(self):
        self.create_buttons()
        self.main_window()
        self.window_elements()
        self.win1.mainloop()

if  __name__ == '__main__':

    Display().display_window()
