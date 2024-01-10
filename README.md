
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
| 13  | Xithonga        (tso)            | Mozambique  |
| 14  | Yoruba    (yor)            | Nigeria          |

</div>

# Dataset

If you have used our dataset, please cite the following four papers: [AfriSenti dataset]([https://arxiv.org/abs/2302.08956](https://aclanthology.org/2023.emnlp-main.862.pdf)) , [AfriSenti-SemEval task description paper](https://aclanthology.org/2023.semeval-1.315.pdf), [NaijaSenti](https://aclanthology.org/2022.lrec-1.63) paper, and [ASAB](https://aclanthology.org/2020.coling-main.91.pdf) paper. 

AfriSenti dataset is available on [HugginFace](https://huggingface.co/datasets/shmuhammad/AfriSenti-twitter-sentiment) or [data folder](https://github.com/afrisenti-semeval/afrisent-semeval-2023/tree/main/data)


```
@inproceedings{muhammad-etal-2023-afrisenti,
    title = "{A}fri{S}enti: A {T}witter Sentiment Analysis Benchmark for {A}frican Languages",
    author = "Muhammad, Shamsuddeen  and
      Abdulmumin, Idris  and
      Ayele, Abinew  and
      Ousidhoum, Nedjma  and
      Adelani, David  and
      Yimam, Seid  and
      Ahmad, Ibrahim  and
      Beloucif, Meriem  and
      Mohammad, Saif  and
      Ruder, Sebastian  and
      Hourrane, Oumaima  and
      Jorge, Alipio  and
      Brazdil, Pavel  and
      Ali, Felermino  and
      David, Davis  and
      Osei, Salomey  and
      Shehu-Bello, Bello  and
      Lawan, Falalu  and
      Gwadabe, Tajuddeen  and
      Rutunda, Samuel  and
      Belay, Tadesse  and
      Messelle, Wendimu  and
      Balcha, Hailu  and
      Chala, Sisay  and
      Gebremichael, Hagos  and
      Opoku, Bernard  and
      Arthur, Stephen",
    editor = "Bouamor, Houda  and
      Pino, Juan  and
      Bali, Kalika",
    booktitle = "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing",
    month = dec,
    year = "2023",
    address = "Singapore",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.emnlp-main.862",
    doi = "10.18653/v1/2023.emnlp-main.862",
    pages = "13968--13981",
    abstract = "Africa is home to over 2,000 languages from over six language families and has the highest linguistic diversity among all continents. This includes 75 languages with at least one million speakers each. Yet, there is little NLP research conducted on African languages. Crucial in enabling such research is the availability of high-quality annotated datasets. In this paper, we introduce AfriSenti, a sentiment analysis benchmark that contains a total of {\textgreater}110,000 tweets in 14 African languages (Amharic, Algerian Arabic, Hausa, Igbo, Kinyarwanda, Moroccan Arabic, Mozambican Portuguese, Nigerian Pidgin, Oromo, Swahili, Tigrinya, Twi, Xitsonga, and Yoruba) from four language families. The tweets were annotated by native speakers and used in the AfriSenti-SemEval shared task (with over 200 participants, see website: https://afrisenti-semeval.github.io). We describe the data collection methodology, annotation process, and the challenges we dealt with when curating each dataset. We further report baseline experiments conducted on the AfriSenti datasets and discuss their usefulness.",
}

@inproceedings{muhammadSemEval2023,
    title = {{SemEval-2023 Task 12: Sentiment Analysis for African Languages (AfriSenti-SemEval)}},
    author = {Shamsuddeen Hassan Muhammad and Idris Abdulmumin and Seid Muhie Yimam and David Ifeoluwa Adelani and Ibrahim Sa'id Ahmad and Nedjma Ousidhoum and Abinew Ali Ayele and Saif M. Mohammad and Meriem Beloucif and Sebastian Ruder},
    booktitle = {Proceedings of the 17th {{International Workshop}} on {{Semantic Evaluation}} ({{SemEval-2023}})},
    publisher = {{Association for Computational Linguistics}},
    year = {2023}
}

@inproceedings{muhammad-etal-2022-naijasenti,
    title = "{N}aija{S}enti: A {N}igerian {T}witter Sentiment Corpus for Multilingual Sentiment Analysis",
    author = "Muhammad, Shamsuddeen Hassan  and Adelani, David Ifeoluwa  and Ruder, Sebastian  and Ahmad, Ibrahim Sa{'}id  and Abdulmumin, Idris  and Bello, Bello Shehu  and Choudhury, Monojit  and Emezue, Chris Chinenye  and Abdullahi, Saheed Salahudeen  and Aremu, Anuoluwapo  and orge, Al{\'\i}pio  and Brazdil, Pavel",
    booktitle = "Proceedings of the Thirteenth Language Resources and Evaluation Conference",
    month = jun,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
    url = "https://aclanthology.org/2022.lrec-1.63",
    pages = "590--602",
}

@InProceedings{yimametalcoling2020,
    title = "Exploring {A}mharic Sentiment Analysis from Social Media Texts: Building Annotation Tools and Classification Models",
    author = "Yimam, Seid Muhie  and
      Alemayehu, Hizkiel Mitiku  and
      Ayele, Abinew  and
      Biemann, Chris",
    booktitle = "Proceedings of the 28th International Conference on Computational Linguistics",
    month = dec,
    year = "2020",
    address = "Barcelona, Spain (Online)",
    pages = "1048--1060"
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

# Baselines

See example [here](https://huggingface.co/Davlan/afrisenti-twitter-sentiment-afroxlmr-large)


# Shared Task Starter kit

We provide a [starter kit](https://github.com/afrisenti-semeval/afrisent-semeval-2023/tree/main/starter_kit) for the competition to create a baseline result. You can open the starter kit in Colab Notebook and run the baseline system. The resultant experiment can be submitted to codalab to ensure all submission format is clear. You can then work on your own system towards the competition. 

To run the Colab Notebook, fork this repo first and click the badge "open on colab" on the forked version. 


- **Task A**: <a target="_blank" href="https://colab.research.google.com/github/afrisenti-semeval/afrisent-semeval-2023/blob/main/AfriSenti_SemEval_2023_Starter_Notebook_Task_A.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

- **Task B**: <a target="_blank" href="https://colab.research.google.com/github/afrisenti-semeval/afrisent-semeval-2023/blob/main/AfriSenti_SemEval_2023_Starter_Notebook_Task_B.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## Funding Acknowledgements

This competition recieves generous support of the Lacuna Fund. 

## License

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

