import os, sys
import nltk
import codecs
import csv
import ui_freakuent_mainwindow
from PyQt4 import QtCore, QtGui

class Freakuent(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)

        self.ui = ui_freakuent_mainwindow.Ui_FreakuentMain()
        self.ui.setupUi(self)
        
#        Create button connections
        QtCore.QObject.connect(self.ui.inputDocumentBrowser, QtCore.SIGNAL("clicked()"), self.set_input_file)
        QtCore.QObject.connect(self.ui.outputDocumentBrowser, QtCore.SIGNAL("clicked()"), self.set_output_path)
        QtCore.QObject.connect(self.ui.processButton, QtCore.SIGNAL("clicked()"), self.document_process)
        
#    Select file for processing, only text files allowed
    def set_input_file(self):
        inputFileDialog = QtGui.QFileDialog(self)
        self.inputFilePath = inputFileDialog.getOpenFileName(self, "Select Input File", "/", "Text files (*.txt)")
        self.ui.inputPathEdit.setText(self.inputFilePath)
        
#    Select directory for output file
    def set_output_path(self):
        outputFileDialog = QtGui.QFileDialog(self)
        self.outputFilePath = outputFileDialog.getExistingDirectory(self, "Select Directory for Output File", "/")
        self.ui.outputPathEdit.setText(self.outputFilePath)

#    Write out table into csv file
    def write_csv(self, text, output):
        tokens = nltk.word_tokenize(text)
        fdist = nltk.FreqDist(tokens)
        csvwriter = csv.writer(output, dialect = 'excel')
        for i in fdist.items():
            csvwriter.writerow(i)
        output.close()
        
    def document_process(self):
        try:
            text = codecs.open(self.ui.inputPathEdit.text(), 'r', encoding = 'utf-8').read()
        except IOError:
            QtGui.QMessageBox.about(self, "Error", "Input File Not Found")
            return
        self.outputFile = os.path.join(str(self.outputFilePath), 
                                       str(self.ui.outputFileEdit.text()))
        if os.path.isfile(self.outputFile):
            reply = QtGui.QMessageBox.question(self, "Attention", 
                                               "This action will overwrite existing file!\nAre you sure you want to continue?", 
                                               QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
            if reply == QtGui.QMessageBox.No:
                return
        else:
            newOutputFile = codecs.open(self.outputFile, 'w', encoding = 'utf-8')
            if self.ui.lowerCheck.isChecked():
                self.write_csv(text.lower(), newOutputFile)
            else:
                self.write_csv(text, newOutputFile)
        QtGui.QMessageBox.about(self, "Ready", "File Processing Has Been Complete")

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Freakuent()
    window.show()
    sys.exit(app.exec_())