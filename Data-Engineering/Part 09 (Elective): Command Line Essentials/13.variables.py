01. The shell is actually a programming language & just like Javascript & python;
	it jhas variables they lokk a little different
02. Name & an equals sign, followed by the value you want to have
	numbers='one two three' {no spaces between the = sign}
03. If you want to refer to the  variable:
	echo $numbers === one two three
04. There are 2 different kinds of variables in the shell 
	1. One them is called a shell variable {i.e. echo $LINES x $COLUMNS}
		==> 24 x 96
	The lines and columns variables are just internals to the shell program  itself
	2. The other kind is called an enviroment variable:
	Enviroment variables are shared with programs that you run within the shell 
	One of the most important variables is the PATH variable:
	echo $PATH ==> /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin { tells you system where your program files are}  
	For instance when we type ls, thencomputer fetches the command from here!
/bin/ls ==> dictionary.txt {thats where ls is located}
the direcrories in the path variable are separated by colons & the shell searches them  starting with the first one and then proceeding to the right until it finds the commands you want to enter: & thats how the shell is able to find the command ls when i run it
Some instructions will tell you to add a directory to your path so programs in it can be found
To add the new directory to the end of your path, you do it like this:
	PATH=$PATH:/new/dir/here
Disadvantage: if you do it like that, that change will only last until you close the shell.
We will take a look at where we do this if we want to make it permanent 
