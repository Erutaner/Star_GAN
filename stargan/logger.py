import tensorflow as tf


# class Logger(object):
#     """Tensorboard logger."""
#
#     def __init__(self, log_dir):
#         """Initialize summary writer."""
#         # self.writer = tf.summary.FileWriter(log_dir)
#         self.writer = tf.summary.create_file_writer(log_dir)
#
#     def scalar_summary(self, tag, value, step):
#         """Add scalar summary."""
#         summary = tf.Summary(value=[tf.Summary.Value(tag=tag, simple_value=value)])
#         self.writer.add_summary(summary, step)

class Logger(object):
    """Tensorboard logger."""

    def __init__(self, log_dir):
        """Initialize summary writer."""
        self.writer = tf.summary.create_file_writer(log_dir)

    def scalar_summary(self, tag, value, step):
        """Add scalar summary."""
        with self.writer.as_default():
            tf.summary.scalar(name=tag, data=value, step=step)
            self.writer.flush()
