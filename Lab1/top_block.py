#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Sat Sep  1 19:41:38 2018
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

from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx


class top_block(grc_wxgui.top_block_gui):

    def __init__(self):
        grc_wxgui.top_block_gui.__init__(self, title="Top Block")
        _icon_path = "/usr/local/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
        self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

        ##################################################
        # Variables
        ##################################################
        self.variable_slider_0_3 = variable_slider_0_3 = 1
        self.variable_slider_0_2 = variable_slider_0_2 = 1
        self.variable_slider_0_1 = variable_slider_0_1 = 1
        self.variable_slider_0_0 = variable_slider_0_0 = 1
        self.variable_slider_0 = variable_slider_0 = 1
        self.samp_rate = samp_rate = 32000

        ##################################################
        # Blocks
        ##################################################
        _variable_slider_0_1_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_0_1_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_1_sizer,
        	value=self.variable_slider_0_1,
        	callback=self.set_variable_slider_0_1,
        	label="band_pass_filter_0",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_0_1_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_1_sizer,
        	value=self.variable_slider_0_1,
        	callback=self.set_variable_slider_0_1,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_0_1_sizer)
        _variable_slider_0_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_0_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_0_sizer,
        	value=self.variable_slider_0_0,
        	callback=self.set_variable_slider_0_0,
        	label="band_pass_filter_0",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_0_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_0_sizer,
        	value=self.variable_slider_0_0,
        	callback=self.set_variable_slider_0_0,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_0_0_sizer)
        _variable_slider_0_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_0_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	label="band_pass_filter_0",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_0_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_sizer,
        	value=self.variable_slider_0,
        	callback=self.set_variable_slider_0,
        	minimum=0,
        	maximum=1,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_0_sizer)
        _variable_slider_0_3_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_0_3_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_3_sizer,
        	value=self.variable_slider_0_3,
        	callback=self.set_variable_slider_0_3,
        	label="band_pass_filter_0_3",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_0_3_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_3_sizer,
        	value=self.variable_slider_0_3,
        	callback=self.set_variable_slider_0_3,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_0_3_sizer)
        _variable_slider_0_2_sizer = wx.BoxSizer(wx.VERTICAL)
        self._variable_slider_0_2_text_box = forms.text_box(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_2_sizer,
        	value=self.variable_slider_0_2,
        	callback=self.set_variable_slider_0_2,
        	label="band_pass_filter_0",
        	converter=forms.float_converter(),
        	proportion=0,
        )
        self._variable_slider_0_2_slider = forms.slider(
        	parent=self.GetWin(),
        	sizer=_variable_slider_0_2_sizer,
        	value=self.variable_slider_0_2,
        	callback=self.set_variable_slider_0_2,
        	minimum=0,
        	maximum=100,
        	num_steps=100,
        	style=wx.SL_HORIZONTAL,
        	cast=float,
        	proportion=1,
        )
        self.Add(_variable_slider_0_2_sizer)
        self.blocks_wavfile_source_0 = blocks.wavfile_source("/home/alok/Desktop/5TH-SEM/EE340/Lab1/Bach.wav", True)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_0_3 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	variable_slider_0, samp_rate, 9000, 15000, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_2 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	variable_slider_0, samp_rate, 6000, 9000, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	variable_slider_0_1, samp_rate, 3000, 6000, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	variable_slider_0_0, samp_rate, 500, 3000, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0 = filter.interp_fir_filter_fff(1, firdes.band_pass(
        	variable_slider_0, samp_rate, 20, 500, 100, firdes.WIN_HAMMING, 6.76))
        self.audio_sink_0 = audio.sink(samp_rate, "", True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.band_pass_filter_0, 0), (self.blocks_add_xx_0, 0))    
        self.connect((self.band_pass_filter_0_0, 0), (self.blocks_add_xx_0, 1))    
        self.connect((self.band_pass_filter_0_1, 0), (self.blocks_add_xx_0, 2))    
        self.connect((self.band_pass_filter_0_2, 0), (self.blocks_add_xx_0, 3))    
        self.connect((self.band_pass_filter_0_3, 0), (self.blocks_add_xx_0, 4))    
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_0, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_1, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_2, 0))    
        self.connect((self.blocks_wavfile_source_0, 0), (self.band_pass_filter_0_3, 0))    

    def get_variable_slider_0_3(self):
        return self.variable_slider_0_3

    def set_variable_slider_0_3(self, variable_slider_0_3):
        self.variable_slider_0_3 = variable_slider_0_3
        self._variable_slider_0_3_slider.set_value(self.variable_slider_0_3)
        self._variable_slider_0_3_text_box.set_value(self.variable_slider_0_3)

    def get_variable_slider_0_2(self):
        return self.variable_slider_0_2

    def set_variable_slider_0_2(self, variable_slider_0_2):
        self.variable_slider_0_2 = variable_slider_0_2
        self._variable_slider_0_2_slider.set_value(self.variable_slider_0_2)
        self._variable_slider_0_2_text_box.set_value(self.variable_slider_0_2)

    def get_variable_slider_0_1(self):
        return self.variable_slider_0_1

    def set_variable_slider_0_1(self, variable_slider_0_1):
        self.variable_slider_0_1 = variable_slider_0_1
        self._variable_slider_0_1_slider.set_value(self.variable_slider_0_1)
        self._variable_slider_0_1_text_box.set_value(self.variable_slider_0_1)
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.variable_slider_0_1, self.samp_rate, 3000, 6000, 100, firdes.WIN_HAMMING, 6.76))

    def get_variable_slider_0_0(self):
        return self.variable_slider_0_0

    def set_variable_slider_0_0(self, variable_slider_0_0):
        self.variable_slider_0_0 = variable_slider_0_0
        self._variable_slider_0_0_slider.set_value(self.variable_slider_0_0)
        self._variable_slider_0_0_text_box.set_value(self.variable_slider_0_0)
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.variable_slider_0_0, self.samp_rate, 500, 3000, 100, firdes.WIN_HAMMING, 6.76))

    def get_variable_slider_0(self):
        return self.variable_slider_0

    def set_variable_slider_0(self, variable_slider_0):
        self.variable_slider_0 = variable_slider_0
        self._variable_slider_0_slider.set_value(self.variable_slider_0)
        self._variable_slider_0_text_box.set_value(self.variable_slider_0)
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.variable_slider_0, self.samp_rate, 20, 500, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(self.variable_slider_0, self.samp_rate, 6000, 9000, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(self.variable_slider_0, self.samp_rate, 9000, 15000, 100, firdes.WIN_HAMMING, 6.76))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.band_pass(self.variable_slider_0, self.samp_rate, 20, 500, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_0.set_taps(firdes.band_pass(self.variable_slider_0_0, self.samp_rate, 500, 3000, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_1.set_taps(firdes.band_pass(self.variable_slider_0_1, self.samp_rate, 3000, 6000, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_2.set_taps(firdes.band_pass(self.variable_slider_0, self.samp_rate, 6000, 9000, 100, firdes.WIN_HAMMING, 6.76))
        self.band_pass_filter_0_3.set_taps(firdes.band_pass(self.variable_slider_0, self.samp_rate, 9000, 15000, 100, firdes.WIN_HAMMING, 6.76))


def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.Start(True)
    tb.Wait()


if __name__ == '__main__':
    main()
