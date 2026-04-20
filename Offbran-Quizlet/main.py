from tkinter import *
import pandas
import pandas as pd
import random
data=pd.read_csv("./data/words_to_learn.csv")
english_words=(data["English"]).to_list()
foreign_words=(data["French"]).to_list()
BACKGROUND_COLOR = "#B1DDC6"
language="French"
word="word"
window=Tk()
window.title("Flash Card Generator")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
def gen():
    global word_index
    if len(foreign_words)==0:
        canvas.itemconfig(word_txt, text="")
        canvas.itemconfig(language_txt, text="You Have Finished Studying!")
    else:
        word_index=random.randint(0,len(foreign_words)-1)
        word=foreign_words[word_index]
        canvas.itemconfig(word_txt,text=word)
def flip():
    global face_down
    global word_index
    if len(foreign_words) != 0:
        if face_down:
            canvas.itemconfig(card,image=card_back)
            canvas.itemconfig(language_txt,text="English")
            canvas.itemconfig(word_txt,text=english_words[word_index])
            face_down=False
        else:
            canvas.itemconfig(card, image=card_front)
            canvas.itemconfig(language_txt, text=language)
            canvas.itemconfig(word_txt, text=foreign_words[word_index])
            face_down=True
def learn():
    english_words.remove(english_words[word_index])
    foreign_words.remove(foreign_words[word_index])
    dictionary={
        language:foreign_words,
        "English":english_words
    }
    data=pandas.DataFrame(dictionary)
    data.to_csv("./data/words_to_learn.csv")
    gen()
def refresh():
    global data
    data2 = pd.read_csv("./data/french_words.csv")
    data2.to_csv("./data/words_to_learn.csv")
    data = pd.read_csv("./data/words_to_learn.csv")
    gen()
canvas=Canvas(width=800, height=526)
right_img=PhotoImage(file="./images/right.png")
left_img=PhotoImage(file="./images/wrong.png")
card_back=PhotoImage(file="./images/card_back.png")
card_front=PhotoImage(file="./images/card_front.png")
card=canvas.create_image(400,263,image=card_front)
language_txt=canvas.create_text(400,150,text=language,font=("Arial",40,"italic"))
word_txt=canvas.create_text(400,263,text=word,font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
wrong_btn=Button(image=left_img,highlightthickness=0,command=gen)
wrong_btn.grid(row=1,column=0)
right_btn=Button(image=right_img,highlightthickness=0,command=learn)
right_btn.grid(row=1,column=1)
face_down=True
flip_btn=Button(text="Flip",font=("Arial",20,"bold"),fg="white",bg=BACKGROUND_COLOR,command=flip)
flip_btn.grid(row=2,column=0)
refresh_btn=Button(text="Refresh",font=("Arial",20,"bold"),fg="white",bg=BACKGROUND_COLOR,command=refresh)
refresh_btn.grid(row=2,column=1)
gen()





window.mainloop()