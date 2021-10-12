"""
Programing Language: Python3
Project #1 - Question 8,
Problem: Orbit of Eris.
Group Members: 
Steve Wufeng, Tim Bishop, Lucas Romero, Aniket Sonika, Kyle Mullen
"""
import math as m        # importing math module for better calculation

# global variables
# constants
R_p = 5.7635 * (10**9)      # radius at periapsis.
e   = 0.4335                # Eccentricity (between 0 and 1)

def A_total(theta):
    """ This is a f(x) given in the A_total integrals."""
    # Note that this A_total function does not include intergral.
    return (0.5)*((R_p*(1+e))/(1+ e * m.cos(theta)))**2

def simpson_rule(n, function, upper_bound, lower_bound):
    """ This function performs the simpson rule to for a given function """
    if n % 2:   # simpson rule must have an even n!
        raise ValueError("n must be even (received n=%d)" % n)  #raise an error

    # outside
    # In other word, this is the "(delta-x)/3" of the simpson's rule
    outside = (upper_bound - lower_bound)/(3 * n)

    # inside
    # This represent the [f(x0) + 4f(x1) + 2f(x2) + 4f(x3) ... + 4f(x29) + f(x30)] of simpson rule.
    inside = 0                                  # simply creating a variable to store the right side of simpson's rule
    delta_x = (upper_bound - lower_bound)/n     # pre-calculate delta-x

    for i in range(0,n+1):                      # i = index = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ... 28, 29, 30]
        x = lower_bound + (i * delta_x)         # calculate our domain to sub into the funciton equation
        if i == 0 or i == n:                    # in simpsons rule, we dont multiply for the bounding points
            inside += function(x)               # +f(0) and +f(30) with out multiplying.
            print(f'{i+1}. f({x}) = {function(x)}')
        elif i % 2 != 0:                        # for odd numbers index,
            inside += (4 * function(x))         # we multiply our function by 4.
            print(f'{i+1}. 4 * f({x}) = {4*function(x)}')
        elif i % 2 == 0:                        # for even numbers index,
            inside += (2 * function(x))         # we multiply our function by 2.
            print(f'{i+1}. 2 * f({x}) = {2*function(x)}')


    # result 
    # outside = ((delta-x)/3)
    # inside = [f(x0) + 4f(x1) + 2f(x2) + 4f(x3) ... + 4f(x29) + f(x30)]
    result = outside * inside

    return result   # return result

def check_answer():
    """ This function will return the correct answer for us to compare and check """
    a = (R_p)/(1-e)             # as given a is raiuds at periapsis over (1 - eccentricity)
    b = a * m.sqrt(1 - (e**2))  # and b is a * sqrt(1- eccentricity^2)
    result = m.pi * a * b       # our expected answer is A = pi * a * b
    return result

def main():
    """ This function will call our functions to run the program """
    # our calculation
    answer = simpson_rule(30, A_total, 2*m.pi, 0)
    print('simspon_rule:', answer)

    # the actual answer
    actual_answer = check_answer()
    print('check:', actual_answer)

    # print out the difference between the two answer
    print('check - simpson =', actual_answer - answer)

if __name__ == "__main__":
    """ 
    this if statement will set out program to only be running if the file is running in main
    but not as an imported module
    """
    main()

"""
#### Output ####
1. f(0.0) = 1.6608966125e+19
2. 4 * f(0.20943951023931953) = 6.7322703373124624e+19
3. 2 * f(0.41887902047863906) = 3.5025431325630333e+19
4. 4 * f(0.6283185307179586) = 7.482978258642854e+19
5. 2 * f(0.8377580409572781) = 4.101499894619489e+19
6. 4 * f(1.0471975511965976) = 9.221366333138543e+19
7. 2 * f(1.2566370614359172) = 5.3085191313615585e+19
8. 4 * f(1.4660765716752366) = 1.2494106638524636e+20
9. 2 * f(1.6755160819145563) = 7.489383210341034e+19
10. 4 * f(1.8849555921538759) = 1.8202076959448944e+20
11. 2 * f(2.0943951023931953) = 1.1126720592637773e+20
12. 4 * f(2.3038346126325147) = 2.7087231832062706e+20
13. 2 * f(2.5132741228718345) = 1.6191573127886035e+20
14. 4 * f(2.722713633111154) = 3.742447205272257e+20
15. 2 * f(2.9321531433504733) = 2.0576130990337055e+20
16. 4 * f(3.141592653589793) = 4.254006575082753e+20
17. 2 * f(3.3510321638291125) = 2.057613099033706e+20
18. 4 * f(3.560471674068432) = 3.742447205272258e+20
19. 2 * f(3.7699111843077517) = 1.6191573127886035e+20
20. 4 * f(3.979350694547071) = 2.7087231832062725e+20
21. 2 * f(4.1887902047863905) = 1.1126720592637782e+20
22. 4 * f(4.39822971502571) = 1.8202076959448944e+20
23. 2 * f(4.607669225265029) = 7.48938321034104e+19
24. 4 * f(4.817108735504349) = 1.249410663852464e+20
25. 2 * f(5.026548245743669) = 5.3085191313615585e+19
26. 4 * f(5.235987755982988) = 9.221366333138546e+19
27. 2 * f(5.445427266222308) = 4.1014998946194915e+19
28. 4 * f(5.654866776461628) = 7.482978258642854e+19
29. 2 * f(5.864306286700947) = 3.5025431325630345e+19
30. 4 * f(6.073745796940266) = 6.732270337312464e+19
31. f(6.283185307179586) = 1.6608966125e+19
simspon_rule: 2.930363161308837e+20
check: 2.9303631546669004e+20
check - simpson = -664193662976.0
#### End of Output ####
"""
