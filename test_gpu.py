import tensorflow as tf
import time

with tf.Session():
    start_time = time.time()

    input1 = tf.constant([1, 1, 1, 1] * 100 * 100 * 100)
    input2 = tf.constant([2, 2, 2, 2] * 100 * 100 * 100)
    output = tf.add(input1, input2)
    result = output.eval()

    duration = time.time() - start_time
    print("TIME:", duration)

    print("result: ", result)