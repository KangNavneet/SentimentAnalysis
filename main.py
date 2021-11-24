from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient


from azure.identity import DefaultAzureCredential

import pandas as pd

document1= pd.read_csv('sentimentTweet.csv', header=None, index_col=0, squeeze=True).to_dict()
print(document1)

# importing module
import csv

# csv fileused id Geeks.csv
filename = "sentimentTweet.csv"

documents=[]

# opening the file using "with"
# statement
with open(filename, 'r') as data:
    for line in csv.reader(data):
        print(line[1])
        documents.append(line[1])




credential = AzureKeyCredential("2096ecab40d64070abceef0bf330802c")

text_analytics_client = TextAnalyticsClient(endpoint="https://twittercognitive.cognitiveservices.azure.com/", credential=credential)

# documents = [
#     {"id": "1", "language": "en", "text": "I hated the movie. It was so slow!"},
#     {"id": "2", "language": "en", "text": "The movie made it into my top ten favorites. What a great movie!"},
#
#
# ]

response = text_analytics_client.analyze_sentiment(documents , language="en")
result = [doc for doc in response if not doc.is_error]
count=0
for doc in result:
    print("\n"+ documents[count] +":::: ")
    count=count+1
    print("Overall sentiment: {}".format(doc.sentiment))
    print("Scores: positive={}; neutral={}; negative={} \n".format(
        doc.confidence_scores.positive,
        doc.confidence_scores.neutral,
        doc.confidence_scores.negative,
    ))


#Codeeeee
documents=[]
id=[]
i = 0 # counter variable as it only permits 10 record for analyze
k=""
with open(filename, 'r') as data:
    for line in csv.reader(data):
      if i<10:
        print(line[1])
        documents.append(line[1])
        k = str(i)
        id.append(k)
        i= i+1


updated_csv = 'updated_csv.csv'

header = ['id','message','positive','neutral','negative']
with open(updated_csv,'w',encoding='UTF8') as f:
  writer = csv.writer(f)
  writer.writerow(header)
  for (doc,i,j) in zip(result,id,documents):
    print("Overall sentiment: {}".format(doc.sentiment))
    print("Scores: positive={}; neutral={}; negative={} \n".format(
        doc.confidence_scores.positive,
        doc.confidence_scores.neutral,
        doc.confidence_scores.negative,
    ))
    writer.writerow([i,j,doc.confidence_scores.positive,doc.confidence_scores.neutral,doc.confidence_scores.negative])


