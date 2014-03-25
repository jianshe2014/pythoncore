#coding:utf-8

在空白处填上True或False
p q   (not p) or q   (p and q) or q   (p or q) and p   (p or q) and (p and q)
True True 
True False 
False True 
False False 
'''


print "p q  (not p) or q   (p and q) or q     (p or q) and p     (p or q) and (p and q)"
length = len("p q (not p) or q (p and q) or q (p or q) and p (p or q) and (p and q)")

print "_" * length
for p in [True,False]:
    for q in [True,False]:
        print "%-9s %-9s %-9s %-9s %-9s %-9s" %(p,q,(not p) or q,(p and q) or q,(p or q) and p, (p or q) and (p and q))
