# situation

## http://192.168.56.101/?page=recover#

The HTML code of the form looks like this :
 ```
 <form action="#" method="POST">
	<input type="hidden" name="mail" value="webmaster@borntosec.com" maxlength="15">
	<input type="submit" name="Submit" value="Submit">
</form>
```
It is noticed that the value of the email is stored in the post with a hidden type, which leaves the field open for changing the email and retrieving it to our email address. 

apres avoir changer le mail on clicque sur submit et on obtient se flag : 1D4855F7337C0C14B6F44946872C4EB33853F40B2D54393FBE94F49F1E19BBB0

# problem

he problem is that the email address is stored in the HTML code as a hidden input field in a form, which means that an attacker could change the email address and submit the form to receive the password recovery link at their own email address. This could allow them to gain unauthorized access to someone else's account.

# solution

A solution to this issue could be to store the email address on the server-side instead of in the client-side HTML code. This way, the email address cannot be easily tampered with by an attacker. Additionally, proper validation and sanitization of user input can be implemented to ensure that the email address submitted is valid and belongs to the intended user.
