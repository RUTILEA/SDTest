import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12

ApplicationWindow {
    visible: true
    maximumWidth : 240
    maximumHeight: 160
    minimumWidth: 240
    minimumHeight: 160
    color: "#f5f5f5"
    title: "Sample"

    Text {
        text: "button clicked"
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        font.pointSize: 20
    }
}
