01. The shell isn't only a  CLI but a programming language
02. Files containing shell commands are called Shell Scripts
03. The can be simple like 1 or 2 commands just like you write in the shell prompt or
	they can be long and complex programs made of many functions.
04. But we are not gonna look into shell programming in this course ;-(
05. It's very useful for everyone who uses the shell & thats customizing the shell itself.
06. It really common for shell users to install programs into a sub-directory of their home directory called bin{which stands for binary}
07. But the shell doesn't come pre-configured to know that there are any commands there 
08. If you have a program stored in bin/magic & you want to run it from the shell: you would have to type the directory out as well as the command name
09. You can get around that by adding the directory to your PATH variable.
	i.e. PATH=$PATH:/Users/students/bin
		magic ==> prints the file 
		But that gets reset everytime you restart the shell
10. In order to make that sticky: you have to putit into the shells configurations file
11. For historical reasons there are a few different files that the Bash Shell can run on start-up to get it's configuration.
12. On a Mac or Windows system with git bash, the shell and every terminal you open will run the commands in the file called .bash_profile(Mac & Windows)
13. But on a Linux System bash_profile is only run for some sessions specifically logging shell sessions.
14. Non-logging in sessions run a file called .bashrc(Linux) instead.
15. This inconsistency can be a problem if you want to use the same Shell configuration on different Operating Systems.
	One popular way to get around this is to put a statement in your .bash_profile saying if thereis a file called .bashrc run that file;
		if [-f ~/.bashrc ] ; then
			source ~/.bashrc
		fi
16. But if you're on Mac or Windows you can use the .bash_profile without worrying about that
17. Any command you put in this configuration file will be run every time you start the shell
	That included variable assignments like change in $dollar sign path {PATH=$PATH:/Users/students/bin}
18. It can also inclued any thing you would like to see at the start of your shell session.
	Maybe you want to see the date and a friendly message:
		Add: date
		     echo "hey there!"
	When you open a new shell; the commands get run #killed it!!! 
