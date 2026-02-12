def fizzbuzz(n):
    for i in range(1, n+1):
        txt = ""
        if i % 3 == 0:
            txt = txt + "Fizz"
        if i % 5 == 0:
            txt = txt + "Buzz"
        if txt == "":
            print(i)
        else:
            print(txt)

fizzbuzz(15)