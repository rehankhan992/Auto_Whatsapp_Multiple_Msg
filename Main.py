import pywhatkit as pk
import time
import keyboard
#Auto text file contains messages to be sent. Specify the full path with extension.
with open("D:\Auto.txt", "r") as Quotes:
	lines = Quotes.readlines()
for i in lines:
	pk.sendwhatmsg_instantly(f"+91999999999",i)
	time.sleep(5)
	keyboard.press_and_release('ctrl+w')
