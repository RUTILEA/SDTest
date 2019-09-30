import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12

ApplicationWindow {
    visible: true
    maximumWidth : 320
    maximumHeight: 200
    minimumWidth: 320
    minimumHeight: 200
    color: "#f5f5f5"
    title: "Sample"

    Text {
        text: "sample"
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        font.pointSize: 32
    }

    Row {
        anchors.horizontalCenter: parent.horizontalCenter
        y:parent.height * 0.8
        spacing: 40

        GeneralButton {
            id: startbutton
            objectName: 'start_button'
            mytext: 'start'
        }
    }
}
