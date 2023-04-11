class TicTacToe:
    def __init__(self):
        self._gamecount=0
        k=1
        self._game_status=["WIN","DRAW","IN_PROGRESS"]
        self.arr=list()
        self.row,self.cols=(3,3)
        for i in range(0,3):
            self.arr.append([0]*self.cols)
        for i in range(0,self.row):
            self.arr.append(self.cols)
        for i in range(0,self.row):
            for j in range(0,self.cols):
                self.arr[i][j]=k
                k=k+1
    def is_already_Marked(self,pos):
         for i in range(0,self.row):
                for j in range(0,self.cols):
                    if self.arr[i][j]==pos:
                        if self.arr[i][j]=='X' or self.arr[i][j]=='Y':
                            return True
                        else:
                            return False
    def isValidPos(self,pso):
        pos=int(pso)
        if pos<0 or pos>9:
            return False
        else:
            return True 
    def show(self):
        for i in range(0,self.row):
            for j in range(0,self.cols):
                print(self.arr[i][j],end="  ")
            print("\n")
    def markPosition(self,pso,sym):
        pos=int(pso)
        if self.isValidPos(pos)==True and self.is_already_Marked(pos)==False:
            for i in range(0,self.row):
                for j in range(0,self.cols):
                    if pos==self.arr[i][j]:
                        self.arr[i][j]=sym
            self._gamecount=self._gamecount+1
            return True
        else:
            return False
    def along_rows(self):
        x=0
        y=0
        for i in range(0,self.row):
            for j in range(0,self.cols):
                if self.arr[i][j]=='X':
                    x=x+1
                elif self.arr[i][j]=='Y':
                    y=y+1
            if x==3 or y==3:
                return self._game_status[0]
            else:
                x=0
                y=0
        return self._game_status[2]
    def along_columns(self):
        x,y=(0,0)
        for i in range(0,3):
            for j in range(0,3):
                if self.arr[j][i]=='X':
                    x=x+1
                elif self.arr[j][i]=='Y':
                    y=y+1
            if x==3 or y==3:
                return self._game_status[0]
            else:
                x=0
                y=0
        return self._game_status[2]
    def along_diagonals(self):
        x=0
        y=0
        for i in range(0,self.row):
            for j in range(i,i+1):
                if self.arr[i][j]=='X':
                    x=x+1
                elif self.arr[i][j]=='Y':
                    y=y+1
        if x==3 or y==3:
            print("here i return ")
            return self._game_status[0]
        else:
            x=0
            y=0
            j=2
            for i in range(0,self.row):
                if self.arr[i][j]=='X':
                    x=x+1
                elif self.arr[i][j]=='Y':
                    y=y+1
            if x==3 or y==3:
                return self._game_status[0]
            else:
                return self._game_status[2]
    def get_result(self):
        if self.along_columns()==self._game_status[0]:
            return self._game_status[0]
        elif self.along_rows()==self._game_status[0]:
            return self._game_status[0]
        elif self.along_diagonals()==self._game_status[0]:
            return self._game_status[0]
        elif self._gamecount==9:
            return self._game_status[1]
        else:
            return self._game_status[2]
class Play_Game(TicTacToe):
    def __init__(self):TicTacToe.__init__(self)
    def play_game(self):
        pso=0
        while(self.get_result()==self._game_status[2]):
            self.show()
            status=False
            while status==False:
                    print("Player 1 Enter position:",end=" ")
                    pos=input()
                    if self.markPosition(pos,'X')==True:
                        print("the block is true")
                        status=True
                    else:
                        print("Player 1 not a valid position")
                        status=False
            if self.get_result()==self._game_status[0]:
                print("Player 1 Wins:")
                self.show()
                quit()
            if self.get_result()==self._game_status[1]:
                print("Game Draw:")
                self.show()
                # 
                return
            self.show()
            status=False
            while status==False:
                    print("Player 2 Enter position: ",end=" ")
                    pos=input()
                    if self.markPosition(pos,'Y')==True:
                        status=True
                    else:
                        print("Player 2 not a valid position")
                        status=False
            if self.get_result()==self._game_status[0]:
                print("Player 2 wins")
                self.show()
                quit()
            if self.get_result()==self._game_status[1]:
                print("Game Draw:")
                self.show()
                # quit()
                return
def main():
    a=Play_Game()
    a.play_game()
if __name__=="__main__":
    main()