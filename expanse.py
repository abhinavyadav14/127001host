import os
from colorama import Fore
from tabulate import tabulate

class expanse:#{
    def __init__(self,members):#{
        self.members = members+1
        self.expanse = [[0]*self.members for i in range(self.members)]
    #}
    def addNames(self):#{
        for i in range(self.members):
            if(i == 0):#{
                self.expanse[0][i] = "EXPANSE"
                print(self.expanse[0][0])
            #}
            else:#{
                na = input("Enter the"+str(i)+" name:\r")
                self.expanse[0][i] = na
                self.expanse[i][0] = na
            #}
    #}
    def addExpanse(self):#{
        for i in range(self.members):#{
            if(i != 0):#{
                print(str(i)+".",self.expanse[0][i])
                #}
            #}
        p = int(input("Who paid[Enter the number from above]:"))
        m = int(input("How much?:"))
        dividedMoney = round(m/(self.members-1),2)
        for i in range(1,self.members):
            if(i != p):
                self.expanse[p][i] += dividedMoney
                div = self.expanse[i][p] - dividedMoney
                if(div < 0):
                    self.expanse[p][i] -= self.expanse[i][p]
                    self.expanse[i][p] = 0
                elif(div >= 0):
                    self.expanse[p][i] -= dividedMoney
                    self.expanse[i][p] = div
        #}
    def totalGet(self):#{
        temp = 0
        for i in self.expanse:
            if(temp != 0):
                total = 0
                for j in i[1:]:
                    total += int(j)
                print(str(i[:1])+" will get Rs "+str(total))
            temp += 1
        #}
    def totalPay(self):
        for i in range(self.members):
            total = 0
            if(i != 0):
                for j in range(self.members):
                    if(j != 0):
                        total += self.expanse[j][i]
                print(str(self.expanse[i][0])+" have to pay "+str(total))
    
    def singleExpanse(self):
        for i in range(1,self.members):
            print(str(i)+". "+self.expanse[0][i])
        p = int(input("whose expanse you want know:"))
        print("PAY:")
        for i in range(1,self.members):
            if(i != p):
                print(str(self.expanse[0][p])+" have to pay "+str(self.expanse[i][p])+" to "+str(self.expanse[i][0]))
        print("GET:")
        for i in range(1,self.members):
            if(i != p):
                print(str(self.expanse[p][0])+" will get "+str(self.expanse[p][i])+" from "+str(self.expanse[i][0]))


    def printExpanse(self):#{
        #with tabulate
        print(tabulate(self.expanse))
        """ without tabulate
        for i in self.expanse:
            print(i)
        """
    #}
#}

ex = expanse(3)
ex.addNames()
ex.addExpanse()
ex.printExpanse()
ex.totalGet()
ex.totalPay()
ex.singleExpanse()
# ex.addExpanse()
# ex.printExpanse()
# ex.addExpanse()
# ex.printExpanse()
# ex.addExpanse()
# ex.printExpanse()
# ex.addExpanse()
# ex.printExpanse()