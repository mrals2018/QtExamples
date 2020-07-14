# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audiodevicesbase.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from Qt import QtCore, QtGui, QtWidgets


class Ui_AudioDevicesBase(object):
    def setupUi(self, AudioDevicesBase):
        AudioDevicesBase.setObjectName("AudioDevicesBase")
        AudioDevicesBase.resize(679, 598)
        self.centralwidget = QtWidgets.QWidget(AudioDevicesBase)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 659, 558))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.modeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.modeLabel.setObjectName("modeLabel")
        self.gridLayout_2.addWidget(self.modeLabel, 0, 0, 1, 1)
        self.deviceLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.deviceLabel.setObjectName("deviceLabel")
        self.gridLayout_2.addWidget(self.deviceLabel, 0, 1, 1, 1)
        self.modeBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.modeBox.setObjectName("modeBox")
        self.modeBox.addItem("")
        self.modeBox.addItem("")
        self.gridLayout_2.addWidget(self.modeBox, 1, 0, 1, 1)
        self.deviceBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.deviceBox.setObjectName("deviceBox")
        self.gridLayout_2.addWidget(self.deviceBox, 1, 1, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName("tabWidget")
        self.testFormatTab = QtWidgets.QWidget()
        self.testFormatTab.setObjectName("testFormatTab")
        self.gridLayout = QtWidgets.QGridLayout(self.testFormatTab)
        self.gridLayout.setObjectName("gridLayout")
        self.actualLabel = QtWidgets.QLabel(self.testFormatTab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actualLabel.sizePolicy().hasHeightForWidth())
        self.actualLabel.setSizePolicy(sizePolicy)
        self.actualLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.actualLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.actualLabel.setTextFormat(QtCore.Qt.RichText)
        self.actualLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.actualLabel.setObjectName("actualLabel")
        self.gridLayout.addWidget(self.actualLabel, 0, 1, 1, 1)
        self.nearestLabel = QtWidgets.QLabel(self.testFormatTab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nearestLabel.sizePolicy().hasHeightForWidth())
        self.nearestLabel.setSizePolicy(sizePolicy)
        self.nearestLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nearestLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.nearestLabel.setTextFormat(QtCore.Qt.RichText)
        self.nearestLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nearestLabel.setObjectName("nearestLabel")
        self.gridLayout.addWidget(self.nearestLabel, 0, 2, 1, 1)
        self.sampleRateBox = QtWidgets.QComboBox(self.testFormatTab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.sampleRateBox.sizePolicy().hasHeightForWidth()
        )
        self.sampleRateBox.setSizePolicy(sizePolicy)
        self.sampleRateBox.setObjectName("sampleRateBox")
        self.gridLayout.addWidget(self.sampleRateBox, 3, 1, 1, 1)
        self.nearestSampleRate = QtWidgets.QLineEdit(self.testFormatTab)
        self.nearestSampleRate.setEnabled(False)
        self.nearestSampleRate.setObjectName("nearestSampleRate")
        self.gridLayout.addWidget(self.nearestSampleRate, 3, 2, 1, 1)
        self.channelsBox = QtWidgets.QComboBox(self.testFormatTab)
        self.channelsBox.setObjectName("channelsBox")
        self.gridLayout.addWidget(self.channelsBox, 5, 1, 1, 1)
        self.nearestChannel = QtWidgets.QLineEdit(self.testFormatTab)
        self.nearestChannel.setEnabled(False)
        self.nearestChannel.setObjectName("nearestChannel")
        self.gridLayout.addWidget(self.nearestChannel, 5, 2, 1, 1)
        self.sampleSizesBox = QtWidgets.QComboBox(self.testFormatTab)
        self.sampleSizesBox.setObjectName("sampleSizesBox")
        self.gridLayout.addWidget(self.sampleSizesBox, 9, 1, 1, 1)
        self.nearestSampleSize = QtWidgets.QLineEdit(self.testFormatTab)
        self.nearestSampleSize.setEnabled(False)
        self.nearestSampleSize.setObjectName("nearestSampleSize")
        self.gridLayout.addWidget(self.nearestSampleSize, 9, 2, 1, 1)
        self.endianBox = QtWidgets.QComboBox(self.testFormatTab)
        self.endianBox.setObjectName("endianBox")
        self.gridLayout.addWidget(self.endianBox, 14, 1, 1, 1)
        self.nearestEndian = QtWidgets.QLineEdit(self.testFormatTab)
        self.nearestEndian.setEnabled(False)
        self.nearestEndian.setObjectName("nearestEndian")
        self.gridLayout.addWidget(self.nearestEndian, 14, 2, 1, 1)
        self.testButton = QtWidgets.QPushButton(self.testFormatTab)
        self.testButton.setObjectName("testButton")
        self.gridLayout.addWidget(self.testButton, 15, 1, 1, 1)
        self.testResult = QtWidgets.QLabel(self.testFormatTab)
        self.testResult.setText("")
        self.testResult.setObjectName("testResult")
        self.gridLayout.addWidget(self.testResult, 15, 2, 1, 1)
        self.actualFreqLabel = QtWidgets.QLabel(self.testFormatTab)
        self.actualFreqLabel.setObjectName("actualFreqLabel")
        self.gridLayout.addWidget(self.actualFreqLabel, 3, 0, 1, 1)
        self.actualChannelLabel = QtWidgets.QLabel(self.testFormatTab)
        self.actualChannelLabel.setObjectName("actualChannelLabel")
        self.gridLayout.addWidget(self.actualChannelLabel, 5, 0, 1, 1)
        self.actualSampleSizeLabel = QtWidgets.QLabel(self.testFormatTab)
        self.actualSampleSizeLabel.setObjectName("actualSampleSizeLabel")
        self.gridLayout.addWidget(self.actualSampleSizeLabel, 9, 0, 1, 1)
        self.actualEndianLabel = QtWidgets.QLabel(self.testFormatTab)
        self.actualEndianLabel.setObjectName("actualEndianLabel")
        self.gridLayout.addWidget(self.actualEndianLabel, 14, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.testFormatTab)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 16, 0, 1, 3)
        self.actualCodecLabel = QtWidgets.QLabel(self.testFormatTab)
        self.actualCodecLabel.setObjectName("actualCodecLabel")
        self.gridLayout.addWidget(self.actualCodecLabel, 2, 0, 1, 1)
        self.nearestCodec = QtWidgets.QLineEdit(self.testFormatTab)
        self.nearestCodec.setEnabled(False)
        self.nearestCodec.setObjectName("nearestCodec")
        self.gridLayout.addWidget(self.nearestCodec, 2, 2, 1, 1)
        self.codecsBox = QtWidgets.QComboBox(self.testFormatTab)
        self.codecsBox.setObjectName("codecsBox")
        self.gridLayout.addWidget(self.codecsBox, 2, 1, 1, 1)
        self.actualSampleTypeLabel = QtWidgets.QLabel(self.testFormatTab)
        self.actualSampleTypeLabel.setObjectName("actualSampleTypeLabel")
        self.gridLayout.addWidget(self.actualSampleTypeLabel, 6, 0, 1, 1)
        self.sampleTypesBox = QtWidgets.QComboBox(self.testFormatTab)
        self.sampleTypesBox.setObjectName("sampleTypesBox")
        self.gridLayout.addWidget(self.sampleTypesBox, 6, 1, 1, 1)
        self.nearestSampleType = QtWidgets.QLineEdit(self.testFormatTab)
        self.nearestSampleType.setEnabled(False)
        self.nearestSampleType.setObjectName("nearestSampleType")
        self.gridLayout.addWidget(self.nearestSampleType, 6, 2, 1, 1)
        self.tabWidget.addTab(self.testFormatTab, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.populateTableButton = QtWidgets.QPushButton(self.tab)
        self.populateTableButton.setObjectName("populateTableButton")
        self.verticalLayout_2.addWidget(self.populateTableButton)
        self.allFormatsTable = QtWidgets.QTableWidget(self.tab)
        self.allFormatsTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.allFormatsTable.setDragDropOverwriteMode(False)
        self.allFormatsTable.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.allFormatsTable.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectItems
        )
        self.allFormatsTable.setTextElideMode(QtCore.Qt.ElideNone)
        self.allFormatsTable.setWordWrap(False)
        self.allFormatsTable.setCornerButtonEnabled(False)
        self.allFormatsTable.setObjectName("allFormatsTable")
        self.allFormatsTable.setColumnCount(6)
        self.allFormatsTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        self.allFormatsTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        self.allFormatsTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        self.allFormatsTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        self.allFormatsTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        self.allFormatsTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(
            QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter
        )
        self.allFormatsTable.setHorizontalHeaderItem(5, item)
        self.allFormatsTable.horizontalHeader().setHighlightSections(False)
        self.allFormatsTable.verticalHeader().setVisible(False)
        self.allFormatsTable.verticalHeader().setHighlightSections(False)
        self.verticalLayout_2.addWidget(self.allFormatsTable)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 0, 1, 2)
        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        AudioDevicesBase.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AudioDevicesBase)
        self.statusbar.setObjectName("statusbar")
        AudioDevicesBase.setStatusBar(self.statusbar)

        self.retranslateUi(AudioDevicesBase)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AudioDevicesBase)

    def retranslateUi(self, AudioDevicesBase):
        _translate = QtCore.QCoreApplication.translate
        AudioDevicesBase.setWindowTitle(_translate("AudioDevicesBase", "Audio Devices"))
        self.modeLabel.setText(_translate("AudioDevicesBase", "Mode"))
        self.deviceLabel.setText(_translate("AudioDevicesBase", "Device"))
        self.modeBox.setItemText(0, _translate("AudioDevicesBase", "Input"))
        self.modeBox.setItemText(1, _translate("AudioDevicesBase", "Output"))
        self.actualLabel.setText(
            _translate("AudioDevicesBase", "<i>Actual Settings</i>")
        )
        self.nearestLabel.setText(
            _translate(
                "AudioDevicesBase",
                '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">\n'
                '<html><head><meta name="qrichtext" content="1" /><style type="text/css">\n'
                "p, li { white-space: pre-wrap; }\n"
                "</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                '<p style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-style:italic;">Nearest Settings</span></p></body></html>',
            )
        )
        self.testButton.setText(_translate("AudioDevicesBase", "Test"))
        self.actualFreqLabel.setText(_translate("AudioDevicesBase", "Frequency (Hz)"))
        self.actualChannelLabel.setText(_translate("AudioDevicesBase", "Channels"))
        self.actualSampleSizeLabel.setText(
            _translate("AudioDevicesBase", "Sample size (bits)")
        )
        self.actualEndianLabel.setText(_translate("AudioDevicesBase", "Endianness"))
        self.label.setText(
            _translate(
                "AudioDevicesBase",
                "Note: an invalid codec 'audio/test' exists in order to allow an invalid format to be constructed, and therefore to trigger a 'nearest format' calculation.",
            )
        )
        self.actualCodecLabel.setText(_translate("AudioDevicesBase", "Codec"))
        self.actualSampleTypeLabel.setText(_translate("AudioDevicesBase", "SampleType"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.testFormatTab),
            _translate("AudioDevicesBase", "Test format"),
        )
        self.populateTableButton.setText(
            _translate("AudioDevicesBase", "Populate table")
        )
        self.allFormatsTable.setSortingEnabled(False)
        item = self.allFormatsTable.horizontalHeaderItem(0)
        item.setText(_translate("AudioDevicesBase", "Codec"))
        item = self.allFormatsTable.horizontalHeaderItem(1)
        item.setText(_translate("AudioDevicesBase", "Frequency (Hz)"))
        item = self.allFormatsTable.horizontalHeaderItem(2)
        item.setText(_translate("AudioDevicesBase", "Channels"))
        item = self.allFormatsTable.horizontalHeaderItem(3)
        item.setText(_translate("AudioDevicesBase", "Sample type"))
        item = self.allFormatsTable.horizontalHeaderItem(4)
        item.setText(_translate("AudioDevicesBase", "Sample size (bits)"))
        item = self.allFormatsTable.horizontalHeaderItem(5)
        item.setText(_translate("AudioDevicesBase", "Endianness"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            _translate("AudioDevicesBase", "All formats"),
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    AudioDevicesBase = QtWidgets.QMainWindow()
    ui = Ui_AudioDevicesBase()
    ui.setupUi(AudioDevicesBase)
    AudioDevicesBase.show()
    sys.exit(app.exec_())
