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

1. come up with a better name for the project?
2. finish this readme file.
3. find suitable web app host?
4. find more cell image datasets/examples?
5. create a better model. 
  - the model is not perfect and there is a few things I would like to do to try to get closer to perfection.
6. <del>redesign webapp. currently barebones for demonstration purposes.</del>

<br>
<br>



## .h5 file instructions 
<br>
<img align="right" src="https://user-images.githubusercontent.com/105183376/194649993-fd926e92-3e35-4273-a55f-a0c6592064ea.png?raw=true" width="28%">
the leukoRight model tar file can be found in /models with the caveat being that because the file is very large (~32mb) it is split into 2 different parts:  
<br><br>

`partaa` and `partab`

<br><br>
To combine these files into a single tar file use the following command

`cat leukoright_model.tar.gz.parta* >leukoright.tar.gz.joined`

<br><br><br><br>


(in process)
