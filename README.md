# Automated Wordle Solver
 
This program will open the Wordle website, solve the Wordle, and send the result as a text message.

Changes to the Wordle website might make parts of the code stop working. To fix this, the HTML format of the website may have to be looked at, and the code modified accordingly. The avoid_rules function is used to close any pop-ups that occur when the website is opened. The press_letter function is used to press a letter. The get_hints function is used to get the data about the colors and letters that have been entered. 

In order to send the result as a text message, some information is required. The program sends the data as an email from the email the user provides and sends the message to an email associated with a phone number. In order for this to work, 4 variables have to be assigned by the user in credentials.py. The first is the phone number you want to send the message to. The second is the provider associated with the number. The third is the email that you want to use to send the message. The fourth is the access token that the program will use to access the email.

The file bestwords.py contains a variety of possible heuristics that can be used to evaluate the best possible guess from a list of valid words. The heuristic being used can be changed by modifying the select_best function and changing the heuristic function that is called.
