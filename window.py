def border_r():
	border = '-' * (len(windowtitle + greeting + question3) + 3)

	return(border)

def question():
	return("Hello my name is Darren what is your name? ")

windowtitle = raw_input(question())

greeting = "|Hello,"
question3 = "How was your day?|"


print("%s" %(border_r()))

print "%s %s, %s" %(greeting, windowtitle, question3)

print(border_r())

day = raw_input("")

if day = ("Good", "good", "great", "amazing", "Amazing" 'Wonderful', "wonderful")