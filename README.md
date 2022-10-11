<br><p align="center"><img src="https://raw.githubusercontent.com/originates/leukoRight/main/leukoright.png?raw=true" alt="leukoRight logo" width="20%"></p>
<br>
#### <p align="center">a trained Keras model to recognize white blood cells.</p>
<br> <br>


---
<br>
<br>
<br>

<p align="center">
Heroku has announced that they will no longer offer their free tier after November 28. 
<br>
I will be exploring other options to share this as a web application. In the meantime, an example gif can be seen below.
<br><br></p>



<br><p align="center"><img src="https://raw.githubusercontent.com/originates/leukoRight/main/leukoRightWeb.gif?raw=true" alt="leukoRight web example" width="70%"></p>

<br><br><br><br>

## todo


1. finish this readme file.
2. find suitable web app host?
3. find more cell image datasets/examples?
4. create a better model. 
  - the model is not perfect (seemingly due to an over representation of neutrophils in the training images). 
  - I am looking into ways to increase inference accuracy. 
6. <del>redesign webapp. currently barebones for demonstration purposes.</del>

<br>
<br>

## The model

the leukoRight model has been trained to differentiate the following WBC types.

- Neutrophil
- Band Neutrophil
- Lymphocyte
- Large (activated) lymphocyte
- Monocyte
- Basophil
- Eosinophil
- Metamyelocyte

It is also trained to differentiate Artifacts and Bursted Cells.

<br><br>

## .h5 file instructions 
<br>
I wouldn't suggest using the current model for any purpose, however, if interested—the leukoRight model tar file can be found in /models with the caveat being that because the file is very large (~32mb) it is split into 2 different parts:  
<br><br>

`partaa` and `partab`

<br><br>
To combine these files into a single tar file use the following command

`cat leukoright_model.tar.gz.parta* >leukoright.tar.gz.joined`

<br><br><br><br>


(in process)
