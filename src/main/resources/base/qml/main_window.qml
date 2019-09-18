import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import QtMultimedia 5.12
import Qt.labs.platform 1.1


ApplicationWindow {
    id: root
    visible: true
    // 795, 512
    property int fixedWidth: {
        if (topbar.currentTab===0)
            return 842
        else if (topbar.currentTab===1)
            return 864
        else
            return 864
    }

    property int fixedHeight: {
        if (topbar.currentTab===0)
            return 532 + 40
        else if (topbar.currentTab===1)
            return 730 + 40
        else
            return 730 + 40
    }
    width: fixedWidth
    height: fixedHeight
    maximumWidth: fixedWidth
    maximumHeight: fixedHeight
    minimumWidth: fixedWidth
    minimumHeight: fixedHeight
/*
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
*/
    MenuBar{
        id: menuBar

        Menu {
            id: fileMenu
            title: qsTr("ファイル")

            MenuItem {
                text: qsTr("新規プロジェクト")
                objectName: 'newprojectaction'
                // onTriggered:
            }

            MenuItem {
                text: qsTr("開く")
                objectName: 'openaction'
                // onTriggered:
                }

            MenuSeparator { }

            MenuItem {
                text: qsTr("閉じる")
                objectName: 'closeaction'
                // onTriggered:
            }
        }

        Menu {
            id: helpMenu
            title: qsTr("ヘルプ")

            MenuItem {
                text: qsTr("SDTestホームページ")
                objectName: 'websiteaction'
                // onTriggered:
            }

            MenuItem {
                text: qsTr("アップデートを確認")
                objectName: 'versionaction'
                // onTriggered:
            }
        }
    }


    title: 'プロジェクト名'

    Rectangle {
        id: topbar
        width: root.width
        height: 50
        color: '#AAAAAA'
        property int currentTab: 0
        objectName: 'topbar'

        Row {
            TopbarButton {
                tabname: '検品'
                mynumber: 0
                objectName: 'inspectionbutton'
                imgsource: '../fonts/fontawesome/eye_3e3e3e.png'
                imgsource_selected: '../fonts/fontawesome/blueeye.png'
            }

            TopbarButton {
                tabname: '学習'
                mynumber: 1
                objectName: 'optimizationbutton'
                imgsource: '../fonts/fontawesome/eye_3e3e3e.png'
                imgsource_selected: '../fonts/fontawesome/blueeye.png'
            }

            TopbarButton {
                tabname: 'レポート'
                mynumber: 2
                objectName: 'pastresultbutton'
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

        PastResultView {}
    }
}
