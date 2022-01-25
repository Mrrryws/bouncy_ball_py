from tkinter import *
import time
import random
import webbrowser
from tkinter import Tk, PhotoImage, ttk
import csv
from csv import reader
import operator


#  Window configuration
def configure_window():
    window.geometry("1280x720")
    window.configure(bg="darkblue")
    window.title("Bouncy Ball")


# Welcome Button Configuration
def WelcomeButtonPress():
    global WelcomeImage
    top = Toplevel()
    top.title('Welcome to Bouncy Ball!')
    WelcomeImage = PhotoImage(file="photo.png")
    WelcomeLabel = Label(top, image=WelcomeImage).pack()


# Good luck image, 'How to play' button configuration
def HowToPlayFunction():
    HowToPlay = Tk()
    HowToPlay.geometry("640x415")
    HowToPlay.configure(bg="cornflowerblue")
    HowToPlay.title("How to Play")
    HowToPlayLabel = Label(HowToPlay, text="HOW TO PLAY\n✦",
                           bg="cornflowerblue", font=("Arial", 15)).grid(row=0)
    HowToPlayLabel2 = Label(HowToPlay,
                            text="<Return> = Start/Restart the game." +
                            "\n<Space> = Pause the game." +
                            "\n<B> = Bosskey (Only use in emergency cases)" +
                            "\nBosskey also pauses the game" +
                            " so don't worry about your progress:)" +
                            "\n<C> !!!CHEAT!!! Makes the bar bigger." +
                            "\n<V> !!!CHEAT!!! Makes the ball bigger." +
                            "\nKeep in mind:" +
                            "\nCheats maintain the object" +
                            " moving in the same way" +
                            "and the bar/ball restarts from the middle" +
                            "\nAfter the game is over, you" +
                            " will be prompted with a window" +
                            " that asks for the name." +
                            "\nEnter your name, Press 'Submit' and then" +
                            " press 'Exit'" +
                            "\nAfter pressing 'Exit' in the window," +
                            " restarting the game will not keep the previous" +
                            " score.\nThe leaderboard will" +
                            " be updated the next" +
                            " time you open the game.\nTips and tricks:" +
                            "\nUse ball cheat only when ball is going up:)" +
                            "\n✦\n✦\n✦\n✦\n✦",
                            bg="cornflowerblue",).grid(row=1)
# Introducing good luck image
    top = Toplevel()
    global GoodLuckImage
    GoodLuckImage = PhotoImage(file="GoodLuck.png")
    GoodLuck = Label(top, image=GoodLuckImage).grid(row=2)
    LeaderboardCloseButton = Button(HowToPlay, text="Close",
                                    width=15,
                                    command=HowToPlay.destroy)
    LeaderboardCloseButton.grid(row=4, column=0)
    HowToPlay.mainloop()


# Leaderboard Button Configuration
def ShowLeaderboardScores():
    def LeaderboardScores():
        # Read the player name and player score from external files
        GetName = open("namefile.txt")
        PlayerName = GetName.read()
        GetScore = open("scorefile.txt")
        PlayerScore = GetScore.read()
        ScoreTextOpen = open("Score.txt", "a", newline="")
# Designing the row to have the name first, then the score
        RowDesign = (PlayerName, str(PlayerScore))
        writer = csv.writer(ScoreTextOpen)
# Write the row in the table
        writer.writerow(RowDesign)
        ScoreTextOpen.close()
        ScoreList = []
        with open('Score.txt', 'r') as csv_file:
            readCSV = csv.reader(csv_file, delimiter=',')
# Sort according to the score. From highest to lowest
            sort = sorted(readCSV, key=operator.itemgetter(1), reverse=True)
            for row in sort:
                if row not in ScoreList:
                    ScoreList.append(row)
        for i, (name, score) in enumerate(ScoreList, start=1):
            LeaderList.insert("", "end", values=(i, name, score))
# Window configuration for leaderboard
    LeaderboardWindow = Tk()
    LeaderboardWindow.configure(bg="skyblue")
    LeaderboardWindow.title("Leaderboard Table")
    label = Label(LeaderboardWindow, text="Leaderboard",
                  bg="skyblue", font=("Arial", 25)).grid(row=0, columnspan=3)
# Create 3 columns: Position, Name and Score
    cols = ('Position', 'Name', 'Score')
    LeaderList = ttk.Treeview(LeaderboardWindow, columns=cols, show='headings')

    for col in cols:
        LeaderList.heading(col, text=col)

    LeaderList.grid(row=1, column=0, columnspan=1)
# Button to close the Leaderbord window
    LeaderboardCloseButton = Button(LeaderboardWindow, text="Close",
                                    width=15,
                                    command=LeaderboardWindow.destroy)
    LeaderboardCloseButton.grid(row=4, column=0)

    LeaderboardScores()
    LeaderboardWindow.mainloop()


