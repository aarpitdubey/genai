# Natural Language Processing (NLP)

Steps to Understand NLP:

![img](./img/nlp.png "Author: Arpit Dubey")

There are some fundamental concepts like:

1. **Corpus** : Paragraph

* A corpus is a large and structured set of texts that are used for linguistic analysis and processing. It serves as the foundational dataset upon which NLP tasks are performed. Corpora can be general-purpose or specialized for specific domains.
* **for example** : The Brown Corpus is a well-known example of a corpus in NLP. It contains a balanced selection of texts in American English from a wide range of genres and is used for various linguistic studies.

2. **Documents** : Sentences

* In the context of a corpus, documents are individual, self-contained units of text. A document could be a sentence, a paragraph, a webpage, an article, a book, or any distinct piece of text depending on the application's requirements.
* **for example** : In a corpus of news articles, each article would be considered a document.

3. **Vocabulary** : Unique Words

* Vocabulary refers to the set of unique words and expressions found within a corpus. It is the collection of all the distinct words that appear in the corpus and typically disregards frequency.
* **for example** : If a corpus contains the text "The cat sat on the mat," the vocabulary would be {the, cat, sat, on, mat}.

4. **Words** :

* Words are the smallest independent units of language that have meaning and can be used to form sentences. In text analysis, words are usually separated by spaces or punctuation.
* **for example** : In the sentence "Hello, world!", the words are "Hello" and "world".

## Tokenization

- Tokenization is a simple process where I can convert a corpus (Paragraph) into multiple documents (sentences) as well as multiple words as tokens.

1) **Sent_tokenizer()**

Corpus = "My name is ARPIT and I have interest in building projects related to Machine Learning, Data Science, Natural Language Processing, Deep Learning, Artificial Intellegence and Generative AI. I'm also a Senior Data Scientist."

![img](./img/sent_tokenization.png "Author: Arpit Dubey")

![img](./img/sent_token.png "Author: Arpit Dubey")

2) **word_tokenizer()**

![img](./img/word_token.png "Author: Arpit Dubey")

## Stemming

- Stemming is the process of reducing a word to it;s word stem that affixes to suffixes and prefixes or to the roots of words known as a lemma.
- Stemming is important in natural language understanding (NLU) and Natural Language processing (NLP).

words= ["eating", "eats", "eaten", "writing", "writes", "programming", "programs", "history", "finally", "finalized"]

## One Hot Encoding

One hot encoding is a technique used in machine learning to convert categorical data into numerical form.

This method involves creating new binary variables for each category of the original variable. Each category is represented by a binary vector of length equal to the number of categories, where a '1' marks the presence of a specific category and '0's indicate the absence of the other categories.

![img](./img/ohe.png "Author: Arpit Dubey")

**Advantages** **of one hot encoding :**

1. **Facilitation of Machine Learning Algorithms** : It allows categorical variables to be used in machine-learning algorithms that require numerical input.
2. **Avoids Ordinal Relationships** : By not assigning ordinal numbers, it helps in preventing any unintended ordinal relationship between categories. This is particularly useful when the categories don't have a natural order.
3. **Straightforward Implementation** : It is relatively straightforward to implement using libraries such as Scikit-learn or Pandas in Python.

**Disadvantages** **of one hot encoding:**

1. **Increased Dimensionality** : A significant drawback is the increase in dimensionality since it creates as many new variables as there are unique categories in the original data. This can lead to high memory usage and computational complexity, sometimes referred to as the **curse of dimensionality**.
2. **Sparse Matrices** : The resulting data usually becomes sparse, meaning most of the entries are zero, which leads to Overfitting.
3. **Not Ideal for Large Categories** : With a large number of unique categories, this approach might not be efficient.
4. No Semantic meaning is getting captured.
5. Out of vocabulary (ODV)

## Bag of Words (BoW) and Binary BoW

**The **Bag of Words (BoW)** model involves creating a vector representation where each vector dimension corresponds to a word in the vocabulary derived from the corpus. Each element of the vector is the frequency of the corresponding word in the document.**

for example:

**Sentence 1: "He is a good boy"**

**Sentence 2: "She is a good girl"**

**Sentence 3: "Boy and girl are good"**

**Vocabulary**

First, let's create a vocabulary from the sentences:

* Vocabulary: {He, is, a, good, boy, She, girl, and, are}
* Remove the stopwords: {He, is, a, She, and, are}
* Now, Vocabulary: {good, boy, girl}

| Sentences                           | good | boy | girl | output |
| ----------------------------------- | :--: | :-: | :--: | :----: |
| Sentence 1: "He is a good boy"      |  1  |  1  |  0  |   1   |
| Sentence 2: "She is a good girl"    |  1  |  0  |  1  |   1   |
| Sentence 3: "Boy and girl are good" |  1  |  1  |  1  |   1   |

