import cmd
import os
import random
import time
import algorithm
import subprocess

class consol(cmd.Cmd):
    intro = "Hello Bro:"
    prompt = "[KW] "
    file = None

    def do_credits(self, arg):	
        print("Download System Sort du fotze kw-corp.de !!!! \nand sub to wittu")

    def do_cd(self, arg):
        if arg == "":
            os.system("cd")
        else:
            os.chdir(arg)
            os.system("cd")
        print()

    def do_dir(self, arg):
        os.system("dir")

    def do_netstat(self, arg):
        os.system("netstat")

    def do_execute(self, arg):
        os.system(arg)

    def do_cool(self, arg):
        if arg == "":
            algorithm.start(int(4))
        else:
            try:
                algorithm.start(int(arg))
            except:
                print("gib ne zahl du spaßt")

if __name__ == '__main__':
    consol().cmdloop()
