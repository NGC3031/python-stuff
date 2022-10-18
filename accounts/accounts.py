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


p1 = Account("BK", "000001")
p2 = Account("MF", "000002")
p3 = Account("AC", "000003")
p4 = Account("RM", "000004")


def deposit(dr, am):
    p1.credit(am)
    dr.debit(am)


def withdrawal(cr, am):
    p1.debit(am)
    cr.debit(am)


def transfer(cr, dr, am):
    cr.credit(am)
    dr.debit(am)


transfer(p3, p2, 34)

print("ACC:", p3.acNumber, " Balance: ", "${:,.2f}".format(p3.bl))
print("ACC:", p2.acNumber, " Balance: ", "${:,.2f}".format(p2.bl))
