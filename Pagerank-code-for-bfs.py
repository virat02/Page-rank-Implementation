import math
import pickle
from collections import OrderedDict
M = {}                                                            #dictionary of pages as key and their in-links as value
L = {}                                                            #dictionary of pages as key and their out-links as value
S = []                                                            #list of sink pages(pages with no out-links)
with open("urlsCrawledBFSInlinkGraph-encoded.txt", 'rb') as f:
    M = pickle.loads(f.read())

N = len(M.keys())                                                 #Total number of pages in the corpus
set_of_pages =  M.keys()

with open("urlsCrawledBFSOutlinkGraph-encoded.txt", 'rb') as f:
    L = pickle.loads(f.read())

for x,y in L.items():
    if y == []:
        S.append(x)

d = 0.85                                                          #PageRank damping/teleportation factor
page_rank = {}                                                    #dictinary of pages as key and their PageRank scores as value
newPR = 0                                                         #stores the new Pagerank value
s = 0
convergence_list = []                                             #list of 0's and 1's, denotes convrgence if atleast four 1's appear together in the list

def perplexity(p):                                                #calculates the perplexity
    entropy = 0
    for page in set_of_pages:
        entropy += p[page] * math.log2(p[page])
    entropy = entropy * -1
    current_perplexity = math.pow(2,entropy)
    return current_perplexity

def PageRank (M,L,d):                                             #calculates the Pagerank
    global newPR
    init_page_rank = {page: (1/N) for page in set_of_pages}       #initial-value
    prev_perplexity = perplexity(init_page_rank)
    f = open('Perplexity-values-BFS.txt', 'w')
    while sum(convergence_list[-4:]) < 4:
        sinkPR = 0
        for page in S:                                            #calculate total sink PR
            sinkPR += init_page_rank[page]
        for page in set_of_pages:
            newPR = (1-d)/N + d * (sinkPR/N)                      #teleportation and spread remaining sink PR evenly
            for q in M[page]:                                     #pages pointing to page
                newPR += d * init_page_rank[q] / (len(L[q]))      #add share of PageRank from in-links
            page_rank[page] = newPR
        current_perplexity = perplexity(page_rank)
        difference = prev_perplexity - current_perplexity
        if difference < 1:
            convergence_list.append(1)
        else:
            convergence_list.append(0)

        f.write("Current Perplexity value: %d " %current_perplexity)
        f.write("Previous Perplexity value: %d " %prev_perplexity)
        f.write("Difference(Previous - Current): %d \n" %difference)

        print("-----------")
        print(convergence_list)

        prev_perplexity = current_perplexity
        init_page_rank = page_rank.copy()

    f.close()
    return page_rank

PageRank(M,L,0.85)
print(page_rank)

#writing the outputs to files

page_ranks = dict((k,float(v)) for k,v in page_rank.items())

for key,value in page_ranks.items():
    s+=value

f=open('All_Pageranks_for_BFS.txt','w')
for keys,values in sorted(page_ranks.items(), key=lambda x: x[1], reverse=True):
    f.write("\n {0} -> {1}" .format(keys,values))
f.write("\n\nSum of PageRanks = %s" %s)
f.close()

top_50 = []
f=open('All_Pageranks_for_BFS.txt','r')
top_50 = f.readlines()
top_50=[x.strip() for x in top_50]
f.close()

del top_50[0]

f=open('Top_50_Pagerank_through_BFS.txt','w')
for i in range(0,50):
    f.write('%s\n' %top_50[i])
f.close()

f=open('Top_10_Pagerank_through_BFS.txt','w')
for i in range(0,10):
    f.write('%s\n' %top_50[i])
f.close()

ordered_d = {}
f=open('Top_10_Inlink_Counts_for_BFS.txt','w')
ordered_d = OrderedDict(sorted(M.items(), key=lambda x: len(x[1]),reverse=True))

topkeys=[]
topvalues=[]

for k,v in ordered_d.items():
    topkeys.append(k)
    topvalues.append(v)

for i in range(0,10):
    f.write("%s -> "%topkeys[i])
    f.write("%s\n "%topvalues[i])
f.close()

f = open("Sources(No-Inlinks)_BFS", 'w')
sources = []
for i in M:
    if (M[i] == []):
       sources.append(M[i])
       f.write("Source: %s\n" %M[i])
f.write("Total no. of sources = %s\n" %len(sources))
proportion_sources_bfs = float(len(sources)/N)
f.write("Proportion of sources for G1 = %f" %proportion_sources_bfs)
f.close()

f = open("Sinks(No-Outlinks)_BFS", 'w')
for i in L:
    if (L[i] == []):
       f.write("Sink: %s\n" %i)
f.write("Total no. of sinks = %s\n" %len(S))
proportion_sinks_bfs = float(len(S)/N)
f.write("Proportion of sinks for G1 = %f" %proportion_sinks_bfs)
f.close()
