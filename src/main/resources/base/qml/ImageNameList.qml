import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.13

Item {

    ListModel {
        id: resultModel

        ListElement {
            name: "camera_0_2019-06-19T17-47-04.419843.jpg"
        }
        ListElement {
            name: "camera_0_2019-06-19T17-47-04.419343.jpg"
        }
        ListElement {
            name: "camera_0_2019-06-19T17-47-04.419841.jpg"
        }
    }

    ListView {
        id: list
        width: parent.width
        height: parent.height
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
}
