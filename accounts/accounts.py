import random


class Account:
    def __init__(self, name, acNumber):
        self.name = name
        self.acNumber = acNumber
        self.bl = 20

    def credit(self, cr):
        self.bl = self.bl-cr
        cr = "${:,.2f}".format(cr)
        print(self.acNumber, "----")
        print("DR: -", cr)

    def debit(self, dr):
        self.bl = self.bl+dr
        dr = "${:,.2f}".format(dr)
        print(self.acNumber, "----")
        print("CR: ", dr)


p1 = Account("BK", "88880099986871")
p2 = Account("MF", "78687687677772")
p3 = Account("AC", "76876764323335")
p4 = Account("RM", "45511223354689")


def deposit(dr, am):
    p1.credit(am)
    dr.debit(am)


def withdrawal(cr, am):
    p1.debit(am)
    cr.debit(am)


def transfer(cr, dr, am):
    cr.credit(am)
    dr.debit(am)


for x in range(20000):
    r = random.randrange(1, 5)
    if r == 1:
        a = p1
    if r == 2:
        a = p2
    if r == 3:
        a = p3
    if r == 4:
        a = p4

    r = random.randrange(1, 5)
    if r == 1:
        b = p1
    if r == 2:
        b = p2
    if r == 3:
        b = p3
    if r == 4:
        b = p4

    r = random.randrange(1, 4)
    am = random.randrange(0, 100)
    if r == 1:
        transfer(a, b, am)
    if r == 2:
        deposit(a, am)
    if r == 2:
        withdrawal(a, am)
    print("ACC:", a.acNumber, " Balance: ", "${:,.2f}".format(a.bl))
    print("ACC:", b.acNumber, " Balance: ", "${:,.2f}".format(b.bl))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("ACC:", p1.acNumber, " Balance: ", "${:,.2f}".format(
    p1.bl), "ACC:", p2.acNumber, " Balance: ", "${:,.2f}".format(p2.bl), "ACC:", p3.acNumber, " Balance: ", "${:,.2f}".format(
    p3.bl), "ACC:", p4.acNumber, " Balance: ", "${:,.2f}".format(p4.bl)
)
print
("--------------------------------------------------------------------------------------------------------------------------------------------------------------------")
