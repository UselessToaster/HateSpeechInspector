from google.cloud import language
import random


def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    score=sentiment.score
    magnitude=sentiment.magnitude
    for k, v in results.items():
        print(f"{k:10}: {v}")
    return(score,magnitude)

text=str(input("Enter notification text to analyze: "))
b,c=analyze_text_sentiment(text)

print(b)




popupvar = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SAMURA</title>
    </head>
    <body>
        <style type="text/css">
            body {
               height: 30px;
               width: 200px;
            }
        </style>
        <font size="12">SAMURA </font size>
        <center>The Hate Speech Inspector</center>
        <hr size="5" width="50" color="black">  
        <p style="padding: 10px; border: 2px solid rgb(70, 85, 214);"> %s </p>
        <p style="padding: 10px; border: 2px solid rgb(70, 85, 214);">TEXT from python</p>
        <p style="padding: 10px; border: 2px solid rgb(70, 85, 214);">TEXT from python</p>
    </body>
</html>'''

html = open("popup.html", "w")

#overwrites html file and replaces  s% with the given string (make sure html syntax is correct)
#html.write(popupvar % "<h1> Notificatoin Center </h1>")

if b>-1 and b<-0.25:
    choices=["This is a bad response.","Wow... THEY messaged you again.","The NERVE of them to message you like that!"]
    a=random.choice(choices)
    print(a)
    #html.write(popupvar)
    html.write(popupvar % a)

elif b>=-0.25 and b<0.5:
    choices=["This is a neutral response.","Alright, someone wants your attention.","Somebody would like to speak with you."]
    a=random.choice(choices)
    print(a)
    #html.write(popupvar)
    html.write(popupvar % a)
    
elif b>=0.5 and b<=1:
    choices=["This is a good response.","You got a message from a friend! They're so sweet.","Your friend wants to talk. I like them!"]
    a=random.choice(choices)
    print(a)
    #html.write(popupvar)
    html.write(popupvar % a)

html.close()
