# situation

## http://192.168.56.101/?page=feedback


Wr test if we can enter messages then we test if we can put js script inside and it is interpreted by navigator.
It is interpreted and the site detct that we have sent a balise there and give us the flag.

put <div>test</div> in message
and it print a flag THE FLAG IS : 0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E

# problem 
Anybody can post a message with malicous js.
it s xss attack somone can put javascript and steal usr data

# solution
You should never trust user input so we need to sanityze data. 
We take data and clean it before recording it to the server. In order to do that you can:
filter user input whith plugins
Encode data on output 