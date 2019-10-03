import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.13

Rectangle {
    color: '#F5F5F5'
    Rectangle {
        y: 20
        height: 480
        width: 720
        anchors.horizontalCenter: parent.horizontalCenter
        color: 'white'


        ListModel {
            id: resultModel

            ListElement {
                name: "nut"
                date: "2019/8/23"
            }
            ListElement {
                name: "circuit_board"
                date: "2018/4/11"
            }
            ListElement {
                name: "nut_ver2"
                date: "2018/9/22"
            }
        }



        ListView {
            id: list
            width: parent.width
            height: parent.height - title.height - 20
            anchors.top: title.bottom
            anchors.horizontalCenter: parent.horizontalCenter
            model: resultModel
            highlight: Rectangle {
                color: '#4298F9'
                radius: 5
                opacity: 0.2

            }
            focus: true

            // ScrollBar.vertical: ScrollBar {}

            delegate:
                Item {
                width: parent.width
                height: 30

                // color: index % 2 == 0 ? "#ffffff" : "#f5f5f5"

                Text {
                    anchors.verticalCenter: parent.verticalCenter
                    x: 5
                    text: name
                }
                Text {
                    anchors.verticalCenter: parent.verticalCenter
                    x: 365
                    text: date
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: list.currentIndex = index
                }
            }

        }

        Rectangle {
            y: 0
            id: title
            width: list.width
            height: 45
            anchors.horizontalCenter: parent.horizontalCenter
            color: '#f5f5f5'

            border.color: '#3E3E3E'
            border.width: 0.75

            Text {
                anchors.verticalCenter: parent.verticalCenter
                x: 5
                text: qsTr("ファイル名")
            }

            Text {
                anchors.verticalCenter: parent.verticalCenter
                x: 365
                text: qsTr("日付")
            }


        }

        Rectangle{
            width: 360
            height: parent.height
            color: 'transparent'
            border.color: '#3E3E3E'
            border.width: 0.75
        }

        Rectangle{
            anchors.fill: parent
            color: 'transparent'
            border.color: '#3E3E3E'
            border.width: 1.5
        }





    }





}

