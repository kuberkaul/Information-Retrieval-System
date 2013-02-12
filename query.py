from index import regexp_tokenize
import pickle
from test.test_iterlen import len
import re
import sys
import nltk
import operator

def getTitle(xmlTag):
    '''
    function to get the title
    '''
    outpath = 'C:\Users\Romi\Desktop\picklef.txt'
    pkl_file = open(outpath, 'rb')
    getTitle = pickle.load(pkl_file)
    print getTitle[xmlTag]
    pkl_file.close()
    
def getDoc(docno):
    '''
    function to get the doc number
    '''
    file1 = open('C:\Users\Romi\Desktop\CranField 1'+'\\'+docno, 'r')
    print file1.read()
    file1.close()
    
def similar(word):
    outpath = 'C:\Users\Romi\Desktop\words.txt'
    pkl_file = open(outpath, 'rb')
    words = pickle.load(pkl_file)
    text = nltk.Text(words)
    text.similar(word)
#def calulateTF(docno,tf):
 #   try:
  #      print "term-frequency for ", tf , " in ", docno , " : " ,len(index[tf][docno])
   # except:
    #    print "term-frequency for ", tf , " in ", docno , " : 0"
        
        

if __name__ == '__main__':
    '''
    the main for query.py
    '''
    
        
    path3 = 'C:\Users\Romi\Desktop\myfile'
    pkl_file = open(path3, 'rb')
    index = pickle.load(pkl_file)
    pkl_file.close()
    print 'Loading index... please wait...'
    print 'Index loaded. You may now proceed to search'
    while True:
        
        queriess = raw_input("whats the query??")
        requests = queriess.split(" ")
        newqueries = regexp_tokenize(queriess, pattern = r'\"(.*?)\"')
        queries=regexp_tokenize(re.sub(r'\".*?\"', "", queriess), pattern=r'\w+')
        '''splitting of query into tokens using regex_tokenization'''
        
        if requests[0] == 'similar':
            similar(requests[1])
            continue
        if requests[0] == 'df':
                req = ' '.join(requests[1:])
                reqs = regexp_tokenize(re.sub(r'\".*?\"', "", req), pattern=r'\w+')
                print reqs
                if len(reqs) == 1:
                    ''' handling single word queries'''
                    if reqs[0] not in index:
                        print 'Sorry, not found in any document!'
                    else:
                        print 'number of documents it appears in is' , len(index[reqs[0]])
                requestset = set()
                if len(reqs) > 1:
                    '''
                    handling only < single word requests
                    '''
                    print reqs
                    for r0 in reqs:
                        if r0 not in index:
                            continue
                        else:
                            requestset = requestset.union(set(index[r0].keys()))
                    print 'Found the request in' ,len(requestset), 'documents!'
                req = ' '.join(requests[1:])
                reqs = regexp_tokenize(req, pattern = r'\"(.*?)\"')
                
                t = set()
                for r in reqs:
                    newquer=regexp_tokenize(r, pattern=r'\w+')
                #print newquer
                #print newqueries
                
            
                    if newquer[0] not in index.keys():
                        print " no documents for given phrase"
                    else:
                        finaldoclist = index[newquer[0]]
                        tempdoclist={}
                        i =1
                        for  new in newquer[1:]:
                            #print index
                            for d in finaldoclist:
                                if  d not in index[new].keys():
                                    pass
                                    #del finaldoclist[d]
                                else:
                                    s = set(finaldoclist[d])& set([p-i for p in index[new][d]])
                                    if len(s) is not 0 :    
                                        tempdoclist[d] = s
                            finaldoclist = tempdoclist
                            i = i +1
                            
                    print len(finaldoclist), finaldoclist
                    print 'The phrase',r,' appears in', len(finaldoclist), 'documents'
                '''handling the phrase terms'''
                continue       
                
        if requests[0] == 'title':
            '''calling the function to get the title'''
            req = ' '.join(requests[1:])
            getTitle(req)
            continue 
            
        if requests[0] == 'doc':
            '''calling the function to get document number'''
            req = ' '.join(requests[1:])
            getDoc(req)
            continue
            
        if requests[0] == 'tf':
            '''handling the term frequency'''
            if requests[2] not in index.keys():
                print 0
            else:    
                this = index[requests[2]]
                if requests[1] in this.keys():
                    print 'the term frequency is' , len(this[requests[1]])
                else:
                    print 'term frequency is 0'
            continue
            
    
        if requests[0] == 'freq':
            reqs = ' '.join(requests[1:])
            reqs = regexp_tokenize(reqs, pattern = r'\"(.*?)\"')
            
            for r in reqs:
                newquer=regexp_tokenize(r, pattern=r'\w+')    
                if newquer[0] not in index.keys():
                    print " no documents for given phrase"
                else:
                        finaldoclist = index[newquer[0]]
                        tempdoclist={}
                        i =1
                        for  new in newquer[1:]:
                            #print index
                            for d in finaldoclist:
                                if  d not in index[new].keys():
                                    pass
                                else:
                                    s = set(finaldoclist[d])& set([p-i for p in index[new][d]])
                                    if len(s) is not 0 :    
                                        tempdoclist[d] = s
                            finaldoclist = tempdoclist
                            i = i +1
                     
                #print len(finaldoclist), finaldoclist
                
                freq =0
                for d in finaldoclist.keys():
                    freq = freq + len(finaldoclist[d])
                print 'The phrase',r,' appears ', freq, 'times'
                '''handling the phrase terms'''
                continue  
        '''The above will give the phrase terms or frequency'''
                
        
        #query processing
        # newqueries = regexp_tokenize(queriess, pattern = r'\"(.*?)\"')
        # queries=regexp_tokenize(re.sub(r'\".*?\"', "", queriess), pattern=r'\w+')
    
        #doclist: {doc :[list of postion]}      
        doc_list = {}
        if len(queries)==1:
            if queries[0] in index:
                doc_list  = index[queries[0]]
                '''print doc_list''' 
        elif len(queries) >1:
            
            x = {}
            for query in queries:
                if query in index.keys():
                    x = index[query]
                    for x1 in x.keys():
                        if not x1 in doc_list:
                            doc_list[x1] = x[x1]
                        else:
                            doc_list[x1] = doc_list[x1].append(x[x1])
        newdoc_list = {}
        '''print doc_list'''
           
    #            sorted_newdoc_list = sorted(newdoc_list.iteritems(), key=operator.itemgetter(1))
    #            print sorted_newdoc_list.reverse()
            
     
                      
            
            
            
        
         
        
        
        for newqueries in newqueries:
            newquer=regexp_tokenize(newqueries, pattern=r'\w+')
            #print newquer
            #print newqueries
            
        
            if newquer[0] not in index.keys():
                print " no documents for given phrase"
            else:
                finaldoclist = index[newquer[0]]
                tempdoclist={}
                i =1
                for  new in newquer[1:]:
                    #print index
                    if new not in index.keys():
                        finaldoclist = {}
                        break
                    for d in finaldoclist:
                        if  d not in index[new].keys():
                            continue
                            #del finaldoclist[d]
                        else:
                            s = set(finaldoclist[d])& set([p-i for p in index[new][d]])
                            if len(s) is not 0 :    
                                tempdoclist[d] = s
                    finaldoclist = tempdoclist
                    i = i +1
                for x1 in finaldoclist.keys():
                    if not x1 in doc_list:
                        doc_list[x1] = list(finaldoclist[x1])
                    else:
                        doc_list[x1] = doc_list[x1].append(list(finaldoclist[x1]))
                    
                '''print len(finaldoclist), finaldoclist'''
                    
        newdoc_list = {}
        for doc in doc_list.keys():
            newdoc_list[doc] = len(doc_list[doc])
        print sorted(newdoc_list, key=newdoc_list.get, reverse=True)

                
    
            
           
        
        
            
            
                
            
            
    
        
        
        