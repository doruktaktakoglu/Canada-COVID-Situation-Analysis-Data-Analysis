from optparse import OptionParser
import csv
import math
import json

# -i input file path
# -s stopwords file path
# -o output file path
def option():
    parser = OptionParser()
    parser.add_option("-i", "--input", dest="input_file")
    parser.add_option("-s", "--stopwords", dest="stop_words")
    parser.add_option("-o", "--output", dest="output_file")
    (options, args) = parser.parse_args()
    input_path = options.input_file
    stopwords_path = options.stop_words
    output_path = options.output_file
    return input_path, stopwords_path, output_path

# loading the stopwords list from stopwords.txt
def load_stopwords(path):
    stopwords = []
    with open(path) as f:
        for line in f:
            if (not "#" in line):
                stopwords.append(line.replace("\n", ""))
    return stopwords

# remove punctuation and non-alpha from the text
def remove_punc(line, punc):
    new_line = ""
    for c in line:
        if c not in punc:
            new_line += c
        else:
            new_line += " "
    
    result = []
    for word in new_line.split():
        if (word.isalpha()):
            result.append(word)
    return result

# remove stopwords from the text
def remove_stopwords(line, stopwords):
    result = []
    for word in line:
        if not word in stopwords:
            result.append(word)
    return result

# add word count to a dictionary
def add_word_count(count, topic, line):
    for word in line:
        try:
            count[topic][word] += 1
        except:
            count[topic][word] = 1

# return a dictionary of each topic's word count
def get_word_count(input_file, stopwords_file):
    punc = '()[],-.?!:;#&'
    #topics = ['m', 'v', 'c', 't', 'p', 's', 'a', 'u']
    #word_count = dict.fromkeys(topics, {})
    word_count = {'m':{}, 'v':{}, 'c':{}, 't':{}, 'p':{}, 's':{}, 'a':{}, 'u':{}}
    stopwords = load_stopwords(stopwords_file)
    with open(input_file, 'r', encoding='utf-8') as fd:
        reader = csv.reader(fd, delimiter='\t')
        next(reader)
        for row in reader:
            topic = row[8].lower()
            line = remove_punc(row[7].lower(), punc)
            line = remove_stopwords(line, stopwords)
            add_word_count(word_count, topic, line)
    return word_count

def tf(count, topic, word):
    return count[topic][word]

def idf(count, topics, word):
    num_topic = 0
    total_num = len(topics)
    for topic in count:
        for w in count[topic]:
            if (word==w):
                num_topic += 1
    return math.log(total_num / num_topic, 10)

def tf_idf(count, topic, topics, word):
    return tf(count, topic, word) * idf(count, topics, word)

# return a dict contains 10 words for each topic with highest tf-idf score
def get_result(count):
    topics = ['m', 'v', 'c', 't', 'p', 's', 'a', 'u']
    #word_score = dict.fromkeys(topics, {})
    word_score = {'m':{}, 'v':{}, 'c':{}, 't':{}, 'p':{}, 's':{}, 'a':{}, 'u':{}}
    result = {}
    for topic in count:
        for word in count[topic]:
            word_score[topic][word] = tf_idf(count, topic, topics, word)
        sorted_d = sorted(word_score[topic].items(), key=lambda x: x[1], reverse=True)
        l = []
        for ele in sorted_d[0:10]:
            l.append(ele[0])
        result[topic] = l
    return result

# write the dictionary to a file if -o provided otherwise print to stdout
def generate_json(result, output_file):
    if (output_file == None):
        print(json.dumps(result, indent=4))
    else:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=4)

def main():
    input_path, stopwords_path, output_path = option();
    word_count = (get_word_count(input_path, stopwords_path))
    result = get_result(word_count)
    generate_json(result, output_path)

if __name__ == '__main__':
    main()
