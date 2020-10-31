def DiffieHellman():
    AvaSecret = 14  
    AudraSecret = 19 
    SharedPrime = 9
    SharedBase = 11
    
    Z = (SharedBase ** AvaSecret) % SharedPrime
    print( "Ava Sends Over Public Chanel: " , Z )
    
    Y = (SharedBase ** AudraSecret) % SharedPrime
    print( "Audra Sends Over Public Chanel: ", Y)
    
    AudraSharedSecret = (Z ** AudraSecret) % SharedPrime
    AvaSharedSecret = (Y ** AvaSecret) % SharedPrime
    if AvaSharedSecret == AudraSharedSecret:
        print( "Privately Calculated Shared Secret:" )
        print( "    Ava Shared Secret: ", AvaSharedSecret )
        print( "    Audra Shared Secret: ", AudraSharedSecret )

DiffieHellman()
