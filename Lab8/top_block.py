#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Thu Oct  4 16:53:32 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from gnuradio import digital
from gnuradio import digital 
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import wxgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from math import pi
from optparse import OptionParser
import osmosdr
import time
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.samp_rate = samp_rate = 1.6e6
        self.fShift = fShift = 0

        ##################################################
        # Blocks
        ##################################################
        self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_c(
        	self.GetWin(),
        	title="Scope Plot",
        	sample_rate=400e3,
        	v_scale=0,
        	v_offset=0,
        	t_scale=0,
        	ac_couple=False,
        	xy_mode=False,
        	num_inputs=1,
        	trig_mode=wxgui.TRIG_MODE_AUTO,
        	y_axis_label="Counts",
        )
        self.Add(self.wxgui_scopesink2_0_0.win)
        self.rtlsdr_source_1 = osmosdr.source( args="numchan=" + str(1) + " " + "" )
        self.rtlsdr_source_1.set_sample_rate(samp_rate)
        self.rtlsdr_source_1.set_center_freq(1.2e9, 0)
        self.rtlsdr_source_1.set_freq_corr(0, 0)
        self.rtlsdr_source_1.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_1.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_1.set_gain_mode(False, 0)
        self.rtlsdr_source_1.set_gain(70, 0)
        self.rtlsdr_source_1.set_if_gain(20, 0)
        self.rtlsdr_source_1.set_bb_gain(20, 0)
        self.rtlsdr_source_1.set_antenna("", 0)
        self.rtlsdr_source_1.set_bandwidth(0, 0)
          
        _fShift_sizer = wx.BoxSizer(wx.VERTICAL)
        self._fShift_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_fShift_sizer,
        	value=self.fShift,
        	callback=self.set_fShift,
        	label='fShift',
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._fShift_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_fShift_sizer,
        	value=self.fShift,
        	callback=self.set_fShift,
        	minimum=-10e6,
        	maximum=10e6,
        	num_steps=200,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_fShift_sizer)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(4, 2*pi/100, (filter.firdes.root_raised_cosine(32, 32*sps, 1.0, 0.4, 1408)), 32, 16, 1.5, 1)
        self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(4, 0.4, 55, 2*pi/100)
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(2*pi/100, 8, False)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(10, 1, 0.0001, 1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_costas_loop_cc_0, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.wxgui_scopesink2_0_0, 0))    
        self.connect((self.digital_fll_band_edge_cc_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))    
        self.connect((self.rtlsdr_source_1, 0), (self.digital_fll_band_edge_cc_0, 0))    

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.digital_pfb_clock_sync_xxx_0.update_taps((filter.firdes.root_raised_cosine(32, 32*self.sps, 1.0, 0.4, 1408)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rtlsdr_source_1.set_sample_rate(self.samp_rate)

    def get_fShift(self):
        return self.fShift

    def set_fShift(self, fShift):
        self.fShift = fShift
        self._fShift_slider.set_value(self.fShift)
        self._fShift_text_box.set_value(self.fShift)


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
