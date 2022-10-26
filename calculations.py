import math

def calcSquareFootage(length, width):
    '''
        calcSquareFootage(length : float, width : float)

        Function accepts two float values as parameters, checks
        if values are numerical and then returns the product
        of the values.  If a string is sent in as a parameter, 
        an error message will be displayed and a value of 0 will
        be returned.
    
    '''   
    try:
        length = float(length)
    except:
        print("Length needs to be a number")
        return 0
           
    try:
        width = float(width)
    except:
        print("Width needs to be a number")
        return 0
            

    total_area = length * width
    return round(total_area, 2)


def calcCircumference(radius):
    '''
        calcCircumference(radius : float)

        Function accepts a numerical value.  If a string is passed
        an error message will be displayed and 0 will be returned.  
        Circumference is calculated based on a radius that is passed
        in to the function as a parameter and then returned.
    '''
    try:
        radius = float(radius)
    except:
        print("Radius needs to be a number")
        return 0

    circumference = 2.0 * math.pi * radius
    return round(circumference, 2)



def printName(name):
    print(f"Hello Mr/Ms {name}...we've been waiting for you!")
    
