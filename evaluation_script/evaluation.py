#!/usr/bin/env python
import sys
import os.path
import sklearn.metrics

def check_file(path, correct_number_of_columns):
    f = open(path, 'r')
    first_line = f.readlines()[0].split("\t")
    f.close()
    if (len(first_line) != correct_number_of_columns):
        sys.exit('Column format problem.')
    if (first_line[0].lower() != 'id'):
        sys.exit('Your submission has no header. Please provide the header as: id[tab]pred_label')
    

def evaluate(pred, gold):
    
    check_file(pred, 2)
    check_file(gold, 3)

    print('Files format checked successfully')

    with open(pred, "r") as f:
        pred_lines = f.readlines()
    
    with open(gold, "r") as f:
        gold_lines = f.readlines()
    
    pred_lines = pred_lines[1:]
    gold_lines = gold_lines[1:]

    if(len(pred_lines)==len(gold_lines)):       
        # align tweets ids with gold scores and predictions
        data_dic={}
        
        for line in gold_lines:
            parts=line.split('\t')
            if len(parts)==3:
                data_dic[parts[0]]=[parts[2]]
            else:
                sys.exit('Format problem.')
        
        for line in pred_lines:
            parts=line.split('\t')
            if len(parts)==2:  
                if parts[0] in data_dic:
                    try:
                        data_dic[parts[0]].append(parts[1])
                    except ValueError:
                        sys.exit('Cannot append label.')
                else:
                    sys.exit('Invalid tweet id. Make sure the submission is correct.')
            else:
                sys.exit('Format problem.')
            
        
        # lists storing gold and prediction scores
        gold_scores=[]
        pred_scores=[]
            
        for id in data_dic:
            if(len(data_dic[id])==2):
                gold_scores.append(data_dic[id][0])
                pred_scores.append(data_dic[id][1])
                
            else:
                sys.exit('Repeated id in test data.')
      
        # compute metrics
        eval_report = sklearn.metrics.classification_report(gold_scores, pred_scores, output_dict=True)

        return (eval_report["weighted avg"]["precision"], eval_report["weighted avg"]["recall"], eval_report["weighted avg"]["f1-score"])
       
    else:
        sys.exit('Predictions and gold data have different number of lines.')
        

def main(argv):
    #https://github.com/Tivix/competition-examples/blob/master/compute_pi/program/evaluate.py
    # as per the metadata file, input and output directories are the arguments

    [input_dir, output_dir] = argv
    
    # unzipped submission data is always in the 'res' subdirectory
    # https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions

    ref_dir = os.path.join(input_dir, 'ref')
    gold_standard = os.path.join(ref_dir, os.listdir(ref_dir)[0])

    lang = gold_standard.split('/')[-1].split('_')[0]
    
    submission_path = os.path.join(input_dir, 'res', 'pred_' + lang + '.tsv')
    if not os.path.exists(submission_path):
        sys.exit('Could not find submission file {0}, please check the submission file name.'.format(submission_path))
    
    eval_scores = evaluate(submission_path, gold_standard)
    
    # the scores for the leaderboard must be in a file named "scores.txt"
    # https://github.com/codalab/codalab-competitions/wiki/User_Building-a-Scoring-Program-for-a-Competition#directory-structure-for-submissions
    
    output_file=open(os.path.join(output_dir, 'scores.txt'),"w")

 
    output_file.write("avg_precision:{0}\n".format(eval_scores[0])) 
    output_file.write("avg_recall:{0}\n".format(eval_scores[1]))
    output_file.write("avg_f1_score:{0}\n".format(eval_scores[2]))

    output_file.close()
        
if __name__ == "__main__":
    main(sys.argv[1:])