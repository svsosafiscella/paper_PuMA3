import numpy as np


def PERIOD(T, F0, COEFF, TMID):
    
    DT = (T - TMID) * 1440.
    
    FREQ = ( 11*(DT**10)*COEFF[11] + 10*(DT**9)*COEFF[10] + 9*(DT**8)*COEFF[9] + 8*(DT**7)*COEFF[8] + 7*(DT**6)*COEFF[7] + 6*(DT**5)*COEFF[6] + 5*(DT**4)*COEFF[5] + 4*(DT**3)*COEFF[4] + 3*(DT**2)*COEFF[3] + 2*DT*COEFF[2] + COEFF[1] ) * (1/60.) + F0
        
    return 1/FREQ


def findP(file, T):

    ncoef = np.genfromtxt ( file, comments="none", dtype=int, skip_header=1, max_rows=1, usecols=(4) ) # número de coeficientes
    COEFF = np.zeros(ncoef)                 # vector de coeficientes
    lines = sum(1 for line in open(file))   # número de líneas

    n = 0               # número de líneas leídas del archivo .polycos
    not_found = True

    while not_found:

        TMID = np.genfromtxt( file, comments="none", dtype=np.float128, skip_header=n, max_rows=1, usecols=(3) )
        span_min = np.genfromtxt( file, comments="none", dtype=float, skip_header=n+1, max_rows=1, usecols=(3) )
        span_mjd = span_min * (1./(60.*24.))
        
        T_inicial = TMID - span_mjd/2.
        T_final   = TMID + span_mjd/2.

        if T >= T_inicial and T < T_final:
    
            F0 = np.genfromtxt( file, comments="none", dtype=float, skip_header=n+1 , max_rows=1, usecols=(1) ) 
            matrix = np.genfromtxt(file, usecols=range(3), dtype=np.float128, skip_header=n+2, max_rows=4)
            COEFF = matrix.flatten('C')                                                                   

            P_seg = PERIOD(T, F0, COEFF, TMID)   # período en segundos
            P_ms  = P_seg * 1000.                # período en milisegundos
        
            not_found = False
        
        else:
    
            n += 6
            
            if n >= lines:
                print("ERROR: el T indicado no se encuentra dentro del .polycos")
                return
            
    return P_ms