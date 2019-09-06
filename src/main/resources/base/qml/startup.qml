import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.12

ApplicationWindow {
    visible: true
    maximumWidth : 520
    maximumHeight: 404
    minimumWidth: 520
    minimumHeight: 404
    color: "#f5f5f5"
    title: "SDTest"

    Image {
        id: logo
        anchors.horizontalCenter: parent.horizontalCenter
        y: 100
        // もとは200, 47
        width: 250
        height: 59
        // source: "../images/SDTest_logo.png"
        source: '../images/newLogo.png'
    }

    Text {
        anchors.horizontalCenter: parent.horizontalCenter
        y: 160
        text: qsTr("Software-Defined Test")
        color: '#3E3E3E'
        font.pointSize: 15
    }

    Text {
        anchors.horizontalCenter: parent.horizontalCenter
        y: 200
        text: qsTr("Version 0.5")
        color: '#AAAAAA'
        font.pointSize: 15
    }

    Row {
        anchors.horizontalCenter: parent.horizontalCenter
        y:parent.height * 0.8
        spacing: 40

        WideButton {
            id: newprojectbutton
            objectName: 'newprojectbutton'

            Row {
                anchors.centerIn: parent
                spacing: 2

                Image {
                    id: plus_icon
                    source: "../fonts/fontawesome/font-awesome_4-7-0_plus_32_4_f5f5f5_none.png"
                    width: newprojectbutton.height * 0.5
                    height: newprojectbutton.height * 0.5
                }

                Text {
                    text: qsTr("新規プロジェクト")
                    color: '#F5F5F5'
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
        }

        WideButton {
            id: openbutton
            objectName: 'openbutton'

            Row {
                anchors.centerIn: parent
                spacing: 2

                Image {
                    id: open_icon
                    source: "../fonts/fontawesome/font-awesome_4-7-0_file_32_4_f5f5f5_none.png"
                    width: openbutton.height * 0.5
                    height: openbutton.height * 0.5
                }

                Text {
                    text: qsTr("開く")
                    color: '#F5F5F5'
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
        }
    }
}
