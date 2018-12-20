# vision
Voice assistant

How to use:
1: Download source code.
2: Run start.py
3: Say listen for start listening commands

# code working:
Virtual Vision :
Voice assistant:
	Language used :- Python
Python Libraries Used :- 
1.	Speech Recognition : For using voice to text conversion. (online using google api)
2.	Smtplib : For sending e mail
3.	Pynput : for using keyboard (pressing keys)
4.	Sounder : for approximation of Keywords
5.	Gtts : text to speech conversion. (offline)
6.	Sys
7.	OS

Code of Voice assistant:
	Start form start.py:- 2 thread starts 1. Background thread 2. Application thread.
	1. Background thread: continuously checking for hotword (listen). If hotword arrives Background thread pause and it start application thread.
	2. Application thread:  continuously checking for main menu options:-
		1. ms-word 2.e-mail 3.file searching 4.chrome 5.mouse hover 6.writing
If any of above option arrives it start module of that particular operation.
1. ms word: 	now  we are in sub menu option:- we can choose any ms word options.
		After exit we are again in main menu.
2. e mail: 	first application ask for receiver e mail address then messege that user want to send. That’s it mail send.
3. File searching:  application asks for file name and then after searching it gives location of that file by speaking path.
4. Chrome: we can use almost all basic features for chrome browser for browsing internet.
5. Mouse hover:  It activate window narrator that read text under the pointer of mouse.
6. writing :- this option is for writing text on any text box.
:-)

# Note: you can give voice commands in hindi language also
