from tkinter import *
import random
import re
from word_generator import file_gen
import os
import keyboard
import easygui
class Gen:
    def __init__(self):
        self.t=Tk()
        self.t.title("Wordle But With Any Word Length")
        self.label=Label(text="Please Enter Your Preferred Word Length & Difficulty")
        self.label.grid(row=0,column=1,columnspan=2)
        self.length=Entry()
        self.length.grid(row=1,column=1,columnspan=2)
        self.length.focus_set()
        self.easy = Button(text="Easy", command=self.soft_gen,width=15,background="green")
        self.easy.grid(row=2, column=1)
        self.hard=Button(text="Hard",command=self.igen0,width=15,background="red")
        self.hard.grid(row=2,column=2)
        self.ez=False
        self.status="start"
    def igen0(self):
        num=self.length.get()
        try:
            num2=int(num)
        except:
            easygui.msgbox(title="this option is not valid",msg="Please enter a real positive number that can reasonably be the length of commonly used nouns without using any special characters or letters, only a singular whole and postive number")
            self.length.delete(0, 99)
            self.ez=False
        else:
            #the below values are the limiters for the word length, they can be changed if one modifies the word_generator.py file to use a larger database of words
            if num2<3 or num2>8:
                easygui.msgbox(title="this option is not valid",msg="Please enter a real positive number that can reasonably be the length of commonly used nouns without using any special characters or letters, only a singular whole and postive number")
                self.length.delete(0, 99)
                self.ez = False
            else:
                if self.ez:
                    self.igen5(num)
                self.igen(num)
    def igen5(self,num):
        try:
            with open(f"words({num})^#.csv", "r") as file:
                self.read2=file.readlines()
        except:
            print("file2 not found")
            self.igen4(num)
        else:
            if self.read2==[]:
                print("file2 is empty")
                os.remove(f"words({num})^#.csv")
                self.igen4(num)
            # else:
            #     print("loading prebuilt file2")
            #     self.igen2(num)
    def igen(self,num):
        try:
            with open(f"words({num}).csv", "r") as file:
                self.read=file.readlines()
        except:
            print("file not found")
            self.igen3(num)
        else:
            if self.read==[]:
                print("file is empty")
                os.remove(f"words({num}).csv")
                self.igen3(num)
            else:
                print("loading prebuilt file")
                self.igen2(num)
    def igen4(self,num):
        print("generating new file(ez)")
        gen = file_gen()
        try:
            gen.gen2(num)
            with open(f"words({num})^#.csv") as file:
                self.read2 = file.readlines()
        except:
            self.del_2(num)
        else:
            if self.read2 == []:
                self.del_2(num)
    def igen3(self,num):
        print("generating new file")
        gen = file_gen()
        try:
            gen.gen(num)
            with open(f"words({num}).csv") as file:
                self.read=file.readlines()
        except:
            self.del_(num)
        else:
            if self.read==[]:
                self.del_(num)
            else:
                self.igen2(num)
    def callback(self,var):
        content = var.get()
        for i in range(0,len(content)):
            try:
                self.placements[self.current_row][i].config(text=content[i].upper())
            except:
                pass
    def backdel(self):
        cont=True
        try:
            if len(self.input.get())<=len(self.word):
                for i in range(len(self.word)-1,-1,-1):
                    if cont:
                        if self.placements[self.current_row][i].cget("text")!="[]":
                            self.placements[self.current_row][i].config(text="[]")
                            cont=False
        except:
            pass
    def del_(self,num):
        easygui.msgbox(title="this option is not valid",msg="Please enter a real positive number that can reasonably be the length of commonly used nouns without using any special characters or letters, only a singular whole and postive number")
        self.length.delete(0, 99)
    def del_2(self,num):
        easygui.msgbox(title="this option is not valid",
                       msg="Please enter a real positive number that can reasonably be the length of commonly used nouns without using any special characters or letters, only a singular whole and postive number")
        self.length.delete(0, 99)
    def igen2(self,num2):
        try:
            self.label.destroy()
            self.length.destroy()
            self.hard.destroy()
            self.easy.destroy()
        except:
            pass
        self.read=[re.sub("\n","",word) for word in self.read]
        if self.ez:
            self.read2 = [re.sub("\n", "", word) for word in self.read2]
            self.word = random.choice(self.read2)
        else:
            self.word = random.choice(self.read)
        self.word_characterization={letter:[] for letter in self.word}
        for letter in self.word:
            self.word_characterization[letter].append(letter)
        # print("all files loaded")
        self.t.title("InfiniWordle")
        self.t.config(background="light gray")
        self.placements={0:[],1:[],2:[],3:[],4:[],5:[]}
        self.current_row=0
        for i in range(0,int(num2)*6):
            self.gen(i,num2)
        var = StringVar()
        var.trace("w", lambda name, index, mode, var=var: self.callback(var))
        self.input = Entry(self.t,textvariable=var)
        self.input.grid(row=6, column=0, columnspan=24)
        self.input.focus_set()
        self.status="game"
        self.btn = Button(text="Submit Guess", command=self.guess)
        self.btn.grid(row=7, column=0, columnspan=24)
        self.alphabet=["Q","W","E","R",'T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
        self.alpha={}
        self.alpha2 = {}
        for i in range(0,26):
            self.gen_alpha(i)
        # print(self.word)
        # while True:
        #     time.sleep(1)
        #     print(self.input.get())
    def soft_gen(self):
        self.ez=True
        self.igen0()
    def gen(self,num,num2):
        self.num2=int(num2)
        letter_num=num%self.num2
        line_num=num//self.num2
        new_letter=Label(text="[]",background="light gray",width=1)
        new_letter.grid(row=line_num,column=((letter_num)*2)+1)
        self.placements[line_num].append(new_letter)
        for i in range(0,(self.num2)*2,2):
            l=Label(background="light gray",text="_")
            l.grid(row=99,column=i)
            l = Label(background="light gray",text="_")
            l.grid(row=99, column=i+1)
        l = Label(background="light gray", text="_")
        l.grid(row=99, column=(self.num2*2))
    def gen_alpha(self,col):
        new_keyboard_letter=Label(text=self.alphabet[col],background='light gray',font=("arial",6),width=1)
        self.alpha[self.alphabet[col]]=new_keyboard_letter
        self.alpha2[self.alphabet[col]] = new_keyboard_letter
        col+=1
        row=8
        for i in range(0,2):
            if col>9:
                col-=9
                row+=1
        col+=(int(self.num2)-5)
        if self.num2<4:
            col+=1
        new_keyboard_letter.grid(column=col,row=row)
    def guess(self):
        if self.status=="game":
            guess=self.input.get().lower()
            # guess=guess[0:self.num2]
            self.input.delete(0,99)
            for i in self.word:
                self.backdel()
            if guess != "":
                if len(guess) !=self.num2:
                    easygui.msgbox(title="Invalid Word Length", msg="The length of the word you have guessed does not match the word length that you have set for this game")
                elif guess not in self.read:
                    easygui.msgbox(title="Not a Real Word", msg="The word that you have entered is not registered in our database and is likely not a real english world")
                else:
                    self.word_characterization = {letter: [] for letter in self.word}
                    for letter in self.word:
                        self.word_characterization[letter].append(letter)
                    temp_word_characterization=self.word_characterization
                    for i in range(0,self.num2):
                        self.placements[self.current_row][i].config(text=guess[i].upper(),background="gray")
                        if guess[i].lower()==self.word[i]:
                            temp_word_characterization[guess[i].lower()] = temp_word_characterization[guess[i].lower()][:-1]
                            self.placements[self.current_row][i].config(background="green",width="1")
                            self.placements[self.current_row][i]=""
                            try:
                                self.alpha[guess[i].upper()].config(background="green")
                                self.alpha[guess[i].upper()]="null"
                                self.alpha2[guess[i].upper()] = "null"
                            except:
                                pass
                    # print(self.placements)
                    for i in range(0,self.num2):
                        if (guess[i].lower() in self.word) and (guess[i].lower() in temp_word_characterization[guess[i].lower()]):
                            temp_word_characterization[guess[i].lower()]=temp_word_characterization[guess[i].lower()][:-1]
                            self.placements[self.current_row][i].config(background="yellow")
                            try:
                                self.alpha2[guess[i].upper()].config(background="yellow")
                                self.alpha2[guess[i].upper()] = "null"
                            except:
                                pass
                        elif guess[i].lower() not in self.word:
                            try:
                                self.alpha[guess[i].upper()].config(background="gray")
                            except:
                                pass
                    self.current_row+=1
                    if guess.lower()==self.word:
                        if self.current_row==1:
                            self.end = Label(text=f"YOU WON ON YOUR FIRST GUESS!", background="green",font=("arial",8,"bold"))
                        else:
                            self.end = Label(text=f"YOU WON IN {self.current_row} GUESSES!", background="green")
                        self.end_(f"win-{self.current_row}")
                    elif self.current_row==6:
                        self.end=Label(text=f"YOU LOST TO [{self.word.upper()}]",background="red",font=("arial",8,"bold"))
                        self.end_("loss")
        elif self.status=="over":
            self.replay()
    def end_(self,cond):
        self.status="over"
        self.input.destroy()
        self.btn.destroy()
        self.end.grid(row=6, column=0, columnspan=self.num2*2)
        self.refresh=Button(text="Click to Play Again",font=("arial",7,"italic"),command=self.replay)
        self.refresh.grid(row=7,column=0,columnspan=self.num2*2)
        if self.ez:
            dif="easy"
        else:
            dif="hard"
        with open("win-loss_ratio.csv","a") as file:
            file.write(f"{self.num2},{dif},{self.word},{cond}\n")
    def replay(self):
        self.end.destroy()
        self.refresh.destroy()
        for i in range(0,6):
            for item in self.placements[i]:
                try:
                    item.destroy()
                except:
                    pass
        self.status="game"
        self.igen2(self.num2)
    def cont(self):
        keyboard.on_press_key("backspace", lambda _:self.backdel())
        keyboard.on_press_key("enter", lambda _: self.guess())
        self.t.mainloop()
