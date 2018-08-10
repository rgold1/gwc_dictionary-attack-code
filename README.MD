# Girls Who Hack
## Seattle 2018

### 0. Welcome, hacker
 We have protected `passwordentry.py` with an encrypted password that you are going to write some python code to crack.

 Here are the rules we used to create the password:
 1. Our application stipulates, much like the real world, that each
 password must contain at least one capital letter and one number.
 2. Our user is lazy, so they created their password by selecting one of
 the 1000 most common words in the English language, capitalizing a random
 letter, and converting another letter to a number based on the following:
   - an "a" can be converted to a 4
   - an "e" can be converted to a 3
   - an "o" can be converted to a 0
   - an "i" can be converted to a 1
   
   So, each password has exactly one capital letter and exactly one number.

### 1. Get the code
In a command prompt, `cd` into a folder of your choice (wherever you would like to save the code for this activity). Then run:
```
git clone https://github.com/rgold1/gwc_dictionary-attack-code.git
```

### 2. Try and guess the password yourself
 In a command prompt run the following:
```
python passwordentry.py
```
 Try a password and hit enter. If you get it correct, the program will notify you and let you in. If not, you can try another. To exit, hold down `CTRL+C`.

### 3. Try a list of passwords
Create a `.txt` file and put a password you would like to guess on each line. To test your list of passwords, run the following:
```
python passwordentry.py < [your password .txt file]
```

### 4. Generate a dictionary for your attack
Now we will use our `dictionarygenerator.py` to create a dictionary  
```
python dictionarygenerator.py < 1000words.txt > [an output .txt file of your choice, it can be the same as part 3]
```

### 5. Use the the dictionary to crack the password
Run the following:
```
python passwordentry.py < [the file from step 4]
```

### 6. Try using your own password!
1. replace "#a string of your choice" in `hasher.py` with whatever
password you want to use, and run:
```
python hasher.py
```
2. copy the entire output (including the b and both single-quotes)
and replace the current value of myHashedPassword in `passwordentry.py`
with that output
3. Try running your password attack again on this new myHashedPassword

## Questions to Consider
- What passwords are crackable?
- What passwords aren't?
- Are the following passwords crackable:
  - b4Nk
  - b3causE
  - c3ll
  - billion
  - Language
- How would you modify your program to crack any of the uncrackable passwords above?
- How would you modify your program to crack passwords like "li9hT",
"Ma9azine", and "pRo9ram"? What about passwords like "so1diEr", "nEar1y",
and "suCcessfu1"?
- Suppose the user were smarter, and made every character that could be
converted to a number that number (e.g. "b4n4n4", "m3l0n", "str4wb3rry").
How would you crack these passwords?
- CHALLENGE: Now say the user was required to have a special character in their
password. The user is still lazy, and a) only includes one special character
in their password, and b) uses only #, !, or $ as their character. How might
you write code to crack this password? Try cracking the following passwords if
you think you've written something that works:
  - b4Ll!
  - s$t0rE
  - W0r#ld
  - wOnd3r$
  - #w0mAn

#### Credits
Project by Will Rivitz, README by Rebecca Gold
#### Creator Notes
We used Python's hashlib library to create a password hash. This allows
us to keep the password inside of the "application" as well as to easily
modify the password as needed.
Questions/comments/feedback/concerns? Email will.rivitz [at] girlswhocode [dot] com before
August 17th, 2018, or wrivitz [at] gmail [dot] com after!
