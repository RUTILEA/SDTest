import QtQuick 2.12
import QtQuick.Controls 2.12

Rectangle{
    id: baserec
    width: 50
    height: topbar.height
    visible: true
    radius: 3
    color: topbar.color

    signal clicked()
    property string tabname: 'tabname'
    property int mynumber: 0
    property string imgsource: ''
    property string imgsource_selected: ''
    function setCurrentNumber (n){
        topbar.currentTab = n;
    }

    MouseArea {
        id: _mouse
        anchors.fill:parent
        hoverEnabled: true
        onClicked: {
            baserec.clicked();
            setCurrentNumber(mynumber);
        }
    }

    Image {
        id: topbarIcon
        width: 32
        height: 32
        anchors.horizontalCenter: parent.horizontalCenter
        source: imgsource
    }

    Text {
        id: topbarText
        anchors.horizontalCenter: topbarIcon.horizontalCenter
        anchors.top: topbarIcon.bottom
        text: qsTr(tabname)
        font.pointSize: 10
        color: '#3E3E3E'
    }

    states: [
        State {
            name: 'click'
            when: _mouse.pressed
            PropertyChanges {
                target: baserec
                color: '#4298F9'
            }
        },
        State {
            name: "hover_selected"
            when: _mouse.containsMouse && (topbar.currentTab === baserec.mynumber)
            PropertyChanges {
                target: topbarText
                opacity: 0.7
                font.bold: true
                color: '#4298F9'
            }
            PropertyChanges {
                target: topbarIcon
                source: imgsource_selected
                opacity: 0.7

            }
        },

        State {
            name: "hover"
            when: _mouse.containsMouse && (topbar.currentTab !== baserec.mynumber)
            PropertyChanges {
                target: topbarText
                // color: '#666666'
                opacity: 0.7

            }
            PropertyChanges {
                target: topbarIcon
                opacity: 0.7

            }
        },

        State {
            name: "selected"
            when:  !(_mouse.containsMouse) && (topbar.currentTab === baserec.mynumber)
            PropertyChanges {
                target: topbarIcon
                source: imgsource_selected
            }
            PropertyChanges {
                target: topbarText
                font.bold: true
                color: '#4298F9'
            }
        }
    ]
}
