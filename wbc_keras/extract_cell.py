import json
import os
import cv2
import sys

#--------------------------------------------------------------------------------------------
#------------------------------- Defining Functions -----------------------------------------
#--------------------------------------------------------------------------------------------

def confirm_prompt(question: str) -> bool:
    reply = None
    while reply not in ("y", "n"):
        reply = input(f"{question} (y/n): ").casefold()
    return (reply == "y")

#--------------------------------------------------------------------------------------------

def cell_cropper(json_Dir, image_Dir):
    
    for file_name in os.listdir(json_Dir):
    
        try: 
            img_file_name = file_name.replace(".json", ".jpg")
            theJson = os.path.join(json_Dir,file_name)
            theImage = os.path.join(image_Dir,img_file_name)
    
            print(theJson)
            print(theImage)
    
            jsonData = open(theJson)
            data = json.load(jsonData)
            img=cv2.imread(theImage)

            
            if str(data['Camera']) == "Samsung Galaxy S5":

                img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            
            num_cells=int(data['Cell Numbers'])

            for i in range(0,num_cells):
    
                # crop the cell from the image based on the
                # coordinates provided by the json file
                cell_data=data['Cell_'+str(i)]
                x1=int(cell_data['x1'])
                x2=int(cell_data['x2'])
                y1=int(cell_data['y1'])
                y2=int(cell_data['y2'])
                cellType=str(cell_data['Label1'])
                new_img=img[y1:y2,x1:x2,:]
           
                # create directory for cell type 
                # if it doesnt exist.
                path = '/home/user/ai/wbc/cropped/' + cellType
                if not os.path.exists(path):
                    os.makedirs(path)       
            
                # save the new cropped cell image in 
                # the associated directory
                cv2.imwrite(path+'/'+cellType+'_'+img_file_name.replace(".jpg","")+'_'+str(i)+'.png',new_img)
        except:
            pass
def exit_script():

    return "\nuser has 'gracefully' exited cellCropper.py!\n"

#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------

jsonDir=sys.argv[1]
imageDir=sys.argv[2]

userinputs = [jsonDir, imageDir];

for userinput in range(len(userinputs)):
    if userinputs[userinput][-1] == "/":
        userinputs[userinput] = userinputs[userinput][:-1]

print("\n----------------------------------------")
print("\n   json directory  :  " + userinputs[0])
print("  image directory  :  " + userinputs[1])
print("\n----------------------------------------\n")

#allow user to reverse a potential user error
reply = confirm_prompt("Please confirm your json and image directories. Enter 'y' to proceed ")

if reply != False:
    cell_cropper(userinputs[0], userinputs[1])
else:
    print(exit_script())

