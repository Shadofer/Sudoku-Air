import cv2 as cv
import numpy as np

root=np.zeros((1000,1500,3),np.uint8)

class Button():
    def  __init__(self, pos, text, size=[70,70]):
        self.pos = pos
        self.size = size
        self.text = text
    
    def draw(self, root):
        x,y= self.pos
        w,h= self.size 
        cv.rectangle(root, self.pos, (x+w, y+h), (255,255,255),2)
        cv.putText(root, self.text, (x+20, y+50), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)
        return root
        
    def ifClicked(self, xcor, ycor):
        if((xcor>=self.pos.x and xcor<=self.pos.x+self.size.w) and (ycor>=self.pos.y and ycor<=self.pos.y+self.size.h)):
            return True
        return False
        
# DEFINE ALL THE BUTTONS
keypad=[]

myreset=Button([5,285], "RESET", [200,70])
mysolve=Button([5,375], "SOLVE", [200,70])
myquit=Button([5,465], "QUIT", [200,70])

for x in range(1, 4):
  for y in range(1, 4):
    keypad.append(Button([70*y+5, 70*x+5], str(x+y)))

#DRAW THE BUTTONS
for btn in keypad:
  btn.draw(root)

myreset.draw(root)
mysolve.draw(root)
myquit.draw(root)

run = True

while run:
    cv.imshow("sudoku air", root)
    
    if(myquit.ifClicked(xcor, ycor)):
        run = False

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
