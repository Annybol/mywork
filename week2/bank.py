#bank.py
#input two amounts, adding them and prints the sum
#Anne Boland

x = int(input("enter amount1(in cent): "))
y = int(input("enter amount2(in cent): "))

ans = (x/100) + (y/100)

txt = "the total sum i ${:.2f}"

print (txt.format(ans))

