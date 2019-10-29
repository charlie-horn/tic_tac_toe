import tensorflow as tf

class Network():
    def __init__(self, num_inputs, num_hidden, learning_rate):
        # Values
        self.num_inputs = num_inputs
        self.num_hidden = num_hidden
        self.learning_rate = learning_rate

        #TF components
        self.initializer = tf.contrib.layers.variance_scaling_initializer()
        self.input_layer = tf.placeholder(tf.float32, shape=(None, 27))
        self.hidden_layer_1 = tf.layers.dense(self.input_layer,self.num_hidden,activation=tf.nn.relu,kernel_initializer=self.initializer)
        self.hidden_layer_2 = tf.layers.dense(self.hidden_layer_1,self.num_hidden,activation=tf.nn.relu,kernel_initializer=self.initializer)
        self.hidden_layer_3 = tf.layers.dense(self.hidden_layer_2,self.num_hidden,activation=tf.nn.relu,kernel_initializer=self.initializer)
        self.hidden_layer_4 = tf.layers.dense(self.hidden_layer_3,self.num_hidden,activation=tf.nn.relu,kernel_initializer=self.initializer)
        self.output_layer = tf.layers.dense(self.hidden_layer_4,9,activation=tf.nn.sigmoid,kernel_initializer=self.initializer)
        #self.input_q_values = tf.placeholder(tf.float32, shape=(None,9), name='inputs')
        self.target_q_values = tf.placeholder(tf.float32, shape=(None,9))
        mse = tf.losses.mean_squared_error(predictions=self.output_layer, labels=self.target_q_values)
        self.minimize_loss = tf.train.GradientDescentOptimizer(learning_rate=self.learning_rate).minimize(mse)

    def getOutput(self, input, session):
        return session.run(self.output_layer, feed_dict={self.input_layer:input})

    