import QtQuick 2.12

Rectangle {
    id: tab
    width: 230
    height: parent.height
    color: '#FFFFFF'
    radius: 5
    signal clicked()
    property int mynumber: 0
    property string mytext: ''

    MouseArea {
        id: _mouse
        anchors.fill: parent
        hoverEnabled: true
        onClicked: {
            tab.clicked();
            middleTabBase.currentMiddleTab = tab.mynumber;
        }
    }

    Text {
        id: tabtext
        color: '#3E3E3E'
        anchors.centerIn: parent
        text: qsTr(mytext)
    }

     states: [
         State {
             name: "name"
             when: middleTabBase.currentMiddleTab === mynumber
             PropertyChanges {
                 target: tab
                 color: '#4298F9'
             }
             PropertyChanges {
                 target: tabtext
                 color: '#F5F5F5'
             }
         },

         State {
             name: "hover"
             when: _mouse.containsMouse
             PropertyChanges {
                 target: tab
                 color: '#F5F5F5'

             }
         }
     ]
}
