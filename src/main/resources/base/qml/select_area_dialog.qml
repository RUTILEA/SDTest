import QtQuick 2.12
import QtQuick.Controls 2.12
import QtMultimedia 5.12

ApplicationWindow {
    visible: true

    property real fixedWidth: 435
    property real fixedHeight: 283
    width: 480
    height: 320

    maximumWidth: fixedWidth
    maximumHeight: fixedHeight
    minimumWidth: fixedWidth
    minimumHeight: fixedHeight

    title: 'カメラで撮影'

    Image {
        id: finder
        x: 28
        y: 23
        width: 424
        height: 230
        anchors.horizontalCenter: roundborder.horizontalCenter
        objectName: 'original_image_view'
    }

    GeneralButton {
        x: 317
        y: 277
        height: 20
        width: 140
        mytext: "トレーニング開始"
        objectName: 'ok_button'
    }

    GeneralButton {
        x: 196
        y: 277
        height: 20
        width: 100
        mytext: "キャンセル"
        objectName: 'cancel_button'
    }
    Text {
        id: label
        x: 28
        y: 259
        width: 146
        height: 38
        text: None
        font.pixelSize: 12
        objectName: 'notation_label'
    }
}
