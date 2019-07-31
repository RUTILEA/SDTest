import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Layouts 1.12
// import QtMultimedia 5.12

ApplicationWindow {
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
            return 532
        else
            return 730
    }
    width: fixedWidth
    height: fixedHeight
    maximumWidth: fixedWidth
    maximumHeight: fixedHeight
    minimumWidth: fixedWidth
    minimumHeight: fixedHeight

    title: 'プロジェクト名'

    Rectangle {
        id: topbar
        width: parent.width
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
        width: parent.width
        height: parent.height - topbar.height
        anchors.top: topbar.bottom
        currentIndex: topbar.currentTab

        property int r: 8

        Rectangle {
            color: 'black'
        }

        Rectangle {
            color: 'white'

            StackLayout {
                id: under_middletab
                anchors.horizontalCenter: parent.horizontalCenter
                y: 30
                width: parent.width * 0.96
                height: under_topbar.height - (middleTabBase.y + middleTabBase.height * 0.5 + parent.width * 0.02)

                anchors.verticalCenter: under_topbar.verticalCenter
                currentIndex: middleTabBase.currentMiddleTab

                Rectangle {
                    id: middleTabLeft_Content

                    color: '#EEEEEE'
                    radius: under_topbar.r

                    property int allPic: 100
                    property int selectedPic: 3

                    Rectangle {
                        id: selector
                        color: selectorbackground
                        width: under_topbar.width * 0.25
                        height: under_topbar.height * 0.8
                        x: under_topbar.width * 0.02
                        y: under_topbar.width * 0.04
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

                        Rectangle {
                            id: insideImageViewer
                            width: parent.width * 0.95
                            height: parent.height - under_topbar.width * 0.06 - 35
                            anchors.horizontalCenter: parent.horizontalCenter
                            y: under_topbar.width * 0.02
                            color: '#F5F5F5'
                            radius: under_topbar.r

                            StackLayout {
                                currentIndex: selector.currentColumnTab

                                Text {
                                    text: qsTr("text_1")
                                }

                                Text {
                                    text: qsTr("text_2")
                                }

                                Text {
                                    text: qsTr("text_3s")
                                }

                            }
                        }

                        GeneralButton {
                            id: deleteButton
                            mytext: '削除'
                            x: under_topbar.width * 0.02
                            y: parent.y + parent.height - under_topbar.width * 0.06 - 35
                        }

                        GeneralButton {
                            mytext: '追加'
                            anchors.verticalCenter: deleteButton.verticalCenter
                            anchors.right: insideImageViewer.right
                        }

                        Text {
                            text: qsTr(middleTabLeft_Content.allPic+ '枚 - ' + middleTabLeft_Content.selectedPic + '枚選択中' )
                            color: '#666666'
                            anchors.horizontalCenter: imageviewer.horizontalCenter
                            anchors.verticalCenter: deleteButton.verticalCenter
                        }

                    }

                    Item {
                        anchors.top: imageviewer.bottom
                        anchors.bottom: middleTabLeft_Content.bottom
                        anchors.left: selector.left
                        anchors.right: imageviewer.right

                        Item {
                            id: name
                            visible: false

                            Image {
                                source: "../fonts/fontawesome/blueeye.png"
                            }

                            Text {
                                text: qsTr("トレーニング用画像に変更があります")
                                color: '#FFA00E'
                            }
                        }

                        Text {
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.right: startTrainingButton.left
                            rightPadding: 15
                            text: qsTr("前回のトレーニング：X月Y日")
                            color: '#666666'
                        }

                        WideButton {
                            id: startTrainingButton
                            anchors.verticalCenter: parent.verticalCenter
                            anchors.right: parent.right

                            Row {
                                anchors.centerIn: parent
                                spacing: 2

                                Image {
                                    id: plus_icon
                                    source: "../fonts/fontawesome/font-awesome_4-7-0_plus_32_4_f5f5f5_none.png"
                                    width: startTrainingButton.height * 0.5
                                    height: startTrainingButton.height * 0.5
                                }

                                Text {
                                    text: qsTr("トレーニング")
                                    color: '#F5F5F5'
                                    anchors.verticalCenter: parent.verticalCenter
                                }
                            }
                        }
                    }
                }

                Rectangle {
                   color: '#EEEEEE'
                   radius: under_topbar.r
                }
            }

            Rectangle {
                id: middleTabBase
                anchors.verticalCenter: under_middletab.top
                width: middleTabLeft.width + middleTabRight.width
                height: 30
                color: 'white'
                radius: 5
                anchors.horizontalCenter: parent.horizontalCenter
                property int currentMiddleTab: 0

                Rectangle {
                    id: middleTabBaseBorder
                    anchors.centerIn: parent
                    width: middleTabLeft.width + middleTabRight.width + 2
                    height: parent.height + 2
                    radius: 5
                    color: '#00000000'
                    border.color: '#AAAAAA'
                    border.width: 1
                }

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
