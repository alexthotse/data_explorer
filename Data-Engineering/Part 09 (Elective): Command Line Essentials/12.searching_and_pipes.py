01. There is a shell command called grep that knows how to search a text file for line with particular content
02. grep shell dictionary.txt ==> It will read the file and output all the lines that contain that word.
03. But what if there are more lines with that word?
04. we can ask the shell to send the output of grep into the less command we can do this with the pipe character {|} 
	grep shell dictionary.txt | less {now you can consume the information easily}
05. The grep command reads the input file and prints any file that matches the pattern
06. But the shell has arranged things so the output file doesn't go directly to the terminal. 
07. Instead it gets send to the less program which displays the lines of the  terminal one page at a time.
08. To read this command out loud you'd say; /grep for shell in dictionary.txt and pipe it to less/
09. grep can also operate on other input from another program 
10. curl -L https://tinyurl.com/zeyq9vc | grep fish { for instance you can pull a file from the web and immediately grep it for a particular pattern without having to save it to a file first.
	It would  display on the terminal , though some outputs will get mixed in but if we saved it to a file it would be fine.
11. If we kust want to count the amount of words in the document we would use  wc -l
12. wc stands for word count program and then we can ask it to count the lines with the -l option
	curl -L https://tinyurl.com/zeyq9vc | grep fish | wc -l
		output ==> 105 lines
13.Another option is the give grep -c for count
        curl -L https://tinyurl.com/zeyq9vc | grep -c fish 

