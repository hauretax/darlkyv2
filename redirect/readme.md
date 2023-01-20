# situation

## evrywhere on bottom

wwe see link balise use link whit redirect <a href="index.php?page=redirect&amp;site=instagram" class="icon fa-instagram"></a>

so we can build adress with is domain name like 
http://192.168.56.101/index.php?page=redirect&site=randomdarksite

B9E775A0291FED784A2D9680FCFAD7EDD6B8CDF87648DA647AAF4BBA288BCAB3

# probleme 
An inattentive user might think they are clicking on a trustworthy link and end up on a malicious website.

# fix 
Instead of allowing any parameter to be passed in the URL, only allow redirections to a specific set of known good pages.
Verify that the redirect request is coming from the same domain as the current page, to prevent redirection from external sources.