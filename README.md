# TakeAPic : A Tool to improve your social media experience
TakeAPic is Data Science product that analyzes the 6 fundemental facial expressions + neutral expression. 

## Web Application: http://takeapic.online/

TakeAPic.online is a webapp that I build and develop by utilizing Google Vision API for my Facial Expression Analyzer. 
TakeAPic can be used as an additional **computerized** eyes for your social media picture uploads. 
The program analyzes your images that you submit in the directory, ranks them with respect to highest happiness and lowest sadness scores; and returns you the top 3 happiest pictures so that you can use them as an album cover or your profile picture. 

Here is a quick video of how the app works. App video:
<img alt="App_Video" src="./TakeAPic/static/img/takeapic01302018 (1).gif" height="500" width="1000" />

## Project Presentation:
Slides for the project presentation:
<a href="https://docs.google.com/presentation/d/e/2PACX-1vSYFRupRBmiBZh3q1zJs5VcbirzJ66oHGLc7fG9kCgjYGJF6SGTEoOlktySnfqu0rnE-rO1yz1elA_2/pub?start=true&loop=false&delayms=15000"> Presentation </a>

## Modelling: Into the Weeds...
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






