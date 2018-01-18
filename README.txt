REQUIREMENTS:

1) Python version 3.6.1 (in Pycharm)
2) Install the libraries as mentioned under TASK 2, in Pycharm

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

How To Setup:

Use any IDE, example: Pycharm.

1) Download Pycharm.
2) Go to File -> Settings -> Project -> Project Interpreter
3) Click on the "+" sign on the rightmost side, "+" sign is in light green colour,
   to install the required libraries as mentioned, if not already installed.
4) Copy the program to Pycharm and run.

OR

If using the terminal:

1) Go to the folder where the source code with the py extension exists.
2) Type python <filename>.py
      Eg: python Source_code_for_task_1.py
          python Source_code_for_task_2.py

NOTE: If using Terminal, python environment must be setup for the terminal commands to work. 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Task 1:

File Content:

1) Brief Report : File contains statistics over G1 and G2
                 (Answer for no. of sinks and sources for G1 and G2 as well as their respective proportions for both graphs)

2) Sinks(No-Outlinks)_BFS.txt : File contains all the sinks found from the BFS Graph (G1)
   NOTE: No. of sinks found : 68

3) Sinks(No-Outlinks)_DFS.txt : File contains all the sinks found from the DFS Graph (G2)
   NOTE: No. of sinks found : 82

4) Sources(No-Inlinks)_BFS.txt : File contains all the sources found from the BFS Graph(G1)
   NOTE: No. of sources found : 0

5) Sources(No-Inlinks)_DFS.txt : File contains all the sources found from the DFS Graph(G2)
   NOTE: No. of sources found : 0

6) urlsCrawledBFSInlinkGraph.txt : File contains the in-link graph for BFS ,i.e., G1
   NOTE: format of file: A ['B','C','D']
         where; A is one of the pages of previously crawled 1000 URLs
                B,C,D are the in-links to page A

7) urlsCrawledDFSInlinkGraph.txt : File contains the in-link graph DFS, i.e., G2
   NOTE: format of file: A ['B','C','D']
         where; A is one of the pages of previously crawled 1000 URLs
                B,C,D are the in-links to page A

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Task 2:

Libraries used:

1) import math
2) import pickle
3) from collections import OrderedDict

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

File Content:

1) Perplexity_values_BFS : File contains the current, previous and the difference between current and previous perplexity values obtained from operating on
                           G1(Inlink Graph of BFS) as well as urlsCrawledOutinkGraph.txt(this file contains the outlink graph of BFS)
                           NOTE: Values in the next line indicate values for the next round

2) Perplexity_values_DFS : File contains the current, previous and the difference between current and previous perplexity values obtained from operating on
                           G2(Inlink Graph of DFS) as well as urlsCrawledOutinkGraph.txt(this file contains the outlink graph of DFS)
                           NOTE: Values in the next line indicate values for the next round

3) Top_50_Pagerank_through_BFS : File contains Top 50 pages obtained from G1, based on top 50 pagerank values of G1.
                                 NOTE: Format inside the file: A -> B;
                                       where, A: page and B: pagerank value of the page A 

4) Top_50_Pagerank_through_DFS : File contains Top 50 pages obtained from G2, based on top 50 pagerank values of G2.
				 NOTE: Format inside the file: A -> B;
                                       where, A: page and B: pagerank value of the page A 

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Task 3:

File Content:

1) Top_10_Inlink_Counts_for_BFS : File contains the top 10 pages obtained from G1, based on the top 10 "in-link counts" for G1
                                  NOTE: Format inside the file: A -> B;
                                        where, A: page and B: total number of inlinks on page A 

2) Top_10_Inlink_Counts_for_DFS : File contains the top 10 pages obtained from G2, based on the top 10 "in-link counts" for G2
                                   NOTE: Format inside the file: A -> B;
                                         where, A: page and B: total number of inlinks on page A 

3) Top_10_Pagerank_through_BFS : File contains the top 10 pages obtained from G1, based on the top 10 pagerank values for G1
                                 NOTE: Format inside the file: A -> B;
                                       where, A: page and B: pagerank value of the page A 

4) Top_10_Pagerank_through_DFS : File contains the top 10 pages obtained from G2, based on the top 10 pagerank values for G2  
                                 NOTE: Format inside the file: A -> B;
                                       where, A: page and B: pagerank value of the page A 

5) Comparison and Speculation :  File contains explanation/speculation expected for Task 3

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

NOTE: The Folder named "All_Code" contains every source code as well as all the text files required for Assignment 2.

      INCASE YOU WANT TO RUN THE OTHER PROVIDED SOURCE CODES,
      PLEASE REFER THE LIBRARIES INSIDE THE CODE AND VERIFY YOU HAVE THOSE LIBRARIES INSTALLED, BEFORE RUNNING THE CODE.

      1] PLEASE REFER THE FOLDER "All_Code" TO REFER TO SOURCE CODES FOR:
         a) DFS outlink and inlink graph generation source code ->  DFS-Graph-generation-code.py
         b) BFS outlink and inlink graph generation source code -> BFS-Graphs-generation-code.py

      2] PLEASE REFER THE FOLDER "All_Code" TO REFER THE text files:
         a) containing 1000 Urls crawled via BFS approach: urlsCrawledBFS.txt
         b) containing 1000 Urls crawled via DFS approach: urlsCrawledDFS.txt

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

REFERENCES USED FOR SOLVING THIS ASSIGNMENT:

1]STACK-OVERFLOW AND TUTORIALSPOINT REFERRED FOR PYTHON PROGRAMMING SYNTAXES AND ALSO FOR UNDERSTANDING FEW CONCEPTS, like application of depth-first-search,
  pickle library usage,etc
  a) https://www.tutorialspoint.com/python/string_find.htm
  and many such more links....

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;