Hi GWC facilitators and staff! We (the 2018 SIP teaching team at EY in Seattle)
were discussing different kinds of hacking with our class, and they were
particularly interested in learning different ways that hackers attack
users. As such, we decided to spice up the dictionary attack activity a little -
instead of just checking a password for its strength, we made a rudimentary
"password-protected application" in Python that used a fairly insecure password,
and our class spent some time writing a Python script that would generate a
password dictionary to "crack" the password.

Here are the rules we used to generate the password:
1. Our application stipulates, much like the real world, that each
password must contain at least one capital letter and one number.
2. Our user is lazy, so they created their password by selecting one of
the 1000 most common words in the English language, capitalizing a random
letter, and converting another letter to a number based on the following:
  -an "a" can be converted to a 4
  -an "e" can be converted to a 3
  -an "o" can be converted to a 0
  -an "i" can be converted to a 1
So, each password has exactly one capital letter and exactly one number.

FILES INCLUDED:
-1000words.txt: the 1000 most common words in the English language
-passwordentry.py: the "password-protected application"

INSTRUCTIONS:

To try and guess the password yourself, run the following in your command prompt:
>> python passwordentry.py

To guess the password with a list of passwords of your choice, run the following in
your command prompt:
>> python passwordentry.py < [your password text file]

To generate your dictionary for the attack, run the following
in your command prompt:
>> python dictionarygenerator.py < 1000words.txt > [an output file of your choice]

To use that generated dictionary to crack the password, run the
following in your command prompt:
>> python passwordentry.py < [the same output file from above]

Try using your own password! Here are the steps to do that:
1. replace "#a string of your choice" in hasher.py with whatever
password you want to use, and run the following:
>> python hasher.py
2. copy the entire output (including the b and both single-quotes)
and replace the current value of myHashedPassword in passwordentry.py
with that output

Then, try running your password attack again!

QUESTIONS TO CONSIDER:

-What passwords are crackable?
-What passwords aren't?
-Are the following passwords crackable:
  -b4Nk
  -b3causE
  -c3ll
  -billion
  -Language
-How would you modify your program to crack any of the uncrackable passwords above?
-How would you modify your program to crack passwords like "li9hT",
"Ma9azine", and "pRo9ram"? What about passwords like "so1diEr", "nEar1y",
and "suCcessfu1"?
-Suppose the user were smarter, and made every character that could be
converted to a number that number (e.g. "b4n4n4", "m3l0n", "str4wb3rry").
How would you crack these passwords?
-CHALLENGE: Now say the user was required to have a special character in their
password. The user is still lazy, and a) only includes one special character
in their password, and b) uses only #, !, or $ as their character. How might
you write code to crack this password? Try cracking the following passwords if
you think you've written something that works:
  -b4Ll!
  -s$t0rE
  -W0r#ld
  -wOnd3r$
  -#w0mAn

NOTES:
We used Python's hashlib library to create a password hash. This allows
us to keep the password inside of the "application" as well as to easily
modify the password as needed.
Questions/comments/feedback/concerns? Email will.rivitz [at] girlswhocode [dot] com before
August 17th, 2018, or wrivitz [at] gmail [dot] com after!
