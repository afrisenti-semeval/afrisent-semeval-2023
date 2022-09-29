# This code was adopted from https://huggingface.co/siebert/sentiment-roberta-large-english

# Import required packages
import torch
import os
import pandas as pd
import numpy as np
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter, ArgumentTypeError
import warnings
warnings.simplefilter("ignore")

# Create class for data preparation
class SimpleDataset:
  def __init__(self, tokenized_texts):
    self.tokenized_texts = tokenized_texts
  
  def __len__(self):
    return len(self.tokenized_texts["input_ids"])
  
  def __getitem__(self, idx):
    return {k: v[idx] for k, v in self.tokenized_texts.items()}

def validate_datafile(astring):
  if not astring.endswith('.tsv'):
    raise ArgumentTypeError("%s: is an invalid file, provide a tsv." % astring)
  return astring

parser = ArgumentParser(description="Sentiment Classification Prediction", formatter_class=ArgumentDefaultsHelpFormatter)

parser.add_argument("--model_path", type=str, required=True, help="path to a trained model")
parser.add_argument("--file_name", type=validate_datafile, required=True, help="path to unlabeled tweets to predict")
parser.add_argument("--text_column", type=str, default='text', help="path to save predictions")
parser.add_argument("--lang_code", type=str, default='text', help="language code")
    
args = parser.parse_args()

# Load tokenizer and model, create trainer
model_name = args.model_path
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
trainer = Trainer(model=model)

# Import data from csv-file stored on Google Drive
file_name = args.file_name
text_column = args.text_column

df_pred = pd.read_csv(file_name, sep='\t')
ids = df_pred.iloc[:,0].astype('str').tolist()
pred_texts = df_pred[text_column].astype('str').tolist()

# Tokenize texts and create prediction data set
tokenized_texts = tokenizer(pred_texts, truncation=True, padding=True)
pred_dataset = SimpleDataset(tokenized_texts)

# Run predictions
predictions = trainer.predict(pred_dataset)

# Transform predictions to labels
preds = predictions.predictions.argmax(-1)
labels = pd.Series(preds).map(model.config.id2label)

# Create submissions files directory if not available
if os.path.isdir(model_name):
  print('Data directory found.')
  SUBMISSION_PATH = os.path.join(model_name, 'submission')
  if not os.path.isdir(SUBMISSION_PATH):
    print('Creating submission files directory.')
    os.mkdir(SUBMISSION_PATH)
else:
  print(model_name + ' is not a valid directory or does not exist!')

# Create DataFrame with texts, predictions, and labels
df = pd.DataFrame(list(zip(ids,pred_texts,preds,labels)), columns=['ID', 'text', 'pred', 'label'])
df.to_csv(os.path.join(SUBMISSION_PATH, 'predictions.tsv'), sep='\t', index=False)

df = pd.DataFrame(list(zip(ids,labels)), columns=['ID', 'label'])
df.to_csv(os.path.join(SUBMISSION_PATH, 'pred_' + args.lang_code + '.tsv'), sep='\t', index=False)