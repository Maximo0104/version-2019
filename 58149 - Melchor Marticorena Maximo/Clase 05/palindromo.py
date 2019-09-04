def palindromo (palabra):
    a = list (palabra.replace(" ",""))
    b = list (palabra.replace(" ",""))
    print(a)
    print(b)
    b.reverse()
    if a == b:
         return True
    return False
if __name__ == "__main__":
    print (palindromo("agita falsos usos la fatiga"))