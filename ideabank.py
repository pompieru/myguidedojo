import sys

def write_file():
    with open ("ideas.txt", "a+") as f:
        idea = str(input("What is your new idea: "))
        f.write(idea + "\n")
        





def read_file():
     with open("ideas.txt", "r") as f:
        print("\nYour ideabank")
        for i, line in enumerate(f):
            print("{}.{}".format ((i+1), line.strip()))
        


def delete_file():
    with open ("ideas.txt", "r") as f:
         lista = list(f)
    
    del lista[int(sys.argv[2]) - 1]
    with open ('ideas.txt', 'w') as f:
            for i in lista:
                f.write(i)
    
    read_file()


for argv in sys.argv:
    if (argv == "--list"):
        read_file()
    if len(sys.argv) == 1:
        write_file()
        read_file()
    if (argv == "--delete") and (int(sys.argv[2]) >0):
        delete_file()





