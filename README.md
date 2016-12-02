# RapVision

This module identifies, analyze and visualize rhymes in rap lyrics

This implementation is still in beta and is not yet optimized to handle slangs and missplelled words


## Usage

RapVision can be used either in Terminal or in jupyter notebook. Import the classes and run

	git clone https://github.com/yohannesaf/Computational-Approach-to-Analyze-and-Visualize-Rap-Lyrics
	cd Computational-Approach-to-Analyze-and-Visualize-Rap-Lyrics
	
	from TextAssemble import RapVision
	RapVision(filepath)

## Example

	from TextAssemble import RapVision
	RapVision('lyrics/mini.md')

	input:

	![alt tag](https://github.com/yohannesaf/Computational-Approach-to-Analyze-and-Visualize-Rap-Lyrics/blob/master/image/K_O.png "Original")

	Output:

	![alt tag](https://github.com/yohannesaf/Computational-Approach-to-Analyze-and-Visualize-Rap-Lyrics/blob/master/image/Kendrick.png "Viduslized")


## Necessary Python Packages

	1. MCL-Markov-Cluster
	2. networkx
	3. nltk 
	4. numpy
	5. pronouncing
	6. pyhyphen
	7. regex
	8. sklearn
	9. unidecode
	10. collections
	