# Take name after game is over
def NameForLeaderboard():
    # Also write the name to an external file
    def write_File(text_File):
        NameFile = open("namefile.txt", "w")
        user_Input = text_File.get()
        NameFile.write(user_Input)
        NameFile.close()
    NameInput = Tk()
    Label(NameInput, text="Name").grid(row=0)
    NameTake = Entry(NameInput)
    NameTake.grid(row=0, column=1)
# Write the name to the file after 'Submit' is pressed
    SubmitName = Button(NameInput, text="Submit Name",
                        command=lambda:
                            write_File(NameTake)).grid(row=1, column=0)
    ExitName = Button(NameInput, text="Exit",
                      command=NameInput.destroy).grid(row=1, column=1)
    NameInput.mainloop()

window = Tk()
# Welcome Button
BounceballButton = Button(window, text="\nWelcome to Bouncy Ball\n",
                          fg="white", bg="deepskyblue", font=("Arial", 40),
                          padx=60, pady=30, command=WelcomeButtonPress)
BounceballButton.pack()

# How to Play Button
HowToPlayButton = Button(window, text="✯How to Play✯",
                         fg="white", bg="deepskyblue", font=("Arial", 30),
                         padx=60, pady=30, command=HowToPlayFunction)
HowToPlayButton.pack()

# Play Button
PlayButton = Button(window, text="✯Play✯", fg="white",
                    bg="deepskyblue", font=("Arial", 30),
                    padx=60, pady=30, command=window.destroy)
PlayButton.pack()

# Leaderboard Button
LeaderboardButton = Button(window, text="✯Leaderboard✯",
                           fg="white", bg="deepskyblue", font=("Arial", 30),
                           padx=60, pady=30, command=ShowLeaderboardScores)
LeaderboardButton.pack()

# Exit Button
ExitButton = Button(window, text="✯Exit✯",
                    fg="white", bg="deepskyblue",
                    font=("Arial", 30), padx=60,
                    pady=30, command=quit)
ExitButton.pack()

configure_window()

window.mainloop()


# Class for the bricks
class Bricks:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(5, 5, 84, 35, fill=color, width=2)


# Class for configuring ball, ball movement, ball colision, etc.
class Ball:
    def __init__(self, canvas, color, movingbar, bricks, score):
        self.bricks = bricks
        self.canvas = canvas
        self.movingbar = movingbar
        self.score = score
        self.bottom_hit = False
        self.hit = 0
        self.id = canvas.create_oval(10, 10, 35, 35, fill=color, width=1)
        self.canvas.move(self.id, 660, 460)
        start = [3]
        self.x = start[0]
        self.y = start[0]
        self.canvas.move(self.id, self.x, self.y)
        self.canvas_height = canvas.winfo_height()
        self.canvas_width = canvas.winfo_width()
        self.canvas.bind_all("<v>", self.ballcheat)

# Cheat to make the ball bigger (ball keeps its motion)
    def ballcheat(self, event):
        self.canvas.delete(self.id)
        self.id = canvas.create_oval(10, 10, 50, 50, fill="white", width=1)
        self.canvas.move(self.id, 660, 460)

# Function to destroy the brick hit by the ball.
# Add 1 to the score when the brick is hit and delete that brick.
    def DestroyHitBrick(self, pos):
        for brick_line in self.bricks:
            for brick in brick_line:
                brick_pos = self.canvas.coords(brick.id)
                try:
                    if pos[2] >= brick_pos[0] and pos[0] <= brick_pos[2]:
                        if pos[3] >= brick_pos[1] and pos[1] <= brick_pos[3]:
                            self.hit += 1
                            self.score.configure(text="Score: " +
                                                 str(self.hit))
                            self.canvas.delete(brick.id)
                            return True
                except:
                    continue
        return False

# Function that determines if the ball hit the moving bar or not
    def MovingbarHitBounce(self, pos):
        movingbar_pos = self.canvas.coords(self.movingbar.id)
        if pos[2] >= movingbar_pos[0] and pos[0] <= movingbar_pos[2]:
            if pos[3] >= movingbar_pos[1] and pos[1] <= movingbar_pos[3]:
                return True
            return False

# Function to determine ball positioning
    def ballpositioning(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        start = [3]
        random.shuffle(start)
        if self.DestroyHitBrick(pos):
            self.y = start[0]
        if pos[1] <= 0:
            self.y = start[0]
        if pos[3] >= self.canvas_height:
            self.bottom_hit = True
        if pos[0] <= 0:
            self.x = start[0]
        if pos[2] >= self.canvas_width:
            self.x = -start[0]
        if self.MovingbarHitBounce(pos):
            self.y = -start[0]


# Class for the moving bar
class Movingbar:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 350, 20, fill="dodgerblue")
        self.canvas.move(self.id, 500, 620)
        self.x = 0
        self.pausemovement = 0
        self.canvas_width = canvas.winfo_width()
