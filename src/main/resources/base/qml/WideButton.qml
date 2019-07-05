import QtQuick 2.12
import QtQuick.Controls 2.12

Rectangle {
    id: baserec
    signal clicked()
    width: 170
    height: 40
    radius: 20
    color: '#3E3E3E'

    MouseArea {
        id: _mouse
        anchors.fill: parent
        width: parent.width
        height: parent.height
        hoverEnabled: true
        onClicked: baserec.clicked()
    }

    states: [
        State {
            name: "pressed"
            when: _mouse.pressed
            PropertyChanges {
                target: baserec
                color: '#4298F9'
            }
        },

        State {
            name: "hover"
            when: _mouse.containsMouse
            PropertyChanges {
                target: baserec
                color: '#666666'
            }
        }
    ]
}



