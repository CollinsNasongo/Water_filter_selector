from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtGui import QIntValidator,QDoubleValidator

import sys
import time
import sqlite3
from sqlite3 import Error

def connect():
    conn = None
    try:
        conn = sqlite3.connect("assets/Water Filter.db")
        print("Connected")
    except Error as e:
        print(e)
    return conn

class NotEmpty(QtGui.QValidator):
    pass

class Window(QDialog):
    def __init__(self):

        
        super(Window, self).__init__()
        self.setWindowTitle("Water treatment")
        self.setFixedSize(800, 700)


        
        self.label = QLabel("Water Filter Selector", self)
        self.label.setGeometry(QtCore.QRect(300, 10, 200, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)

        self.label_3 = QLabel("Biological contaminants (check bacteriological analysis)", self)
        self.label_3.setGeometry(QtCore.QRect(40, 345, 400, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QLabel("Organic contaminants (Check organic analysis)",self)
        self.label_4.setGeometry(QtCore.QRect(40, 375, 400, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QLabel("Chemical Characteristics",self)
        self.label_5.setGeometry(QtCore.QRect(40, 260, 175, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.label_6 = QLabel("Quantity",self)
        self.label_6.setGeometry(QtCore.QRect(420, 230, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QLabel("Input your turbidity and total dissolved solids levels as indicated on water report",self)
        self.label_7.setGeometry(QtCore.QRect(110, 40, 551, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QLabel("Turbidity (NTU)",self)
        self.label_8.setGeometry(QtCore.QRect(160, 70, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.label_9 = QLabel("Total Dissolved Solids (mg/L, ppm)",self)
        self.label_9.setGeometry(QtCore.QRect(160, 120, 251, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.label_10 = QLabel("Select and input the values recorded as high in the Chemical analysis section of the water test result",self)
        self.label_10.setGeometry(QtCore.QRect(35, 200, 700, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")

        self.label_11 = QLabel("mg/L",self)
        self.label_11.setGeometry(QtCore.QRect(550, 260, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.label_12 = QLabel("",self)
        self.label_12.setGeometry(QtCore.QRect(620, 375, 180, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")

        self.label_13 = QLabel("",self)
        self.label_13.setGeometry(QtCore.QRect(620, 345, 180, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")

        self.label_14 = QLabel("What is your water source",self)
        self.label_14.setGeometry(QtCore.QRect(40, 310, 200, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")


        self.label_15 = QLabel("Sytem",self)
        self.label_15.setGeometry(QtCore.QRect(40, 540, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")

        self.label_16 = QLabel("",self)
        self.label_16.setGeometry(QtCore.QRect(100, 540, 700, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_16.setWordWrap(True)

        self.label_17 = QLabel("Price",self)
        self.label_17.setGeometry(QtCore.QRect(40, 640, 50, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")

        self.label_18 = QLabel("",self)
        self.label_18.setGeometry(QtCore.QRect(100, 640, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")

        self.label_19 = QLabel("",self)
        self.label_19.setGeometry(QtCore.QRect(100, 640, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")




        self.Chemical = QLineEdit(self)
        self.Chemical.setGeometry(QtCore.QRect(420, 260, 113, 20))
        self.Chemical.setObjectName("Chemical")
        

        self.turbidity = QLineEdit(self)
        self.turbidity.setGeometry(QtCore.QRect(450, 70, 113, 20))
        self.turbidity.setObjectName("turbidity")

        self.TDS = QLineEdit(self)
        self.TDS.setGeometry(QtCore.QRect(450, 120, 113, 20))
        self.TDS.setObjectName("TDS")




        self.rb1 = QRadioButton('present', self)
        self.rb1.setGeometry(QtCore.QRect(450, 345, 180, 22))
        self.rb1.setObjectName("rb1")

        self.rb2 = QRadioButton('not present', self)
        self.rb2.setGeometry(QtCore.QRect(520, 345, 180, 22))
        self.rb2.setObjectName("rb2")

        self.rb3 = QRadioButton('present', self)
        self.rb3.setGeometry(QtCore.QRect(450, 375, 180, 22))
        self.rb3.setObjectName("rb3")

        self.rb4 = QRadioButton('not present', self)
        self.rb4.setGeometry(QtCore.QRect(520, 375, 180, 22))
        self.rb4.setObjectName("rb4")

        self.btngroup1 = QButtonGroup()
        self.btngroup2 = QButtonGroup()

        self.btngroup1.addButton(self.rb1)
        self.btngroup1.addButton(self.rb2)
        self.btngroup2.addButton(self.rb3)
        self.btngroup2.addButton(self.rb4)

        self.rb1.toggled.connect(self.onClicked2)
        self.rb2.toggled.connect(self.onClicked2)

        self.rb3.toggled.connect(self.onClicked)
        self.rb4.toggled.connect(self.onClicked)


        

        self.cbx1 = QCheckBox('Municipal tap water', self)
        self.cbx1.setGeometry(QtCore.QRect(230, 310, 180, 22))
        self.cbx1.setObjectName("cbx1")

        self.cbx2 = QCheckBox('Rain water', self)
        self.cbx2.setGeometry(QtCore.QRect(360, 310, 180, 22))
        self.cbx2.setObjectName("cbx2")

        self.cbx3 = QCheckBox('Bore hole water', self)
        self.cbx3.setGeometry(QtCore.QRect(470, 310, 180, 22))
        self.cbx3.setObjectName("cbx3")

        self.cbx4 = QCheckBox('Supplied by Vendor', self)
        self.cbx4.setGeometry(QtCore.QRect(590, 310, 180, 22))
        self.cbx4.setObjectName("cbx4")


        
        
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(250, 260, 150, 22))
        self.comboBox.setObjectName("comboBox_4")
        self.comboBox.addItems(["Hardness(CaCO3)","Hardness(MgCO3)", "Aluminum (Al)", "Chloride (Cl)", "Copper (Cu)", "Iron (Fe)", "Manganese (Mn)",  "Sodium (Na)", "Sulfate (SO4)", "Zinc (Zn)", "Magnesium (Mg)", "Chlorine concentration", "Calcium (Ca)", "Ammonia (N)", "Fluoride (F)", "Arsenic (As)", "Cadmium (Cd)", "Lead (Pb)", "Mercury (total Hg)", "Selenium (Se)", "Chromium (Cr)", "Cyanide (CN)", "Phenolic Substances", "Barium (Ba)", "Nitrate (NO3)"])




        self.Input = QPushButton("Input",self)
        self.Input.setGeometry(QtCore.QRect(300, 150, 50, 25))
        self.Input.setObjectName("Input")
        self.Input.clicked.connect(self.getInput)
        

        self.add = QPushButton("Add",self)
        self.add.setGeometry(QtCore.QRect(600, 260, 50, 23))
        self.add.setObjectName("add")
        self.add.clicked.connect(self.onAdd)

        self.Design = QPushButton("Design System",self)
        self.Design.setGeometry(QtCore.QRect(300, 420, 100, 25))
        self.Design.setObjectName("Design")
        self.Design.clicked.connect(self.design)

        self.Clr = QPushButton("Reset",self)
        self.Clr.setGeometry(QtCore.QRect(300, 450, 100, 25))
        self.Clr.setObjectName("Clr")
        self.Clr.clicked.connect(self.delete_rows)



        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(QtCore.QRect(670, 265,130, 10))

        self.pbar2 = QProgressBar(self)
        self.pbar2.setGeometry(QtCore.QRect(400, 155,130, 10))

        self.pbar3 = QProgressBar(self)
        self.pbar3.setGeometry(QtCore.QRect(420, 425,130, 10))



    def onClicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label_12.setText("Contaminants " + radioBtn.text())
            
            
    def onClicked2(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label_13.setText("Contaminants " + radioBtn.text())

    def delete_rows(self):
        for i in range(101):
            time.sleep(0.01)
            self.pbar3.setValue(i)
        self.pbar3.reset()
        
        conn = sqlite3.connect("assets/Water Filter.db")
        c = conn.cursor()
        
        c.execute("DELETE  FROM cont_list")
        conn.commit()
        conn.close()
        self.turbidity.clear()
        self.TDS.clear()
        self.label_16.clear()
        self.label_18.clear()
            

    def getInput(self):

        TDS = self.TDS.text()
        turbidity = self.turbidity.text() 
        
        if TDS == "":
            TDS = "0"
        else:
            pass


        if turbidity == "":
            turbidity = "0"
        else:
            pass
          
        TDS = int(TDS)
        turbidity = int(turbidity)

        
        conn = sqlite3.connect("assets/Water Filter.db")
        cur1 = conn.cursor()
        c = conn.cursor()
        
        
        cur1.execute("SELECT * FROM physical_analysis WHERE serial = ?", ("P3",))
        output = cur1.fetchone()
        value1 = output[2]

        c.execute("SELECT * FROM physical_analysis WHERE serial = ?", ("P7",))
        output2 = c.fetchone()
        value2 = output2[2]

        if TDS > value1:
            try:
                conn = sqlite3.connect("assets/Water Filter.db")
                curl = conn.cursor()
                filt_meth = "RO filter"
                curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",("Total Disolved Solids",filt_meth))
                conn.commit()
                conn.close()
                        
            except:
                conn.close()
                
        if turbidity > value2:
            if turbidity > 1 and turbidity <=5:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "1 micron melt blown filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",("Turbidity",filt_meth))
                    conn.commit()
                    conn.close()
                        
                except:
                    conn.close()
                    
            elif turbidity > 5 and turbidity <=100:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "10 micron string wound filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",("Turbidity",filt_meth))
                    conn.commit()
                    conn.close()
                        
                except:
                    conn.close()

            elif turbidity > 100:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "50 micron spin down filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",("Turbidity",filt_meth))
                    conn.commit()
                        
                except:
                    conn.close()

        else:
            conn.close()
            pass
        for i in range(101):
            time.sleep(0.01)
            self.pbar2.setValue(i)
        self.pbar2.reset()
        
        


    def onAdd(self):
        chem = self.comboBox.currentText()
        val = self.Chemical.text()
        if val == "":
            val = "0"
        else:
            pass
        
        val = int(val)
        conn = sqlite3.connect("assets/Water Filter.db")
        cur1 = conn.cursor()
        
        if chem == "Hardness(CaCO3)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C1",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "Cation exchange filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                    conn.commit()
                    conn.close()
                except:
                    conn.close()
            else:
                conn.close()
                pass
        
        if chem == "Hardness(MgCO3)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C25",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "Cation exchange filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                    conn.commit()
                    conn.close()
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Aluminum (Al)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C2",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 1:
                        filt_meth = "Cation exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val>1 :
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass
            

        if chem == "Chloride (Cl)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C3",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 500:
                        filt_meth = "Anion exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val>500 :
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Copper (Cu)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C4",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 5:
                        filt_meth = "Cation exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val>5 :
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass


        if chem == "Iron (Fe)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C5",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "Iron/sulphur filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                    conn.commit()
                    conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass
            
        if chem == "Manganese (Mn)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C6",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "Iron/sulphur filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                    conn.commit()
                    conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass
        if chem == "Sodium (Na)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C7",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "RO filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                    conn.commit()
                    conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Sulfate (SO4)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C8",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 500:
                        filt_meth = "Anion exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val> 500 :
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Zinc (Zn)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C9",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 10:
                        filt_meth = "Cation exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val> 10 :
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass
        if chem == "Magnesium (Mg)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C10",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 200:
                        filt_meth = "Cation exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val> 200 :
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Chlorine concentration":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C11",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "Granular activated carbon filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                    conn.commit()
                    conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        

        if chem == "Calcium (Ca)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C12",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 200:
                        filt_meth = "Cation exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val> 200 :
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Ammonia (N)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C13",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "Anion exchange filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                    conn.commit()
                    conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Fluoride (F)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C14",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 3:
                        filt_meth = "Anion exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val> 3 :
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass
        if chem == "Arsenic (As)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C15",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "KDF - 55 filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                    conn.commit()
                    conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Cadmium (Cd)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C16",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "KDF - 55 filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                    conn.commit()
                    conn.close()
                        
                except:
                    curl.execute("SELECT * FROM cont_list")
                    output = curl.fetchall()
                    print(output)
                    conn.close()
            else:
                conn.close()
                pass

        

        if chem == "Lead (Pb)" :
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C17",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "KDF - 55 filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                    conn.commit()
                    conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass
            
        if chem == "Mercury (total Hg)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C18",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    filt_meth = "KDF - 55 filter"
                    curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                    conn.commit()
                    conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Selenium (Se)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C19",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 0.05:
                        filt_meth = "Anion exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val> 0.05:
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Chromium (Cr)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C20",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 0.1:
                        filt_meth = "Cation exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val> 0.1:
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Cyanide (CN)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C21",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 0.05:
                        filt_meth = "Anion exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val> 0.05:
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

            

        if chem == "Barium (Ba)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C23",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 5:
                        filt_meth = "Cation exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val> 5:
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass
        if chem == "Nitrate (NO3)":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C24",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 5:
                        filt_meth = "Cation exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val> 5:
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass

        if chem == "Phenolic Substances":
            cur1.execute("SELECT * FROM chemical_analysis WHERE serial = ?", ("C22",))
            output = cur1.fetchone()
            value = output[2]
            if val > value:
                try:
                    conn = sqlite3.connect("assets/Water Filter.db")
                    curl = conn.cursor()
                    if val <= 0.01:
                        filt_meth = "Cation exchange filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                    elif val> 0.01:
                        filt_meth = "RO filter"
                        curl.execute("INSERT INTO cont_list  (contaminant,filt_meth) VALUES (?,?)",(chem,filt_meth))
                        conn.commit()
                        conn.close()
                        
                except:
                    conn.close()
            else:
                conn.close()
                pass
        for i in range(101):
            time.sleep(0.01)
            self.pbar.setValue(i)


        self.Chemical.clear()
        self.pbar.reset()
        

    def design(self):

        for i in range(101):
            time.sleep(0.01)
            self.pbar3.setValue(i)
        self.pbar3.reset()
        
        conn = sqlite3.connect("assets/Water Filter.db")
        curl = conn.cursor()

        curl.execute("SELECT filt_meth FROM cont_list")
        output = curl.fetchall()
        filt_list = []
        main_list = []
        for i in output:
            filt_list.append(i[0])

        if "50 micron spin down filter" in filt_list:
            filt_list.extend(["1 micron melt blown filter","10 micron string wound filter"])
        else:
            pass

            
        if "10 micron string wound filter" in filt_list:
            filt_list.append("1 micron melt blown filter")
        else:
            pass
            

        if (self.cbx1.isChecked()== True):
            filt_list.append("Granular activated carbon filter")
        else:
            pass

        if (self.cbx2.isChecked()== True):
            filt_list.extend(["10 micron string wound filter","UV filter"])
        else:
            pass

        if (self.cbx3.isChecked()== True):
            filt_list.extend(["RO filter","UV filter"])
        else:
            pass

        if (self.cbx4.isChecked()== True):
            filt_list.extend(["RO filter", "UV filter"])
        else:
            pass


        if self.rb1.isChecked():
            filt_list.append("UV filter")
        else:
            pass

        if self.rb3.isChecked():
            filt_list.append("Granular activated carbon filter")
        else:
            pass
        

        if "UV filter" in filt_list:
            filt_list.append("1 micron melt blown filter")
        else:
            pass
        

        if "RO filter" in filt_list:
            filt_list.extend(["1 micron melt blown filter","Carbon block filter","Mineralization filter"])

            if "Cation exchange filter" in filt_list:
                filt_list.remove("Cation exchange filter")
            elif "Anion exchange filter" in filt_list:
                filt_list.remove("Anion exchange filter")


    

        for x in filt_list:
            if x not in main_list:
                main_list.append(x)

        if "Cation exchange filter" in main_list:
            if "Anion exchange filter" in main_list:
                main_list.remove("Cation exchange filter")
                main_list.remove("Anion exchange filter")
                main_list.append("Mixed bed IX filter")
            else:
                pass
        else:
            pass
        

        if "Carbon block filter" in main_list:
            if "Granular activated carbon filter" in main_list:
                main_list.remove("Granular activated carbon filter")
            else:
                pass
        else:
            pass


        c = conn.cursor()
        c.execute("SELECT * FROM Filters")
        fil_output = c.fetchall()
        
        priority_list = []
        final_list = []
        price_list = [] 
        
        for y in fil_output:
            priority_list.append(y[0])


        for a in priority_list:
            if a in main_list:
                final_list.append(a)
            else:
                continue
        for e in final_list:
            q = conn.cursor()
            q.execute ("SELECT price FROM Filters WHERE filter=?",(e,))
            price_out = q.fetchall()
            for r in price_out:
                price_list.append(r[0])
                
        print(final_list)

        text = ' => '.join(map(str,final_list))
        self.label_16.setText(text)

            
        print("")
        print(price_list)

        total_price = 0
        for i in price_list:
            total_price += i
        total_price = str(total_price)
        self.label_18.setText("KSH "+ total_price)

    
def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
    
