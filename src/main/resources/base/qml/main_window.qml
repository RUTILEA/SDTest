import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
// import QtMultimedia 5.12

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
        id: under_topbar
        width: parent.width
        height: parent.height - topbar.height
        anchors.top: topbar.bottom
        currentIndex: topbar.currentTab

        property int r: 8

        Rectangle {
            color: 'black'
        }

        Rectangle {
            color: '#F5F5F5'

            StackLayout {
                id: under_middletab
                anchors.horizontalCenter: parent.horizontalCenter
                // y: middletabbase.y + middletabbase.height * 0.5
                width: parent.width * 0.96
                height: under_topbar.height - (middleTabBase.y + middleTabBase.height * 0.5 + parent.width * 0.02)
                // anchors.bottom: under_topbar.bottom - 10
                anchors.verticalCenter: under_topbar.verticalCenter
                currentIndex: middleTabBase.currentMiddleTab

                Rectangle {
                    id: middleTabLeft_Content
                    color: '#EEEEEE'
                    radius: under_topbar.r

                    Rectangle {
                        id: selector
                        color: selectorbackground
                        width: under_topbar.width * 0.25
                        height: under_topbar.height * 0.8
                        x: under_topbar.width * 0.02
                        y: under_topbar.width * 0.02
                        radius: under_topbar.r
                        property string selectorbackground: '#DDDDDD'
                        property int columnheight: 30
                        property int indent: 30
                        property int currentColumnTab: 0

                        ColumnLayout {
                            SelectorButton {
                                id: headline1
                                Layout.preferredHeight: selector.columnheight * 1.3
                                iconSource: '../fonts/fontawesome/dumbbell_666666.png'
                                mytext: 'トレーニング用画像'
                                canPress: false
                                radius: under_topbar.r
                            }

                            SelectorButton {
                                iconSource: '../fonts/fontawesome/dumbbell_666666.png'
                                mytext: '良品'
                                mynumber: 0
                            }

                            SelectorButton {
                                id: headline2
                                Layout.preferredHeight: selector.columnheight * 1.3
                                iconSource: '../fonts/fontawesome/dumbbell_666666.png'
                                mytext: '性能評価用画像'
                                canPress: false
                            }

                            SelectorButton {
                                iconSource: '../fonts/fontawesome/dumbbell_666666.png'
                                mytext: '良品'
                                mynumber: 1
                            }

                            SelectorButton {
                                iconSource: '../fonts/fontawesome/dumbbell_666666.png'
                                mytext: '不良品'
                                mynumber: 2
                            }
                        }
                    }

                    Rectangle {
                        id: imageviewer
                        radius: under_topbar.r
                        width: middleTabLeft_Content.width - selector.width - under_topbar.width * 0.06
                        height: under_topbar.height * 0.8
                        color: selector.selectorbackground
                        anchors.verticalCenter: selector.verticalCenter
                        x: selector.x + selector.width + under_topbar.width * 0.02

                        ScrollView {
                            width: parent.width * 0.95
                            height: parent.height * 0.8
                            anchors.horizontalCenter: parent.horizontalCenter
                            y: under_topbar.width * 0.02

                        }

                        GeneralButton {
                            mytext: '削除'
                            x: under_topbar.width * 0.02
                            y: parent.y + parent.height - under_topbar.width * 0.04 - 35
                        }
                    }

                }

                Rectangle {
                   color: 'red'
                }


            }

            Rectangle {
                id: middleTabBase
                anchors.verticalCenter: under_middletab.top
                width: middleTabLeft.width + middleTabRight.width
                height: 20
                color: 'white'
                radius: 5
                anchors.horizontalCenter: parent.horizontalCenter
                property int currentMiddleTab: 0

                MiddleTabButton {
                    id: middleTabLeft
                    mytext: 'データセットの管理とトレーニング'
                    width: 230
                    mynumber: 0
                }

                MiddleTabButton {
                    id: middleTabRight
                    width: 65
                    mynumber: 1
                    mytext: '性能評価'
                    anchors.left: middleTabLeft.right

                }
            }
        }
    }
}
