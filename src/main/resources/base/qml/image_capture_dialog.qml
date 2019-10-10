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

        Camera{
            id: camera
        }

    VideoOutput {
        id: finder
        x: 28
        y: 23
        source: camera
        width: 424
        height: 218
        anchors.horizontalCenter: roundborder.horizontalCenter
    }

    GeneralButton {
        x: 200
        y: 287
        height: 20
        width: 80
        mytext: '撮影'
        objectName: 'hoge'
    }

    GeneralButton {
        x: 190
        y: 254
        height: 20
        width: 100
        mytext: 'カメラを変更'
        objectName: 'hoge'
    }
}
