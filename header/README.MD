# situation

## http://192.168.56.101/?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f

In the footer we have a link to a page
<a href="?page=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f">

when you use curl you see in the comments:

You must come from : "https://www.nsa.gov/".

use this browser : "ft_bornToSec". It will help you a lot.

let's set the right user agent and the referer page in our curl

curl -A "ft_bornToSec" -e "https://www.nsa.gov/" http://127.0.0.1:8080/\?page\=b7e44c7a40c5f80139f0a50f3650fb2bd8d00b0d24667c4c2ca32c88e13b758f

The flag is : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188


# problem
The problem here is that it is explained how to trick the website in the comments...
You shouldnt do any action based on where the person comes from except from analytics.

# fix

Do not give any sensitive information based on where the request comes from as it can be forged. A request with the right header can be made via curl