from textblob import TextBlob
a="computar"
print("original text : ",a)
b=TextBlob(a)
print("corrected text: " , b.correct())