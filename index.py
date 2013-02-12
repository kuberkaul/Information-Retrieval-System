#parsing of crainfield set
#indexing of the Data
from nltk.tokenize import regexp_tokenize
import os
import cPickle as pickle
import nltk
import glob
from xml.dom.minidom import parse
from xml import dom


path = 'C:\Users\Romi\Desktop\CranField'
path1 = 'C:\Users\Romi\Desktop\CranField 1'

for infile in glob.glob( os.path.join(path, ".txt") ):
    print("current file is: " + infile)
    
dirList=os.listdir(path)  
c = {}  #creating empty dictionaries
l = {}
words = []
for fname in dirList:
    
    myInput = open(path + '\\'+fname ,'r').read()
    dom1 = parse(path +'\\' + fname) 
    # parse a file by name
    datasource = open(path + '\\'+fname)
    dom = parse(datasource)   
    myInput.strip()#stripping of white spaces
    xmlTag=dom.getElementsByTagName('DOCNO')[0].firstChild.nodeValue.strip()
    xmlTag1=dom.getElementsByTagName('TEXT')[0].firstChild.nodeValue.strip()
    xmlTag2=dom.getElementsByTagName('TITLE')[0].firstChild.nodeValue.strip()
    c [xmlTag] = xmlTag2
    l [xmlTag] = xmlTag1
    words = words + xmlTag1.split(' ')
    f = open(path1+'\\'+xmlTag, 'w')
    content = str(xmlTag1)
    f.write(content)    
    f.close()
outpath = open('C:\Users\Romi\Desktop\picklef.txt', 'wb')           
pickle.dump( c, outpath ) #pickling of data or serializing it to a file and unpickling it to the other file -query.py
outpath.close()

outpath = open('C:\Users\Romi\Desktop\words.txt', 'wb')           
pickle.dump( words, outpath ) #pickling of data or serializing it to a file and unpickling it to the other file -query.py
outpath.close()


text = content

def word_split(text):
    """
    Split a text in words. Returns a list of tuple that contains
    word.
    """
    a = regexp_tokenize(text.lower().strip(), pattern=r'\w+') 
    return a

def word_index(text):
    """
    Just a helper method to process a text.
    It calls word split.
    """
    words = word_split(text)
    return words
    
inverted = {}        
def inverted_index(text,d):
    """Create an Inverted-Index of the specified text document.
     {word:[locations]} 
    """
    locations = 0 
    for words in word_index(text): 
        #locations = 0
        locations = locations +1
        if not inverted.__contains__(words):
            poslist=[locations]
            doclist = {}
            doclist[d] =poslist
            inverted[words] = doclist
        else:
            if not d in inverted[words]:
                poslist=[locations]
                doclist= inverted[words]
                doclist [d] = poslist
                inverted[words] = doclist 
            else:
                poslist = inverted[words][d]
                poslist.append(locations)
    #print inverted           
    return inverted       

    
if __name__ == '__main__':
    '''
    the main for index.py
    '''
    
    dirList=os.listdir(path1)  
    for d in dirList:
            myInput = open(path1 + '\\'+d ,'r').read()
            doc_index = inverted_index(myInput,d)
    output = open('C:\Users\Romi\Desktop\myfile', 'wb')           
    pickle.dump( doc_index, output )    
    output.close()
    
    
    
                
        



