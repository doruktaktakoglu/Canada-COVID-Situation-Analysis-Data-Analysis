# Compute tf-idf
Code for generating 10 words with highest tf-idf scores for each topics

## Requirement
1. Ensure you have `data/stopwords.txt`file. It is used to filter the commonly used words.


## `src/compute_tf_idf.py`
compile word count, compute tf-idf scores and generate 10 words for each topic by tf-idf scores in descending order.
`compute_tf_idf.py` accepts the following command-line arguments:

- -i: the file contains the tweets collected.
- -s: the file contains the commonly used words.
- -o: (Optional) the output file contains the compute result in json format. By default it prints the result to stdout.

Example:
`python3 ./src/compute_tf_idf.py -i tweets_collected.tsv -s ./data/stopwords.txt -o result.json`

## Assumption
1. the 9th column contains the topics (i.e. row[8]).
