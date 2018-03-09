"""
Dominik Suwala <dxs9411@rit.edu>
Weld Capital Management - Coding Question
HourGlass.py
Reads "N" from stdin and produces an hourglass in stdout.
N is the maximum width of the line
Requires Python 2.7.* (raw_input() vs input())
"""


def getInputInt():
    n = None
    
    while(type(n) is not int):
        
        print('Enter an int:')
        try:
            n = int(raw_input())
        except ValueError:
            print('Err: Input must be of type int')
    return n
        
def main():
    # Change in str length, number of spaces
    delta = -2
    spc = 0
    
    x = 'X'
    n = getInputInt()
    newx = x * n
    
    startLen = n
    MIN_STR_LEN = 2
    
    while(True):
        
        print ' ' * abs(spc) + cur
        # Alternatively could have printed using string format. Same effect,
        # less code
        
        # Exit when we reach the bottom of the hourglass
        if(len(newx[:n]) == startLen and delta > 0):
            break
        
        # Flip i, count back up, Flip number of spaces
        if(n <= MIN_STR_LEN):
            delta = 2
            spc = -spc
        
        n += delta
        spc += 1
    
    return 0
    
if __name__ == "__main__":
    main()
