import re

"""
.       any char except \n
*       0 or more reps
+       1 or more reps
?       0 or 1 reps
{m}     m reps
{m,n}   m-n reps
^       match start
$       match end
[]      set of char - include
[^]     !set of chat - exclude
"""

email = input("What's your email? ").strip()

if re.search(r"^[^@]+@[^@]+\.com$", email):
    print("Valid")
else:
    print("Invalid")