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


| Model(Team Name) | ACC(Test1) | ACC(Test2)| AVG | SScore| CScore | RScore | FinalScore |
|---|---|---|---|---|---|---|---|
| danandeh |0.8902 *| 0.9148 | 0.9025| 100 |  ||
| sasvm | 0.897 | 0.8996 | 0.8983 | 100 | |  ||
| HAL | 0.8908 | 0.9026 | 0.8967 | 100 |  ||
| NGRAMLR(organizer) | 0.8888 | 0.8864 |  0.8876 | - |  ||
| wildonion | 0.8628 | 0.9058 | 0.8843 | 100 |  ||
| 54rnd | 0.8558| 0.9018 | 0.8788 | 100 |  ||
| yaaghobi|0.8684 *| 0.888 | 0.8782 | 100 | |  ||
| Sentiment_Analysis #|0.8902| 0.49 | 0.6901 | 90 | | ||
| BK | 0.8524 *| 0.4938 | 0.6731 | 90 | |  ||
| RandomBaseline(organizer) | 0.5036 | 0.5046 | 0.5041 | - |  ||
| garshasbi #| 0.4952 * | 0.5344 | 0.5148 | 80 | |  ||
| textclassification #| 0.4952 * | 0.5344 *| 0.5148 | 80 | |  ||

* `*` Late Submissions
* `#` Validation-GT sharing outside of the predefined-scope!
* `SScore`: Submission Score (from 100) based on averaged results
* `CScore`: Code quality score (from 100) + unti 100 extra point from me for the quality
* `RScore`: Report quality score (from 100)
* `FinalScore`: (SScore + CScore + RScore)/300  - the result will in range of (0, 100), higher than this is extra mark!

## Timelines
* ~~`13 March 2021`: Task launch.~~
* ~~`5 May 2021`: (EXTENDED) Submission-1 phase(early bird), for Test-1.~~
* ~~`5 May 2021`: Leaderboard update.~~
* ~~`10 May 2021`: Test-1(validation set) GT release. Test-2(test set) data release for final submission-shared only with submitted approaches~~.
* ~~`10 June 2021`: (EXTENDED) Submission-1 phase , for Test-1.~~
* ~~`10 June 2021`: (EXTENDED) Submission-2 phase(final), for Test-2.~~
* ~~`10 June 2021`: (EXTENDED) Code submission.~~
* ~~`10 June 2021`: Test-2 GT release.~~
* ~~`15 June 2021`: Final leaderboard update.~~
* **`20 June 2021`: Participant paper submission.**
* `30 June 2021`: Task overview, and task reports.

## Paper Submission (report file)

The following sections required in the report:

* abstract        
* introduction      : just tell what is the task, and if you want to add some general state and opinions, you are welcome to add it
* proposed method   : describe your proposed model and explain it in a general and detailed manner
* evaluation        : report your model result on your evaluation and submissions (phase 1 and phase 2)
* conclusion        : just tell your conclusion from this project

**Notes**:
* English or Persian is not a case here
* No need to explain your code, but if you are using a specific library like scikit-learn or keras or tensorflow and ... please just mention it
* you can add more sections if you like, but it is totally up to you
* Length of the paper is not mather, as long as you describe each section, even in 2 sentences it is ok!
* Don't forget to put your affliction on the paper!
* If you are uncomfortable with the report, just briefly describe your models that I could understand why you use them, and that is enough too! But I am highly recommend to practice that structure

## Submission Forms

* [Earlybird Submission](https://forms.gle/X8fFVgzBR5pPrtaQ8)
    - Fill the form and submit your model prediction over test-1 until `5 May 2021`
* [Final Submission](https://docs.google.com/forms/d/e/1FAIpQLSdQHaxGnGjjGol4AK-OlP5YX9ACgYSbGUHGT7rzvrK-SqrkIQ/viewform)
    - Fill the form and submit your model prediction over test-2 until `5 June 2021`
* [Report Submission](https://forms.gle/sD1tmdo7hfPJ7aoeA)
    - Fill the form and submit your report until  `20 June 2021`
## Terms and Conditions

1. This is a binary-classification problem.
2. Report results based on F1-Score, Accuracy, and Confusion Matrix, and AUC score.
3. You should do the Exploratory Data Analysis for this task.
4. You should report an analogy of why you used a particular model. to do this; you should report your baseline models(as presented in the task) and some of the works presented in the research field about it and here.
5. Imagine your model will be embedded in our software, so paying attention to your implementations is crucial.
6. Write your report in english.

## News

* 6 jun 2021:
    - paper submission for added
    - phase 1 and phase 2 submission extended for a last time!
    
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

