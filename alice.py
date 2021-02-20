# alice.py
# Copyright 2020 Lu Neder
#
# This work may be distributed and/or modified under the
# conditions of the LaTeX Project Public License, either version 1.3
# of this license or (at your option) any later version.
# The latest version of this license is in
#   http://www.latex-project.org/lppl.txt
# and version 1.3 or later is part of all distributions of LaTeX
# version 2005/12/01 or later.
#
# This work has the LPPL maintenance status `maintained'.
#
# The Current Maintainer of this work is Lu Neder.
#
# This work consists of the files alice.py, README.md and the included original.txt example.


#Alice requires an original.txt file on the directory you're running it from.
#Alice will read the file and then type it (a line followed by an enter, then the next line).
#This way you can send the file contnent on a chat, for example, each line on a message.
#You can also tell Alice to wait some time between a line and the other.
#The first line will be written 10 seconds after you run Alice and tell the time between a line and the other,
#this way you have time to select the place where you want to input your text.

import keyboard
import time
import sys

#Save command line args as args
args = str(sys.argv)

#Shows help if args contain --help, gets and prepare the file if args do not contain --help
if (args.__contains__("--help")):
    mode = "help"
    print("--help: Help mode: show this message")

    print("--loop: Loop mode: restart the file from beginning after it's over")

    print("no args: Normal mode: stop once file ends")
else:
    #Asks how many seconds between lines and saves answer as t
    t = int(input("How many seconds between lines? -> "))
    print(t)

    #open file
    original = open("original.txt", "r", encoding='utf-8')
    conteudo = original.read()

    #divide file lines as list elements and print them
    conteudo_lista = conteudo.splitlines()
    original.close
    print(conteudo_lista)

    #count how many elements are in the list and print the quantity
    linhas = len(conteudo_lista)
    print(linhas)

    #waits 10 seconds so you can find the text input area once Alice is running
    time.sleep(10)

#types each line and press enter, then waits t seconds before doing it with the next line. Keep doing this forever with a While Loop if args contain --loop. If args contain --help it'll just print an empty line
if (args.__contains__("--loop")):
    mode = "loop"
    while True:
        for i in range(linhas):
            keyboard.write(conteudo_lista[i]),
            time.sleep(0.5),
            keyboard.press_and_release("enter"),
            time.sleep(t)
elif (args.__contains__("--help")):
    print("")
else:
    mode = "normal"
    for i in range(linhas):
        keyboard.write(conteudo_lista[i]),
        time.sleep(0.5),
        keyboard.press_and_release("enter"),
        time.sleep(t)
