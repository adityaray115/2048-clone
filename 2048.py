import tkinter as tk
import colors as c
import random
import msvcrt

grid_size=4
class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")

        self.main_grid=tk.Frame(
            self, bg=c.GRID_COLOR, bd=3, width=600, height=600
        )
        self.main_grid.grid(pady=(100,0))
        self.make_GUI()
        self.start_game()
        self.master.bind("<Left>",self.left)
        self.master.bind("<Right>",self.right)
        self.master.bind("<Up>",self.up)
        self.master.bind("<Down>",self.down)
        self.mainloop()


    def make_GUI(self):
        self.cells=[]
        for i in range(grid_size):
            row=[]
            for j in range(grid_size):
                cell_frame=tk.Frame(
                    self.main_grid,
                    bg=c.EMPTY_CELL_COLOR,
                    width=150,
                    height=150
                )
                cell_frame.grid(row=i,column=j,padx=5, pady=5)
                cell_number=tk.Label(self.main_grid, bg=c.EMPTY_CELL_COLOR)
                cell_number.grid(row=i,column=j)
                cell_data={"frame":cell_frame, "number":cell_number}
                row.append(cell_data)
            self.cells.append(row)

        score_frame=tk.Frame(self)
        score_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(
            score_frame,
            text="Score",
            font=c.LABEL_FONT
        ).grid(row=0)
        self.score_label=tk.Label(score_frame, text="0",font=c.LABEL_FONT)
        self.score_label.grid(row=1)
        


    def start_game(self):
        # create a matrix to store values
        self.matrix=[[0]*grid_size for _ in range(grid_size)]
        # self.cells[3][3]["number"].configure(text="hi")
        row=random.randint(0,grid_size-1)
        col=random.randint(0,grid_size-1)
        self.matrix[row][col]=2
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONT,
            text="2"
        )
        while(self.matrix[row][col]!=0):
            row=random.randint(0,grid_size-1)
            col=random.randint(0,grid_size-1)
        self.matrix[row][col]=2
        self.cells[row][col]["frame"].configure(bg=c.CELL_COLORS[2])
        self.cells[row][col]["number"].configure(
            bg=c.CELL_COLORS[2],
            fg=c.CELL_NUMBER_COLORS[2],
            font=c.CELL_NUMBER_FONT,
            text="2"
        )
        self.score=0


    def stack(self):
        new_matrix =[[0]*grid_size for _ in range(grid_size)]
        for i in range(grid_size):
            fill_position=0
            for j in range(grid_size):
                if self.matrix[i][j]!=0:
                    new_matrix[i][fill_position]=self.matrix[i][j]
                    fill_position+=1
        self.matrix=new_matrix

    def combine(self):
        for i in range(grid_size):
            for j in range(grid_size-1):
                if self.matrix[i][j]!=0 and self.matrix[i][j]==self.matrix[i][j+1]:
                    self.matrix[i][j]*=2
                    self.matrix[i][j+1]=0
                    self.score +=self.matrix[i][j]

    def reverse(self):
        new_matrix=[]
        for i in range(grid_size):
            new_matrix.append([])
            for j in range(grid_size):
                new_matrix[i].append(self.matrix[i][grid_size-1-j])
        self.matrix=new_matrix
    
    def transpose(self):
        new_matrix=[[0] * grid_size for _ in range(grid_size)]
        for i in range(grid_size):
            for j in range(grid_size):
                new_matrix[i][j]=self.matrix[j][i]
        self.matrix=new_matrix


    def add_new_tile(self):
        row=random.randint(0,grid_size-1)
        col=random.randint(0,grid_size-1)
        while(self.matrix[row][col]!=0):
            row=random.randint(0,grid_size-1)
            col=random.randint(0,grid_size-1)
        self.matrix[row][col]=random.choice([2,4])


    def update_GUI(self):
        for i in range(grid_size):
            for j in range(grid_size):
                cell_value=self.matrix[i][j]
                if cell_value ==0:
                    self.cells[i][j]["frame"].configure(bg=c.EMPTY_CELL_COLOR)
                    self.cells[i][j]["number"].configure(bg=c.EMPTY_CELL_COLOR,text="")
                else:
                    self.cells[i][j]["frame"].configure(bg=c.CELL_COLORS[cell_value])
                    self.cells[i][j]["number"].configure(
                        bg=c.CELL_COLORS[cell_value],
                        # fg=c.CELL_NUMBER_FONT,
                        font=c.CELL_NUMBER_FONT,
                        text=str(cell_value)
                    )
        self.score_label.configure(text=self.score)
        self.update_idletasks()

    def left(self,event):
        new_matrix=self.matrix
        self.stack()
        self.combine()
        self.stack()
        if(new_matrix==self.matrix):
            return
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def right(self,event):
        new_matrix=self.matrix
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        if(new_matrix==self.matrix):
            return
        self.add_new_tile()
        self.update_GUI()
        self.game_over()


    def up(self,event):
        new_matrix=self.matrix
        self.transpose()
        self.stack()
        self.combine()
        self.stack()
        self.transpose()
        if(new_matrix==self.matrix):
            return
        self.add_new_tile()
        self.update_GUI()
        self.game_over()

    def down(self,event):
        new_matrix=self.matrix  
        self.transpose()
        self.reverse()
        self.stack()
        self.combine()
        self.stack()
        self.reverse()
        self.transpose()
        if(new_matrix==self.matrix):
            return
        self.add_new_tile()
        self.update_GUI()
        self.game_over()    

    def horizontal_move(self):
        for i in range(grid_size):
            for j in range(grid_size-1):
                if self.matrix[i][j] == self.matrix[i][j+1]:return True
        return False

    def vertical_move(self):
        for i in range(grid_size-1):
            for j in range(grid_size):
                if self.matrix[i][j] == self.matrix[i+1][j]:return True
        return False
    
    def game_over(self):
        if any(2048 in row for row in self.matrix):
            game_over_frame=tk.Frame(self.main_grid,bordewidth=3)
            game_over_frame.place(relx=0.5,rely=0.5,anchor="center")
            tk.Label(
                game_over_frame,
                text="YOU REACHED 2048!",
                bg=c.WINNER_BG,
                font=c.CELL_NUMBER_FONT
            ).pack()
            while(True):
                if msvcrt.kbhit():
                    if ord(msvcrt.getch()) == 32:
                        main()
        elif not any(0 in row for row in self.matrix) and not self.horizontal_move() and not self.vertical_move():
            game_over_frame=tk.Frame(self.main_grid,borderwidth=3)
            game_over_frame.place(relx=0.5,rely=0.5,anchor="center")
            tk.Label(
                game_over_frame,
                text="GAME OVER!",
                bg=c.LOSER_BG,
                font=c.CELL_NUMBER_FONT
            ).pack()
            while(True):
                if msvcrt.kbhit():
                    if ord(msvcrt.getch()) == 32:
                        main()

def main():
    Game()

if __name__ == "__main__":
    main()
