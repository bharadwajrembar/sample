import os

#This is a comment
os.system('sudo /bin/bash -c \'mkdir ~/test\'')
os.system('sudo /bin/bash -c \'cd ~/test && touch something.txt && echo \'worked\' >> another_test.txt\'')
