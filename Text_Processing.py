# Importing BeautifulSoup, re for regex and glob for reading files from folder
# simultaneously
from bs4 import BeautifulSoup
import os
import re
import glob

def parser ():

    # accept mode of parsing from user
    option = input("enter handing option: 1 for default (both), 2 for just case folding, 3 for just punctuation handling: ")
    mode = int(option)

    # open each and every file present in the given directory
    for file in glob.glob("*.txt"):

        # following strings will be updated to handle various forms of text in files
        new_str = ""
        final_str = ""
        p = ""
        w= ""
        x = ""
        g = ""
        s = ""
        e = ""

        # opens the file in read mode
        f = open(file, "r", encoding = 'utf-8')
        page = f.read()
        soup_object = BeautifulSoup(page, 'html.parser')
        with open(file, "w",encoding = 'utf-8') as f:
            content_files = soup_object.find_all(['p','h1','h2','h3'])
            for line in content_files:

                 w = line.get_text()
                 # removing certain special characters
                 x = w.replace("\n", " ").replace("(","").replace(")","").replace("\"","").replace("−","").replace("‑", "").replace("′","").replace(u'\ufeff', "")
                 g = re.sub(r'\{.*\}', "", x)                                  # regex for removing curly braces
                 s = re.sub(r'\[.+?\]\s*', "", g)                              # regex for removing square braces

                 if ((mode == 1) or (mode ==3)):
                     e = re.sub('[^a-zA-Z0-9\n\.]', ' ', s)                    # regex to get only alphanumeric value
                 else:
                     e = s

                 if ((mode == 1) or (mode ==2)):
                     p = e.lower()                                             # to convert to lower case
                 else:
                     p = e

                 new_str = new_str + p.strip() + " "                           # to strip any white space present

                 if ((mode == 1) or (mode == 3)):
                     final_str = re.sub(r"(?<!\d)[.,;:''](?!\d)", "", new_str, 0)   # regex to handle punctuations
                 else:
                     final_str = new_str

            f.write(' '.join(final_str.split()))                               # remove white spaces while writing to file


parser()  # calling the function
