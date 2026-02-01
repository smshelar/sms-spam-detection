import streamlit as st
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import pickle
import string
import nltk

def ensure_nltk():
  resources = [
    "punkt",
    "punkt_tab",
    "stopwords"
  ]

  for r in resources:
    try:
      nltk.data.find(r if "/" in r else f"tokenizers/{r}")
    except:
      nltk.download(r)


ensure_nltk()

tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)

  y = []
  for i in text:
    if i.isalnum():
      y.append(i)

  text = y[:]
  y.clear()

  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)

  text = y[:]
  y.clear()

  ps = PorterStemmer()

  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)

st.title("Email/SMS spam Classifier")

input_sms = st.text_area("Enter the message")

if st.button('predict'):

  # 1. Preprocess
  transform_sms = transform_text(input_sms)

  # 2. vectorise
  vector_input = tfidf.transform([transform_sms])

  # 3. predict
  result = model.predict(vector_input)[0]

  # 4. display

  if result == 1:
    st.error('Spam ❌')
  else:
    st.success('Not Spam ✅')