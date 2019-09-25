import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
import QtMultimedia 5.12

Rectangle {
    id: inspection
    color: '#F5F5F5'

    Camera {
        id: camera
    }

    VideoOutput {
        id: finder
        source: camera
        width: 320
        height: 180
        x: 60
        y: 60
        focus : visible // to receive focus and capture key events when visible
        }

    OpenCameraList {
        width: 160
        mytext: '表示するカメラを選択'
        anchors.horizontalCenter: finder.horizontalCenter
        y: 310
    }

/*
    Dialog {
        id: whichCamera
        modal: true
        standardButtons: Dialog.Close

        header: Text {
            anchors.horizontalCenter: whichCamera.horizontalCenter
            text: qsTr("カメラの選択")
        }
    }
*/

    Item {
        width: 320
        anchors.horizontalCenter: finder.horizontalCenter
        y: 365

        GeneralButton {
            width: 150
            mytext: '撮影して判定'
            objectName: 'inspect_button'
        }

        GeneralButton {
            x: 170
            width: 150
            mytext: '既存の画像を判定'
            objectName: 'inspect_existing_image_button'
        }
    }

    Rectangle {
        id: result
        width: 350
        height: 260
        y: finder.y
        x: 430
        radius: under_topbar.r

        StackLayout {
            currentIndex: 0
            anchors.fill: parent
            objectName: "result_layout"

            Item {
                Text {
                    id: result_pre1
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: qsTr("ここに判定結果が")
                }
                Text {
                    anchors.top: result_pre1.bottom
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: qsTr("表示されます")
                }
            }

            Item {
                Rectangle {
                    anchors.fill: parent
                    color: 'transparent'
                    border.width: 3
                    border.color: '#3FDA68'
                    radius: under_topbar.r
                }

                Rectangle {
                    anchors.fill: parent
                    color: '#3FDA68'
                    opacity: 0.1
                    radius: under_topbar.r
                }

                Image {
                    y: 20
                    width: 140
                    height: width
                    anchors.horizontalCenter: parent.horizontalCenter
                    source: "../images/sampleimage.png"
                }

                Text {
                    text: qsTr("この製品は良品です")
                    color: '#3FDA68'
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 190
                    font.pointSize: 15
                }

                Text {
                    y: 220
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: qsTr("スコア: 0.0000002328")
                }

                Text {
                    y: 235
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: qsTr("  閾値: 0.0000000322")
                }

            }

            Item {
                Rectangle {
                    anchors.fill: parent
                    color: 'transparent'
                    border.width: 3
                    border.color: '#E66643'
                    radius: under_topbar.r
                }

                Rectangle {
                    anchors.fill: parent
                    color: '#E66643'
                    opacity: 0.1
                    radius: under_topbar.r
                }



                Image {
                    y: 20
                    width: 140
                    height: 140
                    anchors.horizontalCenter: parent.horizontalCenter
                    source: "../images/sampleimage.png"
                }

                Text {
                    text: qsTr("この製品は不良品です")
                    color: '#E66643'
                    anchors.horizontalCenter: parent.horizontalCenter
                    y: 190
                    font.pointSize: 15
                }

                Text {
                    y: 220
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: qsTr("スコア: 0.0000002328")
                }

                Text {
                    y: 235
                    anchors.horizontalCenter: parent.horizontalCenter
                    text: qsTr("  閾値: 0.0000000322")
                }
            }

        }



    }

    Rectangle {
        id: counter
        width: result.width
        height: 70
        anchors.horizontalCenter: result.horizontalCenter
        y: 350
        radius: under_topbar.r

        Item {

            anchors.verticalCenter: parent.verticalCenter

            Text {
                x: 20
                anchors.verticalCenter: parent.verticalCenter
                text: qsTr("累計")
            }

            Image {
                x: 100
                anchors.verticalCenter: parent.verticalCenter
                source: "../fonts/fontawesome/font-awesome_4-7-0_check-circle_32_4_3fda68_none.png"
            }
            Text {
                id: number_of_ok
                x: 150
                anchors.verticalCenter: parent.verticalCenter
                objectName: "ok_counter"
                text: None
            }
            Image {
                id: name
                x: 210
                anchors.verticalCenter: parent.verticalCenter
                source: "../fonts/fontawesome/font-awesome_4-7-0_check-circle_32_4_3fda68_none.png"
            }
            Text {
                id: number_of_failed
                x: 260
                anchors.verticalCenter: parent.verticalCenter
                text: None
                objectName: "ng_counter"
            }
        }


    }



}
