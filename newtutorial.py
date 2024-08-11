import tkinter as tk
from tkinter import messagebox
import random 
class TicTacToe:
    def __init__(self):
        self.root=tk.Tk()
        self.root.title('Welcome to TICTACTOE Game:')
        self.buttons=[]
        self.player='O'
        self.computer='X'
        self.board=[['' for _ in range(3)] for _ in range(3)]
        self.create_board()
        self.root.mainloop()
    def create_board(self):
        for i in range(3):
            row=[]
            for j in range(3):
                button=tk.Button(self.root,width=5,height=2,font=('Arial',20),command=lambda row=i,col=j: self.click(row,col))
                button.grid(row=i,column=j)
                row.append(button)
            self.buttons.append(row)
    def click(self,row,col):
        if self.board[row][col]=='':
            self.board[row][col]=self.player
            self.buttons[row][col].config(text=self.player)
            if self.check_win():
                self.game_over(self.player)
            else:
                self.computer_turn()
        else:
            return
    def computer_turn(self):
        empty_cells=[(i,j) for i in range(3) for j in range(3) if self.board[i][j]=='']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = self.computer
            self.buttons[row][col].config(text=self.computer)
            if self.check_win():
                self.game_over(self.computer)
    def check_win(self):
        for i in range(3):
            if self.board[i][0]==self.board[i][1]==self.board[i][2]!='':
                return True
        for j in range(3):
            if self.board[0][j]==self.board[1][j]==self.board[2][j]!='':
                return True
        if self.board[0][0]==self.board[1][1]==self.board[2][2]!='':
            return True
        if self.board[0][2]==self.board[1][1]==self.board[2][0]!='':
            return True
        return False
    def game_over(self,winner):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)
        tk.messagebox.showinfo("Game Over", f"{winner} wins!")
if __name__ == '__main__':
    game=TicTacToe()
