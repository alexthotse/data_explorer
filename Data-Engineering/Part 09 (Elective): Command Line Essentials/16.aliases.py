01. aliases = Its a way for making shell commands shorter
	i.e. alias ll='ls -la'
02. similar to variables {no spaces between the = sign}
03. everytime you use the alias command ll; it will in fact run the longer command {ls -la}
04. If you want to see all your aliases run the 'alias' command with no arguments
05. You can use aliases as regular commands
	i.e. ls -la  /usr/bin gets turned into ll /usr/bin
06. Any options you put after the alias when you use it will just go on the end of the command
07. This will only last as long as theterminal window is running
08. If you want them to be there permanently; you put them in your .bash_profile/.bashrc file 
	i.e. alias ll='ls -la'
	i.e. alias cl='curl -l'
	i.e. alias ..='cd ..'
	i.e. alias ...='cd ...' {never seen it=research!!}
	i.e. alias now='date +"%T"'
	i.e. alias sl='ls' {pretty smart commands you can add your own too!!!}
