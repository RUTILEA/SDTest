import QtQuick 2.12
import QtQuick.Controls 2.12

import QtQuick 2.12
// import TableModel 0.1

TableView {
    id: table_view
    columnSpacing: 1
    rowSpacing: 1
    // clip: true

    model: imageModel

    delegate:imagefileview_delegate

    property bool is_selected: true


    Component{
        id: imagefileview_delegate
        Item {
            implicitWidth: parent.width
            implicitHeight: 25
            // color: index % 2 == 0 ? "#ffffff" : "#f5f5f5"

            MouseArea {
                anchors.fill: parent

                onDoubleClicked: {
                    // aiOptimize.image_filename = image_filename
                    // aiOptimize.imagesource = imagesource
                    image_dialog.open()
                }
                onClicked: {
                    // list.currentIndex = index;
                    aiOptimize.image_filename = image_filename
                    aiOptimize.imagesource = imagesource
                    // check_box.change_state(check_box.checkState)
                }
            }

            CheckBox{
                id: check_box

                function change_state(currentState){
                    if (currentState === Qt.Checked) {
                        checked = Qt.Unchecked;
                        console.log("unchecked")

                    }
                    else  {
                        checked = Qt.Checked
                        console.log("checked")
                    }
                }

                x: 5
                anchors.verticalCenter: parent.verticalCenter
                indicator.width: 15
                indicator.height: 15


            }

            Image {
                source: imagesource
                anchors.verticalCenter: parent.verticalCenter
                x: 40
                width: 20
                height: 15
            }

            Text {
                anchors.verticalCenter: parent.verticalCenter
                x: 70
                text: image_filename
            }


        }
    }

    ListModel {
            id: imageModel

            ListElement {
                image_filename: "camera_0_2019-06-19T17-46-52.730279.jpg"
                imagesource: "../images/modeldata_sample/camera_0_2019-06-19T17-46-52.730279.jpg"
            }
            ListElement {
                image_filename: "camera_0_2019-06-19T17-46-52.732224.jpg"
                imagesource: "../images/modeldata_sample/camera_0_2019-06-19T17-46-52.732224.jpg"
            }
            ListElement {
                image_filename: "camera_0_2019-06-19T17-46-52.733900.jpg"
                imagesource: "../images/modeldata_sample/camera_0_2019-06-19T17-46-52.733900.jpg"
            }
        }
}
