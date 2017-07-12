# given a XML file, extract fields and reduce to text file for BCP import
import os
import tensorflow as tf

def create_tf_record_file(xml_directory, record_split='warehouseTransaction'):
	compression_type = tf.python_io.TFRecordOptions(tf.python_io.TFRecordCompressionType.GZIP)
	writer = tf.python_io.TFRecordWriter(path=xml_directory+'records.tfrecords',options=compression_type)
	in_record = False
	for file in files:
		with open(in_directory_path+file, 'r') as file_reference:

			record=''
			for line in file_reference:
				if in_record:
					record=record+line
				if '<'+record_split+'>' in line:
					in_record = True
				if '</'+record_split+'>' in line:
					in_record = False
					try:
						writer.write(record.encode())
					except:
						print('Could not process' + record)
					record = ''
		print(file + ' completed.')

# get file list, remove target in source list
in_directory_path = "path here"
files = os.listdir(in_directory_path)

print(files)
create_tf_record_file(in_directory_path)

# filename_queue = tf.train.string_input_producer(files)

# reader = tf.TextLineReader()
# key, value = reader.read(filename_queue)
# for v in value:
# 	print(v)
