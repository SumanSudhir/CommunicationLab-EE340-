#!/usr/bin/env python

from gnuradio import gr,gru,blks2
from gnuradio.wxgui import stdgui2, fftsink2
from grc_gnuradio import wxgui as grc_wxgui
import numpy
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(
			self,
			title="CPFSK low rate",
		)

		self.samp_rate = samp_rate = 48000

		self.gr_cpfsk_bc_0 = gr.cpfsk_bc(1, 1, 2)
		self.random_source_x_0 = gr.vector_source_b(numpy.random.randint(0, 2, 3), True)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			ref_level=50,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=30,
			average=False,
			avg_alpha=None,
			title="CPFSK low rate FFT",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)

		self.connect((self.gr_cpfsk_bc_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.random_source_x_0, 0), (self.gr_cpfsk_bc_0, 0))

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
	tb = top_block()
	tb.Run()

