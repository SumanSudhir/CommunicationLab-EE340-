#!/usr/bin/env python

from gnuradio import gr, gru, blks2
from gnuradio import eng_notation
from gnuradio.eng_option import eng_option
from gnuradio.wxgui import stdgui2, fftsink2, waterfallsink2, scopesink2, form, slider
from optparse import OptionParser
import wx
import numpy
import sys

_def_samples_per_symbol = 2
_def_excess_bw = 0.35
_def_gray_code = True
_def_verbose = False
_def_log = False

_def_costas_alpha = 0.15
_def_gain_mu = None
_def_mu = 0.5
_def_omega_relative_limit = 0.005

class my_qpsk(stdgui2.std_top_block):
    def __init__(self, frame, panel, vbox, argv):
        stdgui2.std_top_block.__init__(self, frame, panel, vbox, argv)

        self.frame = frame
        self.panel = panel

        parser = OptionParser(option_class=eng_option)
        parser.add_option("", "--excess-bw", type="float", default=_def_excess_bw,
                          help="set RRC excess bandwith factor [default=%default] (PSK)")
        parser.add_option("", "--no-gray-code", dest="gray_code",
                          action="store_false", default=_def_gray_code,
                          help="disable gray coding on modulated bits (PSK)")
        parser.add_option("", "--costas-alpha", type="float", default=_def_costas_alpha,
                          help="set Costas loop alpha value [default=%default] (PSK)")
        parser.add_option("", "--gain-mu", type="float", default=_def_gain_mu,
                          help="set M&M symbol sync loop gain mu value [default=%default] (PSK)")
        parser.add_option("", "--mu", type="float", default=_def_mu,
                          help="set M&M symbol sync loop mu value [default=%default] (PSK)")
        (options, args) = parser.parse_args()   

	random_source_x_0 = gr.vector_source_b(numpy.random.randint(0, 2, 1000), True)

	my_fft = fftsink2.fft_sink_c(
			panel,
			baseband_freq=0,
			y_per_div=10,
			ref_level=50,
			sample_rate=32000,
			fft_size=1024,
			fft_rate=30,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
        vbox.Add(my_fft.win, 1, wx.EXPAND)


	dqpsk_mod = blks2.dqpsk_mod(
			samples_per_symbol=2,
			excess_bw=0.35,
			gray_code=True,
		)



	self.connect(random_source_x_0, dqpsk_mod)

	self.connect(dqpsk_mod, my_fft)


if __name__ == '__main__':
        app = stdgui2.stdapp(my_qpsk, "QPSK high rate")
        app.MainLoop()
