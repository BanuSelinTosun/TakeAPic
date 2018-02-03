# Facial_Expression_Analyzer
A Data Science product that analyzes the 6 fundemental facial expressions + neutral expression. 

I used FERG DB with 256 pixel resolution, using ~ 55700 images. The classes involved:
  * Happiness
  * Sadness
  * Anger
  * Surprise
  * Fear
  * Disgust
  * Neutral
  
Using a in house CNN with 11 hidden layers + sigmoid outlayer, I achieved approximately 99 % accuracy. The confusion matrix is shared below indicated the misidentified classes as fear vs sadness, and anger vs surprise. 

<img alt="MultiClassification_ConfusionMatrix_for_FERG_DB_256" src="./TakeAPic/MultiClassification_ConfusionMatrix_for_FERG_DB_256.png" height="300" width="350" />

The 256 x 256 images are reduced to 48 x 48 pixels. 

Slides for the project presentation:
<a href="https://docs.google.com/presentation/d/e/2PACX-1vSYFRupRBmiBZh3q1zJs5VcbirzJ66oHGLc7fG9kCgjYGJF6SGTEoOlktySnfqu0rnE-rO1yz1elA_2/pub?start=true&loop=false&delayms=15000"> Presentation </a>


