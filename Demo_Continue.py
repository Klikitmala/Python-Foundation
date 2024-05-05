ignore_negative = True
profits = [123,-5,24,-33,69,-99]
for p in profits :
    if p < 0 and ignore_negative :
        continue
    print(p)

for p in profits :
    if p > 0 or (not ignore_negative) :
        print(p)