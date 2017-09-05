# LanguageProcessing

Repository for project that involves extracting, parsing, and analysing data from natural language sources.

### Getting Started

#### HashtagCreator

Use creator.py to generate word frequencies and location of occurences in files.
Pass command line arguments to generate different outputs, in different styles, from different file locations.

##### Flags

```
'--directory' --> directory path to retrieve source data from
              --> example '--directory /home/your_name/your_data'
'--number'    --> to retrieve the top 'n' most common occurring words
              --> example '--number 5'
              --> gives you the 5 most common words from your data source(s)
'--format'    --> the format you want your output to come in
              --> default prints to console
              --> example '--format csv'
              --> gives your output in CSV
'--output'    --> directory path to send output to
              --> example '--output /home/your/output/goes/here'
'--result'    --> file name to put output in
              --> example '--result your_file_name'
              --> puts the results in 'your_file_name'
```
              
###### Example
```
python creator.py --directory /get/data/from/here
                  --number 5
                  --format csv
                  --output /send/output/to/here
                  --result file_name
                  
```
Gives you the 5 most commonly occuring words from the data at --directory, in CSV format.
Then puts your output in /send/output/to/here/file_name.csv

### Prerequisites

* [nltk](http://www.nltk.org/) - Natural Language Tool Kit
```
pip install nltk
```
