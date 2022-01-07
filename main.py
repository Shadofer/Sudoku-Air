import cv2 as cv
import numpy as np

root=np.zeros((1000,1500,3),np.uint8)

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
        


button1=Button([5,5], "1")
button2=Button([75,5], "2")
button3=Button([145,5], "3")
button4=Button([5,75], "4")
button5=Button([75,75], "5")
button6=Button([145,75], "6")
button7=Button([5,145], "7")
button8=Button([75,145], "8")
button9=Button([145,145], "9")

myreset=Button([5,285], "RESET", [200,70])
mysolve=Button([5,375], "SOLVE", [200,70])
myquit=Button([5,465], "QUIT", [200,70])

def ifClicked(self, xcor, ycor):
    if((xcor>=self.x and xcor<=self.x+self.w) and (ycor>=self.y and ycor<=self.y+self.h)):
        return True
    return False


while True:
    root=button1.draw(root)
    root=button2.draw(root)
    root=button3.draw(root)
    root=button4.draw(root)
    root=button5.draw(root)
    root=button6.draw(root)
    root=button7.draw(root)
    root=button8.draw(root)
    root=button9.draw(root)
    root=myreset.draw(root)
    root=mysolve.draw(root)
    root=myquit.draw(root)


    cv.imshow("sudoku air", root)
    cv.waitKey(1)
    
def drawGrid(): #Draw Sudoku Frame
  pass

keypad = []
run = True

while run:
  #DRAW
  #CHECK USER INPUT
  #CHANGE VARIOUS STATES