# Binding all keys related to the movingbar
        self.canvas.bind_all("<Left>", self.turn_left)
        self.canvas.bind_all("<Right>", self.turn_right)
        self.canvas.bind_all("<space>", self.pauser)
        self.canvas.bind_all("<b>", self.bosskey)
        self.canvas.bind_all("<c>", self.barcheat)

    def barpositioning(self):
        pos = self.canvas.coords(self.id)
        if pos[0] + self.x <= 0:
            self.x = 0
        if pos[2] + self.x >= self.canvas_width:
            self.x = 0
        self.canvas.move(self.id, self.x, 0)

# Function defining left movement
    def turn_left(self, event):
        self.x = -4
        self.canvas.move(self.id, self.x, 0)

# Function defining right movement
    def turn_right(self, event):
        self.x = 4
        self.canvas.move(self.id, self.x, 0)

# Function for the pause when 'SPACE' is pressed
    def pauser(self, event):
        self.pausemovement += 1
        if self.pausemovement == 2:
            self.pausemovement = 0

# Bosskey that opens python official website when 'B' is pressed
    def bosskey(self, event):
        self.pausemovement += 1
        if self.pausemovement == 2:
            self.pausemovement = 0
# Open web when bosskey is pressed
        webbrowser.open('https://www.python.org/')

# Cheat that makes the bar bigger when 'C' is pressed
    def barcheat(self, event):
        self.canvas.delete(self.id)
        self.id = canvas.create_rectangle(0, 0, 500, 25, fill="dodgerblue")
        self.canvas.move(self.id, 450, 620)

playing = False


# Function for the actual game start
def start_game(event):
    global playing
    if playing is False:
        playing = True
        score.configure(text="Score: 00")
        canvas.delete("all")
        BallColour = ["mistyrose", "lavender", "white"]

        BrickColour = ["cornflowerblue", "deepskyblue",
                       "lightskyblue", "steelblue", "aqua",
                       "paleturquoise", "azure"]
        random.shuffle(BallColour)
        movingbar = Movingbar(canvas, "blue")
# Create the brick pattern using 2 for s. 5x15 bricks
        bricks = []
        for i in range(0, 6):
            brks = []
            for j in range(0, 15):
                random.shuffle(BrickColour)
                createbrick = Bricks(canvas, BrickColour[0])
                brks.append(createbrick)
            bricks.append(brks)

        for i in range(0, 5):
            for j in range(0, 15):
                canvas.move(bricks[i][j].id, 84 * j, 35 * i)
        ball = Ball(canvas, BallColour[0], movingbar, bricks, score)
        window.update_idletasks()
        window.update()
        time.sleep(1)
        while 1:
            # if 'game is not paused'
            if movingbar.pausemovement != 1:
                try:
                    canvas.delete(pause)
                    del pause
                except:
                    pass
# Condition for the end of the game
                if not ball.bottom_hit:
                    ball.ballpositioning()
                    movingbar.barpositioning()
                    window.update_idletasks()
                    window.update()
                    time.sleep(0.01)
# Condition to win: Destroy all 75 bricks
                    if ball.hit == 75:
                        canvas.create_text(640, 350,
                                           text="YOU WON THE GAME",
                                           fill="lime", font="Consolas 55 ")
# Write the score to a file
                        ScoreFile = open("scorefile.txt", "w")
                        ScoreStr = str(ball.hit)
                        ScoreFile.write(ScoreStr)
                        ScoreFile.close()
                        window.update_idletasks()
                        window.update()
                        playing = False
                        NameForLeaderboard()
                        break
                else:
                    canvas.create_text(640, 350, text="GAME OVER!",
                                       fill="red", font=("Arial", 40))
                    canvas.create_text(640, 400,
                                       text="Press Enter to retry!" +
                                       "(This try will not be scored)",
                                       fill="red", font="Arial, 20")
# Write the score to a file
                    ScoreFile = open("scorefile.txt", "w")
                    ScoreStr = str(ball.hit)
                    if (ball.hit < 10):
                        ScoreStr = "0"+str(ball.hit)
                    ScoreFile.write(ScoreStr)
                    ScoreFile.close()
                    window.update_idletasks()
                    window.update()
                    playing = False
                    NameForLeaderboard()
                    break
# else: if 'game is paused'
            else:
                try:
                    if pause is None:
                        pass
                except:
                    pause = canvas.create_text(640, 350,
                                               text="Game is now on pause!" +
                                               "\nPress Space to unpause!",
                                               fill="magenta", font="Arial 30")
                window.update_idletasks()
                window.update()
# Configuration of the main window
window = Tk()
window.title("Bouncy Ball")
window.geometry("1280x720")
canvas = Canvas(window, width=1280, height=650, bd=0,
                highlightthickness=0, highlightbackground="Red", bg="Black")
canvas.pack(padx=10, pady=10)
score = Label(height=50, width=80, text="Score:", font="Consolas 14 bold")
score.pack(side="left")
window.update()
window.bind("<Return>", start_game)
canvas.create_text(640, 350, text="Press Enter to start the game!",
                   fill="skyblue", font="Arial 35")

window.mainloop()
