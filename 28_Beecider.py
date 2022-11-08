'''
28 - Beecider - Motion Picture Details Scraping Decider
- details scraping for: TV Movie, TV Special (project 27)// Movies (project 22) // TV Series (project 23)
- instead of starting one of the 3 programs according of the new record`s type
- start only one, which triggers the chosen one
'''

from subprocess import call
import os

def run_Movie():
    os.chdir(r"D:\_DEV\Python\py_21-25_projects")
    call(["python", "22_Movie_Details_Scraping.py"])

def run_Series():
    os.chdir(r"D:\_DEV\Python\py_21-25_projects")
    call(["python", "23_TVShow_Details_Scraping.py"])

def run_TV_Movie_TV_Special():
    os.chdir(r"D:\_DEV\Python\py_26-30_projects")
    call(["python", "27_TVMovie-TVSpecial_Details_Scraping.py"])

# BANNER
print('\n')
k = 11
print(' Z-z-z '*k)
print()
print(' Beecider '.center(len(' Z-z-z '*k)))
print()
print(' Z-z-z '*k)
print()

print('Which type of nectar should I collect for you?'.center(len(' Z-z-z '*k)))
print('Movie(M) / Show-Series(S) / TV Movie(T) '.center(len(' Z-z-z '*k)))

print()
print(''.ljust(len(' Z-z-z '*int(k/2))), ' ', end='')   # move the cursor to middle 
n_type = input().lower()

while n_type not in ['m','s','t']:
    print()
    print('It`s a typo buddy. Try again: ', end='')
    n_type = input().lower()

if n_type == 'm':
    run_Movie()

if n_type == 's':
    run_Series()

else:
    run_TV_Movie_TV_Special()