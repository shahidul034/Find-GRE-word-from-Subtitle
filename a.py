
from tkinter import *
import os


def sucess():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Sucessful")
    screen2.geometry("320x100")
    Label(screen2, text="Sucessfully saved GRE words in Desktop \n as a text file(GRE_word.txt)", fg="green", font=("calibri", 11)).pack()
    Label(screen2, text="").pack()
    screen.destroy()



def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("GRE")
    Label(text="GRE word extraction from subtitle", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Open File", height="2", width="30", command=Gre_word_extract).pack()

    Label(text="").pack()
    Label(text="Author: Shahidul Salim Shakib").pack()
    Label(text="CSE,KUET").pack()


    screen.mainloop()

def file_open():
    import os
    from tkinter.filedialog import askopenfilename
    path = os.getlogin()
    filename = askopenfilename(initialdir="C:\\Users\\" + path + "\\Desktop")
    return filename


def Gre_word_extract():
    import os
    d_str2 = ""
    d_str3="Word,Meaning\n"
    path = os.getlogin()
    filename2 = "C:\\Users\\" + path + "\\Desktop\\" + "GRE_word.txt"
    F2 = open(filename2, 'w')

    filename3 = "C:\\Users\\" + path + "\\Desktop\\" + "GRE_word.csv"
    F3 = open(filename3, 'w')

    F1 = open(file_open(),'r')
    str = F1.read()
    str2 = str.split("\n\n")

    import re
    def space_removed(param):
        st = ""
        for x in param:
            if (x >= 'a' and x <= 'z') or (x >= 'A' and x <= 'Z'):
                st += x
        st = st.lower()
        return st

    GreWords = []
    words = []
    NotInGreWords = []

    def FindGreWord(word):
        word2 = word
        word = p_stemmer.stem(word)
        word = word.lower()
        F2 = open(r"all.txt", 'r', encoding="utf8")
        str2 = F2.read()
        str3 = str2.split("\n")
        for x in str3:
            if len(x):
                xx = x.split("-->")
                if len(xx) > 1:
                    w = space_removed(xx[0])
                    if p_stemmer.stem(w) == word or w == word2:
                        words.append(p_stemmer.stem(w))
                        print(w, " --> ", xx[1])
                        l = w, xx[1], True
                        GreWords.append(l)
                        return l

        return "", "", False

    cnt = 0
    from nltk.stem.porter import PorterStemmer
    p_stemmer = PorterStemmer()
    for x in str2:
        cnt += 1
        xx = x.split("\n")
        if len(xx) > 2:
            ss = re.split("\W", xx[2])
            st = xx[2]
            for x2 in ss:
                tr = False
                if len(x2) and (p_stemmer.stem(space_removed(x2)) not in words) and (
                        p_stemmer.stem(space_removed(x2)) not in NotInGreWords):
                    ch = FindGreWord(p_stemmer.stem(space_removed(x2)))
                    if ch[2] == False:
                        NotInGreWords.append((space_removed(x2)))
                    else:
                        d_str2 += (ch[0] + " --> "+ ch[1]+"\n")
                        d_str3+=(ch[0]+","+ch[1]+"\n")

    F2.write(d_str2)
    F3.write(d_str3)
    sucess()
    print("Done!!!!")


main_screen()







