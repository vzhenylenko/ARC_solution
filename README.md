# ARC (UNFINISHED, AT EARLY STAGE OF DEVELOPMENT)
#### Overview
System dedicated to solve problems from ARC dataset (universal IQ test)  

#### What is **ARC**?
It's a challenge, proposed by Francois Chollet in this paper. The goal of this challenge is to address lack of generalization between different tasks and lack of reasoning in current ML approaches, including deep learning. There is a public part of dataset provided, as well as already completed kaggle [chalange]. For more information, visit [this](https://github.com/fchollet/ARC) github repo, or read the original [paper](https://arxiv.org/abs/1911.01547).

#### DONE:
- output list of figures based on to type of cell's neighbourhood (Moore and reduced von Neunman neighbourhoods)  
  
#### TODO:
- create list of relations
- create graph of relations between figures in input and output
- create difference relation between representations
- search for greatest common subgraphs in differences
- add difference to target picture representation
- create answer from obtained representation

#### Examples:
- There is one task on the image below.
- On the left panel in each row you could see 2 inputs and 1 output (3 rows in total). This is train data.
- On the right panel, there is the test input, for which you should provide output (submit array with pixel colors).
![examples_image](https://camo.githubusercontent.com/e09efad05e838b24ac2b98bcd75c1e67be811262/68747470733a2f2f6172632d62656e63686d61726b2e73332e616d617a6f6e6177732e636f6d2f666967732f6172635f746573745f73706163652e706e67)
