import os.path
import tempfile
from errbot import BotPlugin, arg_botcmd
import numpy as np
import matplotlib.pyplot as plt

class Plotter(BotPlugin):
    """Plugin for consuming data and generating plots to post in response."""
    @arg_botcmd('data')
    @arg_botcmd('-x', '--xaxis')
    @arg_botcmd('-y', '--yaxis')
    @arg_botcmd('-t', '--title')
    def plot(self, mess, data, xaxis=None, yaxis=None, title=None):
        try:
            rows = data.split(';')
            n_cols = len(rows[0].split(','))
            arr = np.zeros((0, n_cols))
            for ii in data.split(';'):
                arr = np.vstack((arr, np.array([float(jj) for jj in ii.split(',')])))
            myplot = plt.figure()
            for ii in range(1, arr.shape[0]):
                plt.plot(arr[0, :], arr[ii, :], 'r')

            if xaxis:
                plt.xlabel(xaxis)
            if yaxis:
                plt.ylabel(yaxis)
            if title:
                plt.title(title)

            with tempfile.NamedTemporaryFile(suffix="png") as file:
                plt.savefig(file.name)

                self.send_stream_request(mess.frm, file, name="image.png", stream_type='image/png')
        except ValueError:
            return "Cannot parse the data provided. Please try again."
