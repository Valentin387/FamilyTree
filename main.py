import uuid
import json
import os

class TreeNode:
    def __init__(self,CODE,name,birthday,alive,death):
        self.CODE=CODE
        self.name = name
        #birthday
        self.birthday=birthday
        #dead in
        self.stillLiving=alive
        self.death=death
        #offspring
        self.children=[]
        #ancestry
        self.father=None
        self.mother=None
        #marital status
        self.spouse=None
        self.partner=None
        self.friend=None
        #Diseases
        self.diseases=None
        #Other info
        self.RH=None
        self.cedula=None


    def AddChild(self,child):
        child.parent=self
        self.children.append(child)

    def getLevel(self):
        level = 0
        p = self.father or self.mother
        while p:
            level+=1
            p=p.parent
        return level

    def printTree(self):
        spaces = ' '*self.getLevel() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.name)
        if self.children:
            for child in self.children:
                child.printTree()

    #def convertTOJson(self):
    #    jsonString=json.dumps(self.__dict__)

def addTreeNode():
    print("\t\t\t ADDING NEW MEMBER")
    CODE=str(uuid.uuid1())
    name=input("Enter complete name: ")
    Bday=input("Enter day of birthday: ")
    Bmonth=input("Enter number of month of birthday: ")
    Byear=input("Enter year of birthday: ")
    birthdayDate=Bday+"/"+Bmonth+"/"+Byear

    alive=int(input("is this person still living? (1:yes, other number:no): "))
    deathDate=""
    if alive != 1:
        Dday=input("Enter day of death: ")
        Dmonth=input("Enter month of death: ")
        Dyear=input("Enter year of death: ")
        deathDate=Dday+"/"+Dmonth+"/"+Dyear

    newone=TreeNode(CODE,name,birthdayDate,alive,birthdayDate)
    NewJsonFile=json.dumps(newone.__dict__)

    with open("database.txt",'a', encoding='utf-8') as database:
        database.write(NewJsonFile)
        database.write("\n")

def DisplayMenu():
    print("\t\t\t WELCOME TO VALENTIN'S FAMILY TREE DOCS \n\n")
    print("Please select the number of an option\n\n")
    print("(1) add new member")
    print("(2) print tree from the top")
    print("(100) close application")

    print("\n\n")
    return int(input("Your choice: "))


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def Read_Database_fromAbove():
    with open("database.txt",'r') as file:
        lineList=file.readlines()
        for line in lineList:
            Node=json.loads(line)
            print(Node)

    a=input("\n\n press a key to continue")
    cls()


if __name__ == "__main__":

    while True:
        op=DisplayMenu()
        if op==1:
            cls()
            addTreeNode()
        elif op == 2:
            cls()
            Read_Database_fromAbove()
        elif op ==100:
            break
        else:
            cls()
            print("not a valid selection")


    print("\n\n END OF LINE")

#
