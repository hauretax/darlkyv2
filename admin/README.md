# situation

We download all files in site:

wget -r http://192.168.56.101/

in robots.txt we go to: 

http://192.168.56.101/whatever

we download the file htpasswd on the page:

cat htpasswd
root:437394baff5aa33daa618be47b75cb49

do a md5 decrypt

437394baff5aa33daa618be47b75cb49 : qwerty123@

go to ip/admin:
http://192.168.56.101/admin/

root 
qwerty123@

The flag is : d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff 

# probleme

we can connect to admin easly

# fix

Use complexe password which can't be easily decrypted with strong encryption standard, don't let the password file on the internet.
we can use 2 factor authentication