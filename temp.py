# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from flask import Flask,request,render_template
import pickle
import os
from collections import Counter
app=Flask(__name__)
model=pickle.load(open('spam.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    x=request.form.values()
    path = "C:/Users/yogevohr/project1/spam_classifier/emails/"
    Files=os.listdir(path)
    emails=[path+email for email in Files ]
    words=[]
    for email in emails:
        with open(email,encoding="ISO-8859-1") as f:
            text=f.read()
        words +=text.split(" ")            
        
    for i in range(len(words)):
        if not words[i].isalpha():
            words[i]=""
    dictionary=Counter(words)
    del dictionary[""]
    d=dictionary.most_common(1000)  
    temp=x.split(" ")
    x=temp 
    test=[]
    for word in d:
       test.append(x.count(word[0]))
    result=spam.predict([x])
    return render_template('index.html', prediction_text="text")
if __name__ =="__main__" :
   temp.run(debug=True)