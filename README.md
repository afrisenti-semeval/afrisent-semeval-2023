
<p align="center">
  <img align="center" src="images/afrisenti-twitter.png" />
  
> This repository contains data for the SemEval 2023 Shared Task 12: Sentiment Analysis in African Languages (AfriSenti-SemEval). More information can be found at the: [shared task](https://afrisenti-semeval.github.io) and [competition](https://codalab.lisn.upsaclay.fr/competitions/7320) websites.


  <h1 align="center"> </h1>
</p>


<div style="text-align:center;">


| No. | Language             | Country          |
|-----|----------------------|------------------|
| 1   | Algerian Arabic (arq)      | Algeria          |
| 2   | Amharic  (ama)                | Ethiopia         |
| 3   | Hausa   (hau)               | Nigeria          |
| 4   | Igbo  (ibo)                | Nigeria          |
| 5   | Kinyarwanda    (kin)        | Rwanda           |
| 6   | Moroccan Arabic/Darija (ary)| Morocco          |
| 7   | Mozambique Portuguese (pt-MZ)| Mozambique       |
| 8   | Nigerian Pidgin  (pcm)     | Nigeria          |
| 9   | Oromo   (orm)              | Ethiopia         |
| 10  | Swahili     (swa)         | Kenya/Tanzania   |
| 11  | Tigrinya    (tir)          | Ethiopia         |
| 12  | Twi        (twi)            | Ghana            |
| 13  | Xithonga        (tso)            | Mozambique          |
| 14  | Yoruba    (yor)            | Nigeria          |


</div>

# Dataset

AfriSenti dataset is available on [HugginFace](https://huggingface.co/datasets/shmuhammad/AfriSenti-twitter-sentiment) or [data folder](https://github.com/afrisenti-semeval/afrisent-semeval-2023/tree/main/data)


If you have used our dataset, please cite the following two papers: AfriSenti dataset paper and AfriSenti-SemEval task description paper. 

```
@inproceedings{Muhammad2023AfriSentiAT,
  title={AfriSenti: A Twitter Sentiment Analysis Benchmark for African Languages},
  author={Shamsuddeen Hassan Muhammad and Idris Abdulmumin and Abinew Ali Ayele and Nedjma Ousidhoum and David Ifeoluwa Adelani and Seid Muhie Yimam and Ibrahim Sa'id Ahmad and Meriem Beloucif and Saif Mohammad and Sebastian Ruder and Oumaima Hourrane and Pavel Brazdil and Felermino D'ario M'ario Ant'onio Ali and Davis Davis and Salomey Osei and Bello Shehu Bello and Falalu Ibrahim and Tajuddeen Gwadabe and Samuel Rutunda and Tadesse Belay and Wendimu Baye Messelle and Hailu Beshada Balcha and Sisay Adugna Chala and Hagos Tesfahun Gebremichael and Bernard Opoku and Steven Arthur},
  year={2023}
}
```

```
@inproceedings{muhammad-etal-2023-semeval,
  title="{S}em{E}val-2023 Task 12:  Sentiment Analysis for African Languages ({A}fri{S}enti-{S}em{E}val)",
  author="Muhammad, Shamsuddeen Hassan and
   Yimam, Seid and 
   Abdulmumin, Idris and 
   Ahmad, Ibrahim Sa'id  and 
   Ousidhoum, Nedjma, and
   Ayele, Abinew, and 
   Adelani, David and 
   Ruder, Sebastian and  
   Beloucif, Meriem and 
   Bello, Shehu Bello and 
   Mohammad, Saif M.",
  booktitle="Proceedings of the 17th International Workshop on Semantic Evaluation (SemEval-2023)",
  month=jul,
  year="2023",
}
```



# AfriSenti-SemEval 2023 Shared Task 

We provide the training, dev and test set for each task below. 


- For SubtaskA : Check [SubtaksA](https://github.com/afrisenti-semeval/afrisent-semeval-2023/tree/main/SubtaskA)
- For SubtaskB : Check [SubtaksB](https://github.com/afrisenti-semeval/afrisent-semeval-2023/tree/main/SubtaskB)
- For SubtaskC : Check [SubtaksC](https://github.com/afrisenti-semeval/afrisent-semeval-2023/tree/main/SubtaskC)

# Sample Tweets and Distribution

<p align="center">
<img align="center" src="https://raw.githubusercontent.com/afrisenti-semeval/afrisent-semeval-2023/main/afrisenti_languages.png"/>
</p>


# Sentiment Lexicon

We provide [sentiment lexicon](https://github.com/afrisenti-semeval/afrisent-semeval-2023/tree/main/sentiment_lexicon) in some languages that may be useful for the task. 

# Shared Task Starter kit

We provide a [starter kit](https://github.com/afrisenti-semeval/afrisent-semeval-2023/tree/main/starter_kit) for the competition to create a baseline result. You can open the starter kit in Colab Notebook and run the baseline system. The resultant experiment can be submitted to codalab to ensure all submission format is clear. You can then work on your own system towards the competition. 

To run the Colab Notebook, fork this repo first and click the badge "open on colab" on the forked version. 


- **Task A**: <a target="_blank" href="https://colab.research.google.com/github/afrisenti-semeval/afrisent-semeval-2023/blob/main/AfriSenti_SemEval_2023_Starter_Notebook_Task_A.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

- **Task B**: <a target="_blank" href="https://colab.research.google.com/github/afrisenti-semeval/afrisent-semeval-2023/blob/main/AfriSenti_SemEval_2023_Starter_Notebook_Task_B.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


## License

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

