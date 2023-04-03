
<br><p align="center"><img src="https://raw.githubusercontent.com/originates/leukoRight/main/leukoright.png?raw=true" alt="leukoRight logo" width="10%"></p>
<h1 align="center">leukoRight</h1>


#### <p align="center">Your personal WBC expert!</p>

<br>
LeukoRight is a trained Keras model and web app that has been trained to recognize white blood cells with ease! It can differentiate between 8 types of WBCs and can also differentiate artifacts and bursted cells. You can drag images of stained white blood cells into the app and after clicking submit, LeukoRight will immediately tell you which WBC it is!

<br><p align="center"><img src="https://raw.githubusercontent.com/originates/leukoRight/main/leukoRightWeb.gif?raw=true" alt="leukoRight web example" width="55%"></p>



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

The **leukoRight model tar file** can be found in `/models`. However, please note that this model is not intended to be used in a real healthcare setting. The file is very large (~32mb) and is split into 2 different parts: `partaa` and `partab`. To combine these files into a single tar file use the following command:

`cat leukoright_model.tar.gz.parta* >leukoright.tar.gz.joined`

<br>

## License
```
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
