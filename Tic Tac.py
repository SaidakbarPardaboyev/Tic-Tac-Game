import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


os.system("cls")

class TicTac(QMainWindow):
    __count = 0
    def __init__(self):
        super().__init__()

        self.Create_Meny()

        self.setWindowTitle("Tic Tac")
        self.setWindowIcon(QIcon("C:/Users/user/Desktop/Tic Tac/tic-tac-toe.ico"))
        self.setFixedSize(550,550)

        self.setStyleSheet("""
            background-color: #F0F2F5;
            """)
        
        self.btn1 = QPushButton(self, clicked=lambda: self.btn_click(self.btn1, 1))
        self.btn1.setGeometry(50, 50, 150, 150)
        self.btn1.setFont(QFont("Aptos", 60, weight= 50))
        self.btn1.setStyleSheet("""
            background-color: white;
            border-style: solid;
            border-width: 5px;
            border-color: black;
            color: black;
                                """)

        self.btn2 = QPushButton(self, clicked=lambda: self.btn_click(self.btn2, 2))
        self.btn2.setGeometry(195, 50, 150, 150)
        self.btn2.setFont(QFont("Aptos", 60, weight= 50))
        self.btn2.setStyleSheet("""
            background-color: white;
            border-style: solid;
            border-width: 5px;
            border-color: black;
            color: black;
                                """)

        self.btn3 = QPushButton(self, clicked=lambda: self.btn_click(self.btn3, 3))
        self.btn3.setGeometry(340, 50, 150, 150)
        self.btn3.setFont(QFont("Aptos", 60, weight= 50))
        self.btn3.setStyleSheet("""
            background-color: white;
            border-style: solid;
            border-width: 5px;
            border-color: black;
            color: black;
                                """)
        
        self.btn4 = QPushButton(self, clicked=lambda: self.btn_click(self.btn4, 4))
        self.btn4.setGeometry(50, 195, 150, 150)
        self.btn4.setFont(QFont("Aptos", 60, weight= 50))
        self.btn4.setStyleSheet("""
            background-color: white;
            border-style: solid;
            border-width: 5px;
            border-color: black;
            color: black;
                                """)

        self.btn5 = QPushButton(self, clicked=lambda: self.btn_click(self.btn5, 5))
        self.btn5.setGeometry(195, 195, 150, 150)
        self.btn5.setFont(QFont("Aptos", 60, weight= 50))
        self.btn5.setStyleSheet("""
            background-color: white;
            border-style: solid;
            border-width: 5px;
            border-color: black;
            color: black;
                                """)

        self.btn6 = QPushButton(self, clicked=lambda: self.btn_click(self.btn6, 6))
        self.btn6.setGeometry(340, 195, 150, 150)
        self.btn6.setFont(QFont("Aptos", 60, weight= 50))
        self.btn6.setStyleSheet("""
            background-color: white;
            border-style: solid;
            border-width: 5px;
            border-color: black;
            color: black;
                                """)
        
        self.btn7 = QPushButton(self, clicked=lambda: self.btn_click(self.btn7, 7))
        self.btn7.setGeometry(50, 340, 150, 150)
        self.btn7.setFont(QFont("Aptos", 60, weight= 50))
        self.btn7.setStyleSheet("""
            background-color: white;
            border-style: solid;
            border-width: 5px;
            border-color: black;
            color: black;
                                """)

        self.btn8 = QPushButton(self, clicked=lambda: self.btn_click(self.btn8, 8))
        self.btn8.setGeometry(195, 340, 150, 150)
        self.btn8.setFont(QFont("Aptos", 60, weight= 50))
        self.btn8.setStyleSheet("""
            background-color: white;
            border-style: solid;
            border-width: 5px;
            border-color: black;
            color: black;
                                """)

        self.btn9 = QPushButton(self, clicked=lambda: self.btn_click(self.btn9, 9))
        self.btn9.setGeometry(340, 340, 150, 150)
        self.btn9.setFont(QFont("Aptos", 60, weight= 50))
        self.btn9.setStyleSheet("""
            background-color: white;
            border-style: solid;
            border-width: 5px;
            border-color: black;
            color: black;
                                """)
        
        self.Button_Method_list = [self.btn1_click, self.btn2_click, self.btn3_click, self.btn4_click, 
                                  self.btn5_click, self.btn6_click, self.btn7_click, self.btn8_click, 
                                  self.btn9_click]

        self.Button_list = [self.btn1, self.btn2, self.btn3, self.btn4, self.btn5, self.btn6, 
                            self.btn7, self.btn8, self.btn9]

    def Winning(self):
        msg = QMessageBox(self)
        msg.setWindowTitle("Winner")
        msg.setWindowIcon(QIcon("C:/Users/user/Desktop/Tic Tac/Winner.ico"))
        msg.setStandardButtons(QMessageBox.Ok)

        if TicTac.__count % 2 != 0:
            tem = "Pleyar 1"
        else:
            tem = "Pleyar 2"
        msg.setText(f"{tem} won")
        self.DisAbleAll()

        msg.show()

    def Give_color(self, btn1, btn2, btn3):
        btn1.setStyleSheet("background: green")
        btn2.setStyleSheet("background: green")
        btn3.setStyleSheet("background: green")

    def btn1_click(self):
        if self.btn1.text() == self.btn2.text() and self.btn2.text() == self.btn3.text():
            self.Give_color(self.btn1, self.btn2, self.btn3)
            self.Winning()
            return False
        elif self.btn1.text() == self.btn4.text() and self.btn4.text() == self.btn7.text():
            self.Give_color(self.btn1, self.btn4, self.btn7)
            self.Winning()
            return False
        elif self.btn1.text() == self.btn5.text() and self.btn5.text() == self.btn9.text():
            self.Give_color(self.btn1, self.btn5, self.btn9)
            self.Winning()
            return False
        return True

    def btn2_click(self):
        if self.btn1.text() == self.btn2.text() and self.btn2.text() == self.btn3.text():
            self.Give_color(self.btn1, self.btn5, self.btn9)
            self.Winning()
            return False
        elif self.btn2.text() == self.btn5.text() and self.btn5.text() == self.btn8.text():
            self.Give_color(self.btn2, self.btn5, self.btn8)
            self.Winning()
            return False
        return True

    def btn3_click(self):
        if self.btn3.text() == self.btn2.text() and self.btn2.text() == self.btn1.text():
            self.Give_color(self.btn1, self.btn2, self.btn3)
            self.Winning()
            return False
        elif self.btn3.text() == self.btn5.text() and self.btn5.text() == self.btn7.text():
            self.Give_color(self.btn3, self.btn5, self.btn7)
            self.Winning()
            return False
        elif self.btn3.text() == self.btn6.text() and self.btn6.text() == self.btn9.text():
            self.Give_color(self.btn3, self.btn6, self.btn9)
            self.Winning()
            return False
        return True

    def btn4_click(self):
        if self.btn1.text() == self.btn4.text() and self.btn4.text() == self.btn7.text():
            self.Give_color(self.btn1, self.btn4, self.btn7)
            self.Winning()
            return False
        elif self.btn4.text() == self.btn5.text() and self.btn5.text() == self.btn6.text():
            self.Give_color(self.btn4, self.btn5, self.btn6)
            self.Winning()
            return False
        return True

    def btn5_click(self):
        if self.btn1.text() == self.btn5.text() and self.btn5.text() == self.btn9.text():
            self.Give_color(self.btn1, self.btn5, self.btn9)
            self.Winning()
            return False
        elif self.btn3.text() == self.btn5.text() and self.btn5.text() == self.btn7.text():
            self.Give_color(self.btn3, self.btn5, self.btn7)
            self.Winning()
            return False
        elif self.btn2.text() == self.btn5.text() and self.btn5.text() == self.btn8.text():
            self.Give_color(self.btn2, self.btn5, self.btn8)
            self.Winning()
            return False
        elif self.btn4.text() == self.btn5.text() and self.btn5.text() == self.btn6.text():
            self.Give_color(self.btn4, self.btn5, self.btn6)
            self.Winning()
            return False
        return True
            
    def btn6_click(self):
        if self.btn3.text() == self.btn6.text() and self.btn6.text() == self.btn9.text():
            self.Give_color(self.btn3, self.btn6, self.btn9)
            self.Winning()
            return False
        elif self.btn4.text() == self.btn5.text() and self.btn5.text() == self.btn6.text():
            self.Give_color(self.btn4, self.btn5, self.btn6)
            self.Winning()
            return False
        return True

    def btn7_click(self):
        if self.btn1.text() == self.btn4.text() and self.btn4.text() == self.btn7.text():
            self.Give_color(self.btn1, self.btn4, self.btn7)
            self.Winning()
            return False
        elif self.btn7.text() == self.btn8.text() and self.btn8.text() == self.btn9.text():
            self.Give_color(self.btn7, self.btn8, self.btn9)
            self.Winning()
            return False
        elif self.btn3.text() == self.btn5.text() and self.btn5.text() == self.btn7.text():
            self.Give_color(self.btn3, self.btn5, self.btn7)
            self.Winning()
            return False
        return True
        
    def btn8_click(self):
        if self.btn2.text() == self.btn5.text() and self.btn5.text() == self.btn8.text():
            self.Give_color(self.btn2, self.btn5, self.btn8)
            self.Winning()
            return False
        elif self.btn7.text() == self.btn8.text() and self.btn8.text() == self.btn9.text():
            self.Give_color(self.btn7, self.btn8, self.btn9)
            self.Winning()
            return False
        return True

    def btn9_click(self):
        if self.btn3.text() == self.btn6.text() and self.btn6.text() == self.btn9.text():
            self.Give_color(self.btn3, self.btn6, self.btn9)
            self.Winning()
            return False
        elif self.btn7.text() == self.btn8.text() and self.btn8.text() == self.btn9.text():
            self.Give_color(self.btn7, self.btn8, self.btn9)
            self.Winning()
            return False
        elif self.btn1.text() == self.btn5.text() and self.btn5.text() == self.btn9.text():
            self.Give_color(self.btn1, self.btn5, self.btn9)
            self.Winning()
            return False
        return True

    def btn_click(self, CurBtn, num):
        self.write(CurBtn)
        if not self.Button_Method_list[num-1]():
            pass
        elif TicTac.__count > 8:
            msg = QMessageBox(self)
            msg.setWindowTitle("Information")
            msg.setWindowIcon(QIcon("C:/Users/user/Desktop/Tic Tac/No.ico"))
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setText("There is no way")

            msg.show()
        
    def write(self, CurBtn):
        if TicTac.__count % 2 != 0:
            CurBtn.setText("O")
            CurBtn.setEnabled(False)
        else:
            CurBtn.setText("X")
            CurBtn.setEnabled(False)
        TicTac.__count += 1

    def Create_Meny(self):
        menu = self.menuBar()
        Manu = menu.addMenu("Menu")

        New_game = QAction("New Game", self)
        New_game.triggered.connect(self.New_Game_click)
        Manu.addAction(New_game)

        Quit = QAction("Quit", self)
        Quit.triggered.connect(self.Exit)
        Manu.addAction(Quit)

    def New_Game_click(self):
        for i in self.Button_list:
            i.setEnabled(True)
            i.setText("")
            i.setStyleSheet("""
                background-color: white;
                border-style: solid;
                border-width: 5px;
                border-color: black;
                color: black;
                                    """)
        
        TicTac.__count = 0
        
    def DisAbleAll(self):
        for i in self.Button_list:
            i.setEnabled(False)

    def Exit(self):
        sys.exit()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    TicTacGame = TicTac()
    TicTacGame.show()
    app.exec_()
