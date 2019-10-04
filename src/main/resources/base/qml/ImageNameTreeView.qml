import QtQuick 2.12
import QtQuick.Controls 2.12
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4

Item{
    TreeView{
        id: fileTreeView
        anchors.fill: parent
        style: TreeViewStyle {
            id: treeStyle
            backgroundColor: "white"
            alternateBackgroundColor:"white"
            rowDelegate: Rectangle{
                height: 20
                color: styleData.selected ? "#0077bb" : "white"
            }
            highlightedTextColor: "white"
        }
        model: fileSystemModel
        rootIndex: rootPathIndex
        itemDelegate: Rectangle {
            color: styleData.selected ? "#0077bb" : "white"
            Rectangle{
                id: fileImageRec
                anchors.verticalCenter: parent.verticalCenter
                width: 25
                Image {
                    anchors.verticalCenter: parent.verticalCenter
                    source: isFolder(styleData.index) ? "png/dir.png" : "png/doc.png"
                    sourceSize.width: 20
                    sourceSize.height: 20
                }
            }
            Text {
                anchors.verticalCenter: parent.verticalCenter
                anchors.left: fileImageRec.right
                color: styleData.selected ? "white" : "black"
                text: styleData.value
            }
        }

        TableViewColumn {
            title: "名前"
            role: "fileName"
            resizable: true
        }

        onActivated : {
            Qt.openUrlExternally("file://"+fileSystemModel.data(index,Qt.UserRole+1));
        }

    }
}
