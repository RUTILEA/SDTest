
#bash vgg_sample.sh [work_name]
echo examples/sample.py -p ~/sample_$1/dataset -f examples/hist/$1
python examples/sample.py -p ~/sample_$1/dataset -f examples/hist/$1