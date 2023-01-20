# situation

We have a cookie called i am admin which is false in md5 (found with hash type detector online)
we replace it by true and it works

cookie
	I_am_admin=68934a3e9455fa72420237eb05902327

https://www.md5online.org/md5-encrypt.html

Found : false
(hash = 68934a3e9455fa72420237eb05902327)

The MD5 hash for true is : b326b5062b2f0e69046810717534cb09

inspect go to storage modify value

Good job! Flag : df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3

# probleme

evryobdy can pretend to be admin 

# fix 
 ask for password each time to connect as admin. use jwt token instead of one string in cookie and verify on server side is integrity