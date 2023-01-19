# situation

## http://192.168.56.101/index.php?page=survey


```
<select name="valeur" onchange="javascript:this.form.submit();">
						<option value="1">1</option>
						<option value="2">2</option>
						<option value="3">3</option>
						<option value="4">4</option>
						<option value="5">5</option>
						<option value="6">6</option>
						<option value="7">7</option>
						<option value="8">8</option>
						<option value="9">9</option>
						<option value="10">10</option>
					</select>
```
- Change value="2" to value="2000"
- Select the second option
- FLAG IS 03A944B434D5BAFF05F46C4BEDE5792551A2595574BCAFC9A6E25F67C382CCAA

# problem

 it allows an attacker to potentially submit malicious or unauthorized data.

 # solution

 To prevent these issues, it is important to validate and sanitize all user input on the server-side. This can include checking for proper format, length, and range of the input, as well as ensuring that it does not contain any malicious characters or code. 
