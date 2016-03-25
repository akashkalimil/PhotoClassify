import os
print "Hello, this is the Restaurant Classification Program"
print "You will need to put a file into the classify folder"
print "You will have to enter the file name . It should be example.jpeg format"
ifilename =str( raw_input('Enter a file name: '))


os.system('bazel build tensorflow/examples/label_image:label_image && \ ')
os.system('bazel-bin/tensorflow/examples/label_image/label_image \  ')
os.system('--graph=/workspace/retrained_graph.pb \ ')
os.system('--labels=/workspace/retrained_labels.txt \ ')
os.system('--output_layer=final_result \ ')
os.system('--image=/workspace/classify/' + ifilename)
