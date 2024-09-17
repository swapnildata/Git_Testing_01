if __name__=="__main__":
    import calculator
    c=calculator.addition(4)
    print("c=", c)
    s=calculator.square(c)
    print("s=",s)
    k=calculator.cube(s)
    print("k=",k)
    mul=calculator.mul(k,s)
    print("The multiplication is: ", mul)