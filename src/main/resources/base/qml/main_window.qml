import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import QtMultimedia 5.12

ApplicationWindow {
    id: root
    visible: true
    // 795, 512
    property int fixedWidth: {
        if (topbar.currentTab===0)
            return 842
        else
            return 864
    }

    property int fixedHeight: {
        if (topbar.currentTab===0)
            return 532 + 40
        else
            return 730 + 40
    }
    width: fixedWidth
    height: fixedHeight
    maximumWidth: fixedWidth
    maximumHeight: fixedHeight
    minimumWidth: fixedWidth
    minimumHeight: fixedHeight

    menuBar: MenuBar {
            Menu {
                title: qsTr("&File")
                Action { text: qsTr("&New...") }
                Action { text: qsTr("&Open...") }
                Action { text: qsTr("&Save") }
                Action { text: qsTr("Save &As...") }
                MenuSeparator { }
                Action { text: qsTr("&Quit") }
            }
            Menu {
                title: qsTr("&Edit")
                Action { text: qsTr("Cu&t") }
                Action { text: qsTr("&Copy") }
                Action { text: qsTr("&Paste") }
            }
            Menu {
                title: qsTr("&Help")
                Action { text: qsTr("&About") }
            }
        }

    title: 'プロジェクト名'

    Rectangle {
        id: topbar
        width: root.width
        height: 50
        color: '#AAAAAA'
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
        id: under_topbar
        width: root.width
        height: root.height - topbar.height
        anchors.top: topbar.bottom
        currentIndex: topbar.currentTab

        property int r: 8

        InspectionView {}

        AiOptimizationView {}

    }
}
