def pythagoras(SIDE, LEN1, LEN2):
    
    from math import sqrt # This is function is needed to work, it **SHOULD** be included with the default install. 

    ANSWER = "Error Code 1" # This should not logicaly happen if the user is not an idiot and follows the usage.
    

    if type(LEN1) is str or type(LEN2) is str: # This checks if the user didn't listen to the usage // Was the LEN a string?
        ANWSER = "Error Code 2"
        return ANWSER # This will return an error to the user that didn't listen.

    if type(SIDE) is int or type(SIDE) is float: # This checks if the user didn't listen to the usage // Was the SIDE an integer or float?
        ANWSER = "Error Code 4"
        return ANWSER # This will return an error to the user that didn't listen.

    #--SIDE C--
    if SIDE.lower() == "c":

        #SIDE C CALCULATION (Hypotenuse)
        A_SIDE = LEN1   
        B_SIDE = LEN2 
        C_SIDE = sqrt(A_SIDE * A_SIDE + B_SIDE * B_SIDE)  

        ANSWER = C_SIDE # This sets the answer to be returned.
        
    #--SIDE A--
    elif SIDE.lower() == 'a':  

        if LEN1 < LEN2: # This will happen if the user did not follow instructions. See error below. 
            print("The hypotenues should be bigger")
            anwser = "Error code 2"
            return ANSWER # This will return an error to the user that didn't listen.

        #SIDE A CALCULATION   
        B_SIDE = LEN2 
        C_SIDE = LEN1  
        ASIDE = sqrt((C_SIDE * C_SIDE) - (B_SIDE * B_SIDE))  

        ANSWER = A_SIDE # This sets the answer to be returned.

    #--SIDE B--
    elif SIDE.lower() == 'b':

        if LEN1 < LEN2: # This will happen if the user did not follow instructions. See error below. 
            print("The hypotenues should be bigger")
            ANSWER = "Error code 2"
            return ANSWER # This will return an error to the user that didn't listen.

        #SIDE B CALCULATION    
        A_SIDE = LEN2
        C_SIDE = LEN1
        B_SIDE = sqrt(C_SIDE * C_SIDE - A_SIDE * A_SIDE)  

        ANSWER = B_SIDE # This sets the answer to be returned.
    

    return ANSWER # Returns the anwser for the user to use. 


