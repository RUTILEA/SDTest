import QtQuick 2.12
import QtQuick.Controls 2.12

ApplicationWindow{
    visible: true

    width: 800
    height: 400

    Rectangle {
        width: 720
        height: 30

        property string iconSource: ''
        property string mytext: ''
        property int mynumber: 5
        property bool canPress: true
        signal clicked()

        MouseArea {
                id: _mouse
                visible: baserec.canPress
                anchors.fill: parent
                hoverEnabled: true
                onClicked: {
                    baserec.clicked();
                    selector.currentColumnTab = mynumber;
                }
        }


        states: [
            State {
                name: "selected"
                when: baserec.mynumber === selector.currentColumnTab
                PropertyChanges {
                    target: baserec
                    color: '#4298F9'
                }
                PropertyChanges {
                    target: text
                    color: '#F5F5F5'
                }
            },

            State {
                name: "hover"
                when: _mouse.containsMouse
                PropertyChanges {
                    target: baserec
                    color: '#AAAAAA'

                }
            }
        ]


    }

}

