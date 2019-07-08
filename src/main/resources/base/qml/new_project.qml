git import QtQuick 2.12
import QtQuick.Controls 2.12

ApplicationWindow {
    id: root
    visible: true
    maximumWidth: 653
    maximumHeight: 296
    minimumWidth: 653
    minimumHeight: 296
    title: '新規プロジェクトの作成'
    color: '#F5F5F5'

    property real space_01: 40
    property real space_02: 12

    Item {
        x: space_01

        Text {
            y: 50
            id: projectname
            text: qsTr("プロジェクト名")
            color: '#3E3E3E'
            font.bold: true
        }

        TextField {
            id: projectnamefield
            objectName: projectnamefield
            width: root.width - space_01 * 2
            height: ref.height
            anchors.left: projectname.left
            anchors.top: projectname.bottom
            placeholderText: '入力してください'
        }

        Text {
            y: 125
            id: save_to
            anchors.left: projectname.left
            text: qsTr("保存先")
            color: '#3E3E3E'
            font.bold: true
        }


        TextField {
            id: pathfield
            objectName: pathfield
            width: root.width - space_01 * 2 - ref.width - space_02
            height: ref.height
            anchors.top: save_to.bottom
            anchors.left: projectname.left
            placeholderText: '＜デフォルトでユーザーフォルダが出るように設定が必要＞'
        }

        GeneralButton {
            id: ref
            objectName: ref
            anchors.verticalCenter: pathfield.verticalCenter
            anchors.right: projectnamefield.right
            mytext: '参照'
        }
    }

    GeneralButton {
        id: cancel
        objectName: cancel
        x: nextbutton.x - cancel.width - space_02
        y: 225
        mytext: 'キャンセル'
    }

    GeneralButton {
        id: nextbutton
        objectName: nextbutton
        anchors.verticalCenter: cancel.verticalCenter
        x: root.width - nextbutton.width - space_01
        // 'projectnamefield'に入力があれば下をtrueに変更する必要あり
        validbuttton: if(projectnamefield.text.length > 0){true;}else{false;}
        mytext: '次へ'
    }
}
