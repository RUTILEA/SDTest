# Readme

柿ピーの検品を例に手順を説明します。

## カメラで検品
1. testimages/kakipiにデータセットが格納されています。
2. $ sample_optimization.py -c -tr
3. testimages/kakipi/train/OKtrim2などにトリミング画像が保存され、学習が実行されます。重みデータはlearned_weight/に保存されます。性能評価が自動的に実行され、終了し次第ヒストグラムが表示されます。
4. $ sample_inspection.py -c -jl <重み> -t <閾値> -cam
5. 's'または'start'で検品を開始します。
6. カメラが起動します。'c'キーを押すと撮影され、検品が始まります。検品が終了すると結果が表示されます。
7. 's'または'start'で次の検品、'e'または'exit'で検品終了

## 既存の画像を検品
1. testimages/kakipiにデータセットが格納されています。
2. $ sample_optimization.py -c -tr
3. testimages/kakipi/train/OKtrim2などにトリミング画像が保存され、学習が実行されます。重みデータはlearned_weight/に保存されます。性能評価が自動的に実行され、終了し次第ヒストグラムが表示されます。
4. $ sample_inspection.py -c -jl <重み> -t <閾値>
5. 's'または'start'で検品を開始します。
6. image path: の後に検品したい画像ファイルのパスを指定します。確定すると検品がはじまり、終了すると結果が表示されます。
7. 's'または'start'で次の検品、'e'または'exit'で検品終了

## 補足
- sample_optimization.pyの主なオプションについて
	- -tr ：トリミングを実施します
	- -c ：トリミング範囲の中心を画像の中心に合わせます
	- -ap tuple ：トリミング範囲の左上点を座標指定します
	- -ts tuple ：トリミング範囲の大きさを(w, h)で指定します。
- sample_inspection.pyの主なオプションについて
	- -tr ：トリミングを実施します
	- -c ：トリミング範囲の中心を画像の中心に合わせます
	- -ap tuple ：トリミング範囲の左上点を座標指定します
	- -ts tuple ：トリミング範囲の大きさを(w, h)で指定します。
	- -t float ：スレッショルド値を指定します。デフォルトは-0.5です。
	- -jl str ：.joblibファイルのパスを指定します
	- -cam ：カメラでの検品を実施します
	- -p str ：既存の画像を検品する時の画像パスを指定します。ただしここで指定すると、whileループでの検品時にその画像の検品しか行えません。
	- -f ：test/OKフォルダ内の画像が自動的に検品に用いられます。
- vggからMobileNetに変更するときにすること
	- 双方のスクリプト実施時に、-n MobileNetを追加指定
- 既知の問題
	- カメラでの検品時、撮影後カメラ画面が閉じない
	- -n MobileNetを指定すると ModuleNotFoundError: No module named 'keras.applications.mobile_net'のエラーが出る



