# ML992 : Machine Learning Course Project Description and Leaderboards


## Task Definition and Dataset Description: Sentiment Analysis

**Task**:

Given a text feed, determine whether its postive or negative sentiment.

**Dataset**:

Context:

* A movie review dataset. NLP tasks Sentiment Analysis.
* Note: all the movie review are long sentence(most of them are longer than 200 words.)

Content:
* a file with `*-Data.csv` postfix: two columns used (`text` : the review of the movie, `ID`: id of the review)
* a file with `*-GT.csv` postfix: two columns used (`ID`: id of the review, `label` : the sentiment label of the movie review)


## `Board`


| Model(Team Name) | Accuracy(Test1) | Accuracy(Test2)| AVG | note |
|---|---|---|---|---|
| HAL | 0.8908 | - | - |
| Sentiment_Analysis |0.8902| - | -|
| NGRAMLR(organizer) | 0.8888 | - |  - |
| wildonion | 0.8628 | - | - |
| 54rnd | 0.8558| - | - |
| RandomBaseline(organizer) | 0.5036 | - | - |
|yaaghobi|0.4912 | - | - |  |
| sasvm | ERROR | - | - | code submitted! |
|textclassification|ERROR | - | - | code submitted!|

## Timelines
* ~~`13 March 2021`: Task launch.~~
* ~~`5 May 2021`: (EXTENDED) Submission-1 phase(early bird), for Test-1.~~
* ~~`5 May 2021`: Leaderboard update.~~
* ~~`10 May 2021`: Test-1(validation set) GT release. Test-2(test set) data release for final submission-shared only with submitted approaches~~.
* **`5 June 2021`: Submission-1 phase , for Test-1. STILL OPEN**
* **`5 June 2021`: Submission-2 phase(final), for Test-2.**
* `5 June 2021`: Code submission.
* `10 June 2021`: Test-2 GT release.
* `15 June 2021`: Final leaderboard update.
* `20 June 2021`: Participant paper submission.
* `30 June 2021`: Task overview, and task reports.

## Submission Forms

* [Earlybird Submission](https://forms.gle/X8fFVgzBR5pPrtaQ8)
    - Fill the form and submit your model prediction over test-1 until `5 May 2021`
* [Final Submission](https://docs.google.com/forms/d/1mH_sCqXJUqCEjtdpHvi0HcOE3ZQlzy6PNDeCveqGhsc/prefill)
    - Fill the form and submit your model prediction over test-2 until `5 June 2021`
## Terms and Conditions

1. This is a binary-classification problem.
2. Report results based on F1-Score, Accuracy, and Confusion Matrix, and AUC score.
3. You should do the Exploratory Data Analysis for this task.
4. You should report an analogy of why you used a particular model. to do this; you should report your baseline models(as presented in the task) and some of the works presented in the research field about it and here.
5. Imagine your model will be embedded in our software, so paying attention to your implementations is crucial.
6. Write your report in english.

## News

* 6 May 2021:
    - leaderboard updated
    - test-2 shared
    - deadlines changes for phase-1
    - test-1 GT shared with earlybird submitted teams

* 30 April 2021:
    - Deadline for first submission extended!

* 29 April 2021:
    - adding FAQ section

* 5 April 2021
    - Submission form created for participants

* 13 March 2021
    - Tran/Test1 datasets released
    - Starter Notebooks and LeaderBoard Creation


## References:
* [1] ML982: https://github.com/hamedbabaei/ML982
* [2] Twitter sentiment analysis using the sentiment140 dataset. https://github.com/HamedBabaei/sentiment-analysis
* [3] LSACONet: LSACoNet: A Combination of Lexical and Conceptual Features for Analysis of Fake News Spreaders on Twitter. http://ceur-ws.org/Vol-2696/paper_124.pdf
* [4] Cross-domain Authorship Attribution: Author Identification using a Multi-Aspect Ensemble Approach. http://www.dei.unipd.it/~ferro/CLEF-WN-Drafts/CLEF2019/paper_195.pdf
* [5] Development of an Ensemble Multi-stage Machine for Prediction of Breast Cancer Survivability. http://jad.shahroodut.ac.ir/article_1780_e3aa6f7b2b8463e031c1b4fc2785a103.pdf
* [6] A Low Dimensionality Representation for Language Variety Identification. https://arxiv.org/pdf/1705.10754.pdf

## Contact

Email: hamedbabaeigiglou@gmail.com

## FAQ's:

**Q1 - What we should do exactly for submission 1 and 2?**

A1:

*For the first part of the submissions, we only need a CSV file of your model prediction over the validation set (I mean test-1). This will give you and us an idea of how much your model is performed.*

*After that you will have full month (till 5 June - deadline of submission 2) to work on your model to improve it. Then we will ask you to make your final model prediction over test-2 and submit your final prediction with codes for final evaluation.*

*We want to see how you are able to boost your performance and how you deal with the problem in these two phases. Not a big deal at all. You can submit the same model prediction for prediction on both test-1 and test-2. BUT I highly recommend not do this. Just try to improve your model performance after the first submission.*

**Q2 - What exactly we can implement from `A Low Dimensionality Representation for Language Variety Identification` work for the project? All of the models required to be implemented or not?**

A2:
*This paper introduced a lower dimensionality statistical embedding based on the TFIDF matrix and weighted features based on classes. For this project, if you could implement this statistical embedding on project datasets would be enough for the feature extraction part. For the classification part, you are free to do anything. As I said, it is not a big deal to go for it. But If you could do that it is valuable work for us.*

