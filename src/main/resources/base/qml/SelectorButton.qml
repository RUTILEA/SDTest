import QtQuick 2.12
import QtQuick.Layouts 1.12

Rectangle {
    id: baserec
    Layout.preferredWidth: selector.width
    Layout.preferredHeight: selector.columnheight
    color: selector.selectorbackground

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


    Image {
        id: icon
        anchors.verticalCenter: parent.verticalCenter
        height: parent.height
        width: parent.height
        x: if(canPress){selector.indent}else{selector.indent * 0.15}
        source: iconSource
    }

    Text {
        id: text
        anchors.left: icon.right
        anchors.verticalCenter: parent.verticalCenter
        text: mytext
        color: if(canPress){'#3E3E3E'}else{'#666666'}
        font.pointSize: 15
        font.bold: true

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
