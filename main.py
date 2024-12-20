

import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
nltk.download('punkt_tab')
nltk.download('stopwords')
ps=PorterStemmer()
cv=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))
st.title("EMAIL SPAM CLASSIFIER")
input_SMS=st.text_input("ENTER THE MESSAGE")
def transform_text(text):
  text=text.lower()
  text=nltk.word_tokenize(text)
  y=[]
  for i in text:
    if i.isalnum():
      y.append(i)
  text=y[:]
  y.clear()
  for i in text:
    if i not in stopwords.words("english") and i not in string.punctuation:
      y.append(i)
  text=y[:]
  y.clear()
  for i in text:
    y.append(ps.stem(i))
  return " ".join(y)
if st.button('Predict'):
  transformed_sms=transform_text(input_SMS)
  vector_input=cv.transform([transformed_sms])
  result = model.predict(vector_input)[0]
  if result==1:
      st.header("SPAM")
  else :
      st.header("NOT SPAM")