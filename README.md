# ACM Research Coding Challenge (Fall 2021)

## [](https://github.com/ACM-Research/Coding-Challenge-F21#no-collaboration-policy)No Collaboration Policy

**You may not collaborate with anyone on this challenge.** You _are_ allowed to use Internet documentation. If you _do_ use existing code (either from Github, Stack Overflow, or other sources), **please cite your sources in the README**.

## [](https://github.com/ACM-Research/Coding-Challenge-F21#submission-procedure)Submission Procedure

Please follow the below instructions on how to submit your answers.

1.  Create a **public** fork of this repo and name it `ACM-Research-Coding-Challenge-F21`. To fork this repo, click the button on the top right and click the "Fork" button.

2.  Clone the fork of the repo to your computer using `git clone [the URL of your clone]`. You may need to install Git for this (Google it).

3.  Complete the Challenge based on the instructions below.

4.  Submit your solution by filling out this [form](https://acmutd.typeform.com/to/zF1IcBGR).

## Assessment Criteria

Submissions will be evaluated holistically and based on a combination of effort, validity of approach, analysis, adherence to the prompt, use of outside resources (encouraged), promptness of your submission, and other factors. Your approach and explanation (detailed below) is the most weighted criteria, and partial solutions are accepted.

## [](https://github.com/ACM-Research/Coding-Challenge-S21#question-one)Question One

[Sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis) is a natural language processing technique that computes a sentiment score for a body of text. This sentiment score can quantify how positive, negative, or neutral the text is. The following dataset in `input.txt` contains a relatively large body of text.

**Determine an overall sentiment score of the text in this file, explain what this score means, and contrast this score with what you expected.** If your solution also provides different metrics about the text (magnitude, individual sentence score, etc.), feel free to add it to your explanation.

**You may use any programming language you feel most comfortable. We recommend Python because it is the easiest to implement. You're allowed to use any library/API you want to implement this**, just document which ones you used in this README file. Try to complete this as soon as possible as submissions are evaluated on a rolling basis.

Regardless if you can or cannot answer the question, provide a short explanation of how you got your solution or how you think it can be solved in your README.md file. However, we highly recommend giving the challenge a try, you just might learn something new!

## Solution

The creation of the overall sentiment score of the input text was created using python. In specific, `python 3.9.1`.

The following python library and its use are as follows:

1. `NLTK`: This is a widely popular tool used to work with human language data. This was the core library with which I created the program. In particular, I used the `SentimentIntensityAnalyzer` and `sent_tokenize` tools provided in the library.

The solution for evaluating an overall sentiment score created using just this library. First, I did research to find libraries which proved to be the easiest to implement. After setting it up, I first understood the data output of the `SentimentIntensityAnalyzer` as it was my first time working with NLP. After understanding the data and output, I simply opened the input file and passed it along to the sentiment analyzer method. As indicated in the final output, I got a compound score which .9982 which indicates an overall positive sentiment. Looking at the categorical ratios of neg, neu, and pos, the compound score does seem to make sense as there are positive sentiment embedded within neutral text. Since the text was more explaining a story, I was not surprised by this number.

I did, however, want to dive deeper. I wanted to look at each sentence individually to see if the overall trend does indeed match. A big reason for wanting to look further was that my research on the library had indicated that the sentiment analyzer worked better with shorter text. So, I first split the input file into sentences using `sent_tokenize` available in the same library. From here I printed each sentiment score for individual sentences. The overall trend of slightly positive scores was seen here as well, however, I got a much better picture of the few sentences that were labeled as slightly negative. I was also surprised at some sentences being labeled as fully neutral. For example, **"Watch out!"** had a compound score of 0.0. I believe this is do to the lack of context with such a short sentence, however, further tweaking of the method could better label these issues.
