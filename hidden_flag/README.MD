# situation

We download all website file to see if there is anything interesting:

wget -r http://192.168.59.4/

in robots.txt which is a file asking for no index on files we see a .hidden url with many files and readme's

cat 192.168.59.4/robots.txt 

So i made a script to find if there is a flag 
we make request to get all possible combiantions then ddl all readme and find string flag in content and:


python getflag.py 
string exist in a file
http://192.168.59.4/.hidden/whtccjokayshttvxycsvykxcfm/igeemtxnvexvxezqwntmzjltkt/lmpanswobhwcozdqixbowvbrhw//README
Hey, here is your flag : d5eec3ec36cf80dce44a896f961c1831a05526ec215693c8f2c39543497d4466

22764


# Fix

Robots.txt is here to tell search engines not to look here, it's not hidding anything. 
It's the same as .files on unix they hide from your sight but are still there.
Don't pu any valueable infos in a path in robots.txt