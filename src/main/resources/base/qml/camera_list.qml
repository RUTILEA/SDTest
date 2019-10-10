import QtQuick 2.12
import QtQuick.Controls 2.12
import QtMultimedia 5.12

ApplicationWindow {
    visible: true

    property real fixedWidth: 435
    property real fixedHeight: 283

    width: fixedWidth
    height: fixedHeight
    maximumWidth: fixedWidth
    maximumHeight: fixedHeight
    minimumWidth: fixedWidth
    minimumHeight: fixedHeight

    Component {
            id: cameraDelegate
            Rectangle{
                property int checkbox_state: Qt.Unchecked
                id: roundborder
                width: 270
                height: 180
                radius: 8
                border.color: '#3E3E3E'
                border.width: 1
                anchors.verticalCenter: parent.verticalCenter

                Camera{
                    id: camera
                }

                VideoOutput {
                    id: finder
                    source: camera
                    width: 210
                    height: 140
                    anchors.horizontalCenter: roundborder.horizontalCenter

                }

                CheckBox{
                    id: check_box
                    anchors.horizontalCenter: roundborder.horizontalCenter
                    anchors.top: finder.bottom
                    text: modelData.displayName
                }
            }
    }

    ListView{
        id: camera_list
        width: 360
        height: 240
        delegate: cameraDelegate       
        model: QtMultimedia.availableCameras
        orientation: ListView.Horizontal
    }
}
