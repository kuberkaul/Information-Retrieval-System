--------------------------------README----------------------------------

Course :  CS 6998, Search Engine Technology
Project : HW 1 Building a basic information retrieval system

Name:
1. Kuber Kaul(UNI- kk2872 )
			
List Of Files Submitted:

SearchEngine.py  -------------------- The python program
External Libraries  --------------------------- NLTK for Python
The install, index and query programs.
Results.py ---------------------------- Code for Similar Words.
			
How To Run The Program :	I have created an install file in the directory.
# To run type "make" and it should run the entire project. 

Internal Design of the Project	:

1)I have divided the code into index.py and query.py as the two files    essential for doing the work.

2)NLTK (Natural Language Toolkit) for python has been used by me to handle:
a. find similar words.
b. reduce stock words.
c. stemming of data to its root word.
 
3)Pickle in Python was used to serialize the data from one file to another and vice versa.

Query-Modification Method :	

a) Description of Parsing Algorithm
1) Approach : I have used my own algorithm for fast parsing of crainfield set of data and have stored DOC NO, TITLE and CONTENT using it.

Additional Information	:	


1) I used regex_tokenization to split the queries and the documents into a list of words as tokens for easy parsing.
2) I decided not to stem the words as the collection of documents is fairly normal in size and not very huge also it would have a counter-effect later on searching for the specific term as it would be rooted down. This would not be beneficial.
3) Though, I did remove stock words reducing the index which brought the index to relatively manageable size of the document set that we have. .This resulted in fast parsing of data as it was stripped down.
4)I have included the similarity feature in my code and hence am able to search for various related words.
  



	
						

