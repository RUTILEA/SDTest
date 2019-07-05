import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12

ApplicationWindow {
    visible: true
    maximumWidth: 795
    maximumHeight: 512
    minimumWidth: 795
    minimumHeight: 512
    title: 'プロジェクト名'

    Rectangle {
        width: parent.width
        height: 60
        color: '#F5F5F5'
        Column {
            Item {
                width: 50
                height: parent.height
                Image {
                    anchors.horizontalCenter: parent.horizontalCenter
                    id: eye_logo
                    source: "../../../resources/base/fonts/fontawesome/eye_3e3e3e.png"
                }

                Text {
                    anchors.horizontalCenter: eye_logo.horizontalCenter
                    anchors.top: eye_logo.bottom
                    text: qsTr("検品")
                    font.pointSize: 10
                }
            }
        }
    }
}
