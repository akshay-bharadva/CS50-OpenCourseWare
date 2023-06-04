import re

"""
*** expressions
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
A|B     A or B
(...)   group (i.e, (com|org|net|edu))
(?...)  non-capturing version

*** char sets
\d      decimal digits (i.e, [0-9])
\D      non decimal digits (i.e, [^0-9])
\s      whitespace chars
\S      non whitespace chars
\w      word chars - alphanumeric symbol or _ (i.e, [a-zA-Z0-9_])
\W      non words chars (i.e, [^a-zA-Z0-9_])
"""

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.com$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