If suppose we have these sentences:

**Sentence 1: "He is a good boy, a good"**

**Sentence 2: "She is a good girl"**

**Sentence 3: "Boy and girl are good"**

| Sentences                              | good | boy | girl | output |
| -------------------------------------- | ---- | --- | ---- | ------ |
| Sentence 1: "He is a good boy, a good" | 2    | 1   | 0    | 1      |
| Sentence 2: "She is a good girl"       | 1    | 0   | 1    | 1      |
| Sentence 3: "Boy and girl are good"    | 1    | 1   | 1    | 1      |

Here, frequency count of good in sentence 1 becomes 2

**Binary Bag of Words** is a variation where each vector element represents the presence (1) or absence (0) of the corresponding word, rather than its frequency.

where as, in Binary BOW the frequecy of words doesn't impact the vectors

| Sentences                              | good | boy | girl | output |
| -------------------------------------- | ---- | --- | ---- | ------ |
| Sentence 1: "He is a good boy, a good" | 1    | 1   | 0    | 1      |
| Sentence 2: "She is a good girl"       | 1    | 0   | 1    | 1      |
| Sentence 3: "Boy and girl are good"    | 1    | 1   | 1    | 1      |

![img](./img/bow.png "Author: Arpit Dubey")

| Advantages           | Disadvantages                           |
| -------------------- | --------------------------------------- |
| Simple and Intuitive | Sparse Matrix or array ---> overfitting |
| Fixed Sized          | Ordering of the words is changing       |
|                      | Out of Vocabulary (OOV)                 |
|                      | Semantic meaning is still not caputured |

## Term Frequency - Inverse Document Frequency (TF - IDF)

**Term Frequency (TF):** Term Frequency (TF) is a measure of how frequently a word appears in a document. It is calculated as the number of times a word appears in a document divided by the total number of words in that document.

The formula for Term Frequency is:

$$
TF(t, d) = \frac{\text{Number of times term } t \text{ appears in document } d}{\text{Total number of terms in document } d}
$$

**Example:**

In the sentence "He is a good boy", the term "good" appears 1 time, and the total number of terms in the document is 5. Therefore, the Term Frequency of "good" is:

$$
TF(\text{good}, \text{"He is a good boy"}) = \frac{1}{5} = 0.2
$$

**After Stopwords removal:**

    $TF(\text{good}, \text{"good boy"}) = \frac{1}{2} = 0.5$

**Inverse Document Frequency (IDF):** Inverse Document Frequency (IDF) is a measure of how important a word is in a collection of documents (corpus). It is calculated as the logarithm of the total number of documents in the corpus divided by the number of documents containing the term.

The formula for Inverse Document Frequency is:

$$
IDF(t, D) = log\left(\frac{\text{Total number of documents in the corpus}}{\text{Number of documents containing the term } t}\right)
$$

**Example:**

Let's assume the corpus consists of the following 3 sentences:

1. "He is a good boy"
2. "She is a good girl"
3. "Boy and girl are good"

The term "good" appears in 3 out of the 3 documents, so the IDF of "good" is:

$$
IDF(\text{good}, D) = log\left(\frac{3}{3}\right) = 0
$$

The term "boy" appears in 2 out of the 3 documents, so the IDF of "boy" is:

$$
IDF(\text{boy}, D) = log\left(\frac{3}{2}\right) = 0.1760
$$

**TF-IDF:**

TF-IDF (Term Frequency-Inverse Document Frequency) is a numerical statistic that is intended to reflect the importance of a word to a document in a collection or corpus. It is calculated by multiplying the Term Frequency (TF) by the Inverse Document Frequency (IDF).

The formula for TF-IDF is:

$$
TF-IDF(t, d, D) = TF(t, d) \times IDF(t, D)
$$

**Example:**

Let's calculate the TF-IDF for the term "good" in the sentence "He is a good boy":


$$
TF(\text{good}, \text{"He is a good boy"}) = \frac{1}{5} = 0.2
$$

After Stopwords removal:

    $	TF(\text{good}, \text{"good boy"}) = \frac{1}{2} = 0.5$

$$
IDF(\text{good}, D) = log\left(\frac{3}{3}\right) = 0
$$

$$
TF-IDF(\text{good}, \text{"He is a good boy"}, D) = 0.2 \times 0 = 0
$$

So, the TF-IDF of the term "good" in the sentence "He is a good boy" is 0.

![img](./img/tfidf.png "Author: Arpit Dubey")

| Advantages                          | Disadvantages         |
| ----------------------------------- | --------------------- |
| Intuitive                           | Sparcity still exists |
| Fixed Size --> Vocab Size           | OOV                   |
| Word Importance is getting captured |                       |
