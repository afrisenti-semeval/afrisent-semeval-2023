#!/usr/bin/env python

# load required packages
import sys
import os
import pandas as pd
from sklearn.metrics import f1_score, precision_score, recall_score

def createHTML(output_dir, f1, m_f1, precision, m_precision, recall, m_recall):
	htmlOutputDir = os.path.join(output_dir, "html")
	if not os.path.exists(htmlOutputDir):
		os.makedirs(htmlOutputDir)
	
	htmlString = f'''<!DOCTYPE html>
	<html>
		<head>
		    <title>Detailed Result</title>
		</head>
		<body>
			<p>
				Evaluation Result
			</p>
			<p>
                Average (weighted)<br/>
				Precision: {precision} <br/>
				Recall: {recall} <br/>
				F1: {f1} <br/>
            </p>
			<p>
                Average (macro)<br/>
				Precision: {m_precision} <br/>
				Recall: {m_recall} <br/>
				F1: {m_f1} <br/>
            </p>
		</body>
	</html>'''

	with open(htmlOutputDir+"\\detailed_results.html", "w") as htmlfile:
	    htmlfile.write(htmlString)

sys.stdout.write("Starting scoring program. \n\n") # participants can read these messages in the stdout.txt and errors in the stderr.txt for their submission

# load input and output directories, which are passed as arguments as per the metadata file
input_dir = sys.argv[1]
output_dir = sys.argv[2]

ref_dir = os.path.join(input_dir, 'ref')
gold_dir = os.path.join(ref_dir, os.listdir(ref_dir)[0])

lang = gold_dir.split('/')[-1].split('_')[0]

if lang.find('gold') != -1:
    sys.exit('Sorry, the dataset for this task has not been uploaded yet but will be available very soon. Check the competition website later for updates.')

submission_dir = os.path.join(input_dir, 'res')
if not os.path.exists(submission_dir):
    sys.exit('Could not find submission file {0}, please check the submission file name.'.format(submission_dir))

# validate submission and gold standard data directories
if not os.path.isdir(submission_dir):
    sys.exit("Submission directory doesn't exist")
if not os.path.isdir(ref_dir):
    sys.exit("Evaluation data directory  doesn't exist")

# create output directory
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

sys.stdout.write("File directories are valid. ")

# load submission
sys.stdout.write(str(os.listdir(submission_dir)))
sys.stdout.write("\n\n")
submission_df = pd.read_csv(os.path.join(submission_dir, 'pred_' + lang + '.tsv'), sep='\t') # the first file in the submission zip is expected to be the submission csv
sys.stdout.write("Loaded submission. \n")

# load gold standard data
gold_df = pd.read_csv(gold_dir, sep='\t') # the first file in the gold standard zip is expected to be the gold standard csv
sys.stdout.write("Loaded gold standard data. \n\n")

# validate submission:
# correct columns exist
if "ID" not in submission_df.columns:
    sys.exit('ERROR: Submission is missing ID column, or ensure the name is ID not id.')
if "label" not in submission_df.columns:
    sys.exit('ERROR: Submission is missing label column.')

# length matches gold standard data
if (len(submission_df) != len(gold_df)):
    sys.exit('ERROR: Number of entries in submission does not match number of entries in gold standard data. Are you submitting to the right task?')

# valid labels
unique_submission_labels = submission_df['label'].unique()
unique_gold_labels = gold_df['label'].unique()
for i in unique_submission_labels:
    if i not in unique_gold_labels:
        sys.exit('ERROR: The column label contains invalid label strings. Please see the Submission page for more information.')


sys.stdout.write("Submission contains correct column names (ID and label). \n")
sys.stdout.write("Number of entries in submission matches number of entries in gold standard data. \n\n")
sys.stdout.write("Predicted labels are all valid strings. \n")

# sort submission and gold standard data by Rewire ID, so that labels match predictions
submission_df = submission_df.sort_values("ID")
gold_df = gold_df.sort_values("ID")

sys.stdout.write("Labels in gold standard data: ")
sys.stdout.write(str(sorted(pd.unique(gold_df.label))))
sys.stdout.write("\n")

sys.stdout.write("\nLabels in submission: ")
sys.stdout.write(str(sorted(pd.unique(submission_df.label))))
sys.stdout.write("\n\n")

# calculate macro F1 score for the submission relative to the gold standard data
f1 = f1_score(y_true = gold_df["label"], y_pred = submission_df["label"], average="weighted")
recall = recall_score(y_true = gold_df["label"], y_pred = submission_df["label"], average="weighted")
precision = precision_score(y_true = gold_df["label"], y_pred = submission_df["label"], average="weighted")

m_f1 = f1_score(y_true = gold_df["label"], y_pred = submission_df["label"], average="macro")
m_recall = recall_score(y_true = gold_df["label"], y_pred = submission_df["label"], average="macro")
m_precision = precision_score(y_true = gold_df["label"], y_pred = submission_df["label"], average="macro")

# write macro F1 score to a "scores.txt" file as required by CodaLab
with open(os.path.join(output_dir, 'scores.txt'), 'w') as output_file:
    output_file.write("avg_precision:{}\n".format(precision)) 
    output_file.write("avg_recall:{}\n".format(recall))
    output_file.write("avg_f1_score:{}\n".format(f1))

    output_file.write("macro_precision:{}\n".format(m_precision))
    output_file.write("macro_recall:{}\n".format(m_recall))
    output_file.write("macro_f1_score:{}\n".format(m_f1))

sys.stdout.write("Submission evaluated successfully. \n\n")
sys.stdout.write("Average (weighted). \n")
sys.stdout.write("Precision:{}\n".format(precision)) 
sys.stdout.write("Recall:{}\n".format(recall))
sys.stdout.write("F1:{}\n\n".format(f1))

sys.stdout.write("Average (macro). \n")
sys.stdout.write("Precision:{0}\n".format(m_precision))
sys.stdout.write("Recall:{0}\n".format(m_recall))
sys.stdout.write("F1:{0}\n".format(m_f1))

createHTML(output_dir, f1, m_f1, precision, m_precision, recall, m_recall)