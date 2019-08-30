import QtQuick 2.12
import QtQuick.Controls 2.12


Rectangle {
    id: baserect
    signal clicked()
    visible: true
    width: 90
    height: 35
    color: if(validbuttton){'#F5F5F5';}else{'#AAAAAA';}
    radius: 5
    border.color: '#666666'
    property string mytext: 'テキスト'
    property bool validbuttton: true

    MouseArea {
        id: _mouse
        hoverEnabled: true
        anchors.fill: parent
        onClicked: whichCamera.open()
    }

    states: [
        State {
            name: "click"
            when: _mouse.pressed && validbuttton
            PropertyChanges {
                target: baserect
                color:'#4298F9'
            }
            PropertyChanges {
                target: buttontext
                color: '#F5F5F5'
            }
        },

        State {
            name: "hover"
            when: _mouse.containsMouse && validbuttton
            PropertyChanges {
                target: baserect
                // color: '#AAAAAA'
            }
            PropertyChanges {
                target: buttontext
                color: '#AAAAAA'
            }
        }
    ]

    Text {
        id: buttontext
        anchors.centerIn: parent
        text: qsTr(mytext)
        color: if(validbuttton){'#3E3E3E'}else{'#666666'}
    }
}
