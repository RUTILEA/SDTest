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
        id: topbar
        width: parent.width
        height: 55
        color: '#F5F5F5'
        property int currentTab: 0

        Row {
            TopbarButton {
                tabname: '検品'
                mynumber: 0
                imgsource: '../fonts/fontawesome/eye_3e3e3e.png'
                imgsource_selected: '../fonts/fontawesome/blueeye.png'
            }

            TopbarButton {
                tabname: '学習'
                mynumber: 1
                imgsource: '../fonts/fontawesome/eye_3e3e3e.png'
                imgsource_selected: '../fonts/fontawesome/blueeye.png'
            }

        }
    }

    StackLayout {
        width: parent.width
        height: parent.height - topbar.height
        anchors.top: topbar.bottom
        currentIndex: topbar.currentTab

        InspectionView {

        }

        AiOptimizationView {

        }
    }




}
