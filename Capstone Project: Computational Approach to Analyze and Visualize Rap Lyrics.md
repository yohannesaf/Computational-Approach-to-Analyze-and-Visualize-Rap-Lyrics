## Computation Approach to Analyze and Visualize Rap Lyrics

Rapping, spoken rhyming words, involves to creatively construct an elaborate and meaningful story. Rapping differ from spoken word poetry by it's usage of external musical beat. While rapping has its roots in Africa, rap music reemerged in New York in the 1970s. Since its reemergence, rap has rapidly evolved from simple rhyming intended for a party atmosphere, to much more complex word play rhyming to genre-crossing of today that has a global reach.

Analyzing rap lyrics algorithmically requires understanding the different types of rhyming structure; perfect and imperfect rhymes.[1] Perfect rhymes consists of words that sounds similar such as school and stool. Imperfect rhymes only partially share similar sounds; train and restrain are imperfect rhymes

The aim of this capstone project is to create a web app that identify and visually present families of words that rhyme; words that rhymes will be highlighted using similar color[?]. The outline of the process is as follows:

1. Tokenize each word and translate each word into phonetic language. CMU dictionary will be used to achieve such task.

2. Devise a rhyme scoring system between each words. This will yield an undirected graph with syllables as nodes and their score as the weight of the edges. Stressed syllable of words is rhymes tennd to be heard most strongly between two stressed or emphasized syllables. As such, scoring scheme will follow as such.

Approach 1:
- Two matching stressed syllables are given the highest score possibles.
- A pair of syllables with a single stressed are less likely to rhymes and thus are given a lower score
- The lowest score is given to two unstressed syllables.

Approach 2:
- Use similarity metric between phonetic words to assign a score value of each rhyme.

[Final score allocation will depend based on qualitative evaluation of MCL Algorithm]

3. Group each rhyming words based on their rhyming sounds. Markov Cluster Algorithm will be used to group the nodes. The MCL Algorithm simulates random walks within  a graph by alternation of two operators called expansion and inflation. Expansion coincides with taking the power of a stochastic matrix using the normal matrix product (i.e. matrix squaring). Inflation corresponds with taking the Hadamard power of a matrix (taking powers entry wise), followed by a scaling step, such that the resulting matrix is stochastic again, i.e. the matrix elements (on each column) correspond to probability values.[6]

Interpretation of MCL output:
- Sparse matrix M s.t. M(i,j) in the range (0, 1).
- None-zero entries within the same row form a cluster. As such, number of clusters are not specified ahead of time.
- To speed up convergence of the algorithm, data points close to zero set to 0.  

4. Devise a visualization scheme. 

- Syllables that fall under the same rhyme category will be displayed in the same color.

In the following weeks, I will be researching other text/lyrics analysis papers to create a scoring scheme for rhymes and means of visualization. Lyrics used for evaluation of the algorithms will be scrapped from genius.com. The capstone project will presented with slides and potentially have a demonstration of the web application.


  

[1] Hinton Erik & Eastwood Joel. "Playing With Pop Culture: Writing an Algorithm To analyses and Visualize Lyrics From the Musical "Hamilton." 
[2] Woods, David L., E. Williams Yund, Timothy J Herrom, & Matthew A. I. Ua Cruadhlaoich."Consonant Identification in Consonant-Vowel_Consonant Syllables in speech_spectrum Noise" 
[3] genius.com
[4] http://www.speech.cs.cmu.edu/cgi-bin/cmudict
[5] https://www.youtube.com/watch?v=ZgJyhKEZ8QU
[6] http://www.micans.org/mcl/intro.html

