#TO CHANGE THE PASSWORD YOU'RE TRYING TO CRACK:
#Run hasher.py, replacing myPassword in that program
#with the password you want to use, and replace the value
#of myHashedPassword with the entire output - including the b
#and the single quotes. It should look like the current myHashedPassword.
myHashedPassword = b'\xfe\x1d\x1a\xd6WE\x08\xc5\x8cP\xb2\x1cR\xf9B\xee'

#DO NOT MODIFY ANY CODE BELOW
import hashlib, sys
from time import sleep

#checks the inputted parameter passwordToCheck against the
#correct password
def check_password(passwordToCheck):
    m = hashlib.md5()
    m.update(bytes(passwordToCheck, "utf-8"))
    return(m.digest() == myHashedPassword)

print("Welcome to Will's very secure program! Please enter password:")

#for each line in stdin, checks if the password is correct
for line in sys.stdin:
    line = line.strip()
    if (check_password(line)):
        print("Password correct. Access granted!")
        print("The correct password was \"" + line.strip() + "\"")
        #Feel free to add any more code here that might have been
        #"password-protected," like a link to a relevant video/article or
        #a funny picture!
        sys.exit()

#prints this only if no checked passwords were correct
print("All passwords entered are incorrect. Shutting down...")
