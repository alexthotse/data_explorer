0.Where do files come from? Well, they come from the web
There's a command from the shell that allows you to download files from the web

01. That command stands for curl as in C URL => See URL => explaining the joke (Hahahaha!!)
You can use curl to get any web page but what it does it  shows you the source code of the web page. 	
To get it to write to a file we use -o followed by the file name we would like to save {google.html}
Common  pattern for shell commands : starts with the name of the command (curl) ; followed by some options {-o google.html -L}; then foolwed by the object we want to operate on like the URL {'www.google.com'}
02.  Starts with curl
02.  Ends with the url 'https://tinyurl.com/zeyq9c'
03.  Follow the redirects {-L}
03. We want to save it as dictionary.txt {-o dictionary.txt}
04. We put sungle quotes around urls because there is special characters in the url

