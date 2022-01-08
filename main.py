import cv2 as cv
import numpy as np

root=np.zeros((1000,1500,3),np.uint8)

keys= [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]

def drawALL(root, keypad):
    for button in keypad:
        x,y= button.pos
        w,h= button.size 
        cv.rectangle(root, button.pos, (x+w, y+h), (255,255,255),2)
        cv.putText(root, button.text, (x+20, y+50), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)
    return root
    


class Button():
    def  __init__(self, pos, text, size=[70,70]):
        self.pos= pos
        self.size= size
        self.text= text
    
    def draw(self, root):
        x,y= self.pos
        w,h= self.size 
        cv.rectangle(root, self.pos, (x+w, y+h), (255,255,255),2)
        cv.putText(root, self.text, (x+20, y+50), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)
        return root
        
    def ifClicked(self, xcor, ycor):
        if((xcor>=self.x and xcor<=self.x+self.w) and (ycor>=self.y and ycor<=self.y+self.h)):
            return True
        return False
        

keypad= []

myreset=Button([5,285], "RESET", [200,70])
mysolve=Button([5,375], "SOLVE", [200,70])
myquit=Button([5,465], "QUIT", [200,70])

for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        keypad.append(Button([70*j+5, 70*i+5], key))


while True:
   
    root= drawALL(root, keypad)
    root=myreset.draw(root)
    root=mysolve.draw(root)
    root=myquit.draw(root)


    cv.imshow("sudoku air", root)
    cv.waitKey(1)
    
def drawGrid(): #Draw Sudoku Frame
  pass

run = True

while run:
  #DRAW
  #CHECK USER INPUT
  #CHANGE VARIOUS STATES
