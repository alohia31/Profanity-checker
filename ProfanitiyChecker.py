import urllib

def read_text():
    quotes = open(r"/Users/user/Desktop/movie_quotes.txt")
    content = quotes.read()
    print(content)
    quotes.close()
    check_profanity(content)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print (output)
    connection.close()

    if "true" in output:
        print("Profanity Detected")
    elif "false" in output:
        print("Profanity not detected")
    else:
        print("error reading document")

read_text()
