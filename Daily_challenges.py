""" circalc.py -- simplistic LCR calculator for TPRG 2131 Week 2 Asmt 1

Assignment 1 for Tprg 2131 intro week 1-2


Jack Dunford, 100865823, 2131-01

This LCR calculator is ugly and incomplete. The code runs but doesn't actually
calculate anything. For full marks, you must complete the computation. You must
also "clean up" the code according to the course style guide and coding
standard. Specifically, you must:
  1) Take code that is duplicated and encapsulate it into a function that is
     called from the main program; the function must not "reach into" the
     main program for its working values;
  2) Rename variables so that they are not single letters, using descriptive
     names;
  3) Actually calculate the resonant frequency, bandwidth and Q factor for the
     SERIES resonant circuit (look up the formulas from ELEC II).

Keep working on the program. As you fix each problem, commit with an
informative commit message.
When done, commit with a message like "Ready for marking" and push the changes
to your assignment1 repository on the server hg.set.durhamcollege.org.
"""
import math

print("RC time constant")

    





#print("RC Time Constant (t) =", tau, "seconds")
#tau = R * C

while True:
    g = (input("Do you want to calculate the resistance or time constant or resonant frequency of a series RLC circuit/n enter r or c or h "))
    if g == "r":
        r = float(input("What is the resistance in ohms? "))
        while r <= 0.0:
            r = float(input("The value must be greater than zero\n"
                        "What is the resistance in ohms? "))   

        r2 = float(input("What is the resistance in ohms? "))
        while r2 <= 0.0:
            r2 = float(input("The value must be greater than zero\n"
                        "What is the resistance in ohms? "))
    
        u = (input("Do you want a series or parallel resistor\n enter s or p "))
        if u == "s":
            print("Series resistance is", r + r2)
        elif u == "p":
            print("parallel resistance is", 1/( 1/r + 1/r2))
        else:
            print("invalid input")
        
    elif g == "c":
        r = float(input("What is the resistance r"))
        c = float(input("What is the capacitance c"))
        t = r * c
        print("Time constant is", (t))
    elif g == "h":
        l = float(input("What is the inductance in mH? "))
        while l <= 0.0:
            l = float(input("The value must be greater than zero\n"
                        "What is the inductance in mH? "))

        c = float(input("What is the capacitance in uF? "))
        while c <= 0.0:
            c = float(input("The value must be greater than zero\n"
          "What is the capacitance in uF? "))

        r = float(input("What is the resistance in ohms? "))
        while r <= 0.0:
            r = float(input("The value must be greater than zero\n"
                        "What is the resistance in ohms? "))

    # Calculate the resonant frequency and the Q factor of this circuit
    # Formulas TBD
        print("lcr:", l, c, r, "\n")
    
        L = l * 1e-3
        C = c * 1e-6
    
        f_res = 1 / (2 * math.pi * math.sqrt(L * C))
   
        f = r / (2 * math.pi * L)
        Q = f_res / f
   
        print(f"Resonant frequency (f_res): {f_res:.2f} Hz")
    else:
        print("invalid input")
        
        
        
        
        
print:("The quality factor (Q) of the series RLC circuit is:", Q)

Q = 1/R * math.sqrt(L / C)
Q == "L"

    
    
        
        
        
        
while True:
    r = float(input("What is the resistance in ohms? "))
    while r <= 0.0:
        r = float(input("The value must be greater than zero\n"
                        "What is the resistance in ohms? "))   

    r2 = float(input("What is the resistance in ohms? "))
    while r2 <= 0.0:
        r2 = float(input("The value must be greater than zero\n"
                        "What is the resistance in ohms? "))
    
    u = (input("Do you want a series or parallel resistor\n enter s or p "))
    if u == "s":
        print("Series resistance is", r + r2)
    elif u == "p":
        print("parallel resistance is", 1/( 1/r + 1/r2))
    else:
        print("invalid input")
    
    



print("Series resonant circuit calculator\n(CTRL-C to quit)")

while True:
    l = float(input("What is the inductance in mH? "))
    while l <= 0.0:
         l = float(input("The value must be greater than zero\n"
                        "What is the inductance in mH? "))

    c = float(input("What is the capacitance in uF? "))
    while c <= 0.0:
        c = float(input("The value must be greater than zero\n"
          "What is the capacitance in uF? "))

    r = float(input("What is the resistance in ohms? "))
    while r <= 0.0:
        r = float(input("The value must be greater than zero\n"
                        "What is the resistance in ohms? "))

    # Calculate the resonant frequency and the Q factor of this circuit
    # Formulas TBD
    print("lcr:", l, c, r, "\n")
    
    L = l * 1e-3
    C = c * 1e-6
    
    f_res = 1 / (2 * math.pi * math.sqrt(L * C))
   
    f = r / (2 * math.pi * L)
    Q = f_res / f
   
    print(f"Resonant frequency (f_res): {f_res:.2f} Hz")
    print(f"Bandwidth (f): {f:.2f} Hz")
    print(f"Q Factor (Q): {Q:.2f}")
    
    R = 1000
    C = 0.001

    tau = R * C
    
    print("RC Time Constant (t) =", tau, "seconds")
    
    
    
    
    
    
    
    