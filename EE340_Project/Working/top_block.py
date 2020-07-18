#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Tue Nov 27 17:32:16 2018
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

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import sip
import sys
import time
import tutorial


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.sps = sps = 4
        self.nfilts = nfilts = 32
        self.timing_loop_bw = timing_loop_bw = 15.0/100.0
        self.taps = taps = [1.0, 0.25-0.25j, 0.50 + 0.10j, -0.3 + 0.2j]
        self.samp_rate = samp_rate = 250e3
        self.rrc_taps = rrc_taps = firdes.root_raised_cosine(nfilts, nfilts, 1.0/float(sps), 0.35, 11*sps*nfilts)
        self.phase_bw = phase_bw = 6.0/100.0
        self.frequency = frequency = 2.45e9
        self.excess_bw = excess_bw = 0.35
        self.eq_gain = eq_gain = 10.0e-3
        self.code1 = code1 = '010110011011101100010101011111101001001110001011010001101010001'
        self.arity = arity = 4

        ##################################################
        # Blocks
        ##################################################
        self._timing_loop_bw_range = Range(0.0, 0.2, 0.01, 15.0/100.0, 200)
        self._timing_loop_bw_win = RangeWidget(self._timing_loop_bw_range, self.set_timing_loop_bw, "Time: BW", "slider", float)
        self.top_layout.addWidget(self._timing_loop_bw_win)
        self.qtgui_tab_widget_1 = Qt.QTabWidget()
        self.qtgui_tab_widget_1_widget_0 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_0 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_0)
        self.qtgui_tab_widget_1_grid_layout_0 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_0.addLayout(self.qtgui_tab_widget_1_grid_layout_0)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_0, "channel")
        self.qtgui_tab_widget_1_widget_1 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_1 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_1)
        self.qtgui_tab_widget_1_grid_layout_1 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_1.addLayout(self.qtgui_tab_widget_1_grid_layout_1)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_1, "clock")
        self.qtgui_tab_widget_1_widget_2 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_2 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_2)
        self.qtgui_tab_widget_1_grid_layout_2 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_2.addLayout(self.qtgui_tab_widget_1_grid_layout_2)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_2, "equilizer")
        self.qtgui_tab_widget_1_widget_3 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_3 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_3)
        self.qtgui_tab_widget_1_grid_layout_3 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_3.addLayout(self.qtgui_tab_widget_1_grid_layout_3)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_3, "frequency correction")
        self.qtgui_tab_widget_1_widget_4 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_4 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_4)
        self.qtgui_tab_widget_1_grid_layout_4 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_4.addLayout(self.qtgui_tab_widget_1_grid_layout_4)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_4, "difference")
        self.qtgui_tab_widget_1_widget_5 = Qt.QWidget()
        self.qtgui_tab_widget_1_layout_5 = Qt.QBoxLayout(Qt.QBoxLayout.TopToBottom, self.qtgui_tab_widget_1_widget_5)
        self.qtgui_tab_widget_1_grid_layout_5 = Qt.QGridLayout()
        self.qtgui_tab_widget_1_layout_5.addLayout(self.qtgui_tab_widget_1_grid_layout_5)
        self.qtgui_tab_widget_1.addTab(self.qtgui_tab_widget_1_widget_5, "in/out")
        self.top_layout.addWidget(self.qtgui_tab_widget_1)
        self._phase_bw_range = Range(0.0, 1.0, 0.01, 6.0/100.0, 200)
        self._phase_bw_win = RangeWidget(self._phase_bw_range, self.set_phase_bw, "Phase: Bandwidth", "slider", float)
        self.top_layout.addWidget(self._phase_bw_win)
        self._eq_gain_range = Range(0.0, 0.1, 0.0001, 10.0e-3, 200)
        self._eq_gain_win = RangeWidget(self._eq_gain_range, self.set_eq_gain, "Equalizer: rate", "slider", float)
        self.top_layout.addWidget(self._eq_gain_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(250e3)
        self.uhd_usrp_source_0.set_center_freq(frequency, 0)
        self.uhd_usrp_source_0.set_gain(30, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.uhd_usrp_source_0.set_bandwidth(250e3, 0)
        self.tutorial_my_qpsk_demod_cb_1 = tutorial.my_qpsk_demod_cb(False)
        self.qtgui_freq_sink_x_2 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_2.set_update_time(0.10)
        self.qtgui_freq_sink_x_2.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_2.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_2.enable_autoscale(False)
        self.qtgui_freq_sink_x_2.enable_grid(False)
        self.qtgui_freq_sink_x_2.set_fft_average(1.0)
        self.qtgui_freq_sink_x_2.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_2.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_2.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_2.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_2.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_2.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_2.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_2.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_2_win = sip.wrapinstance(self.qtgui_freq_sink_x_2.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_grid_layout_1 .addWidget(self._qtgui_freq_sink_x_2_win,  0,1)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_1.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_grid_layout_0 .addWidget(self._qtgui_freq_sink_x_1_win,  0,1)
        self.qtgui_freq_sink_x_0_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0_0.enable_grid(False)
        self.qtgui_freq_sink_x_0_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_grid_layout_3 .addWidget(self._qtgui_freq_sink_x_0_0_win,  0,1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_freq_sink_x_0.disable_legend()
        
        if "complex" == "float" or "complex" == "msg_float":
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_grid_layout_2 .addWidget(self._qtgui_freq_sink_x_0_win,  0,1)
        self.output_0_1_0 = qtgui.time_sink_f(
        	500, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.output_0_1_0.set_update_time(0.10)
        self.output_0_1_0.set_y_axis(-1, 1)
        
        self.output_0_1_0.set_y_label("Amplitude", "")
        
        self.output_0_1_0.enable_tags(-1, True)
        self.output_0_1_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.output_0_1_0.enable_autoscale(False)
        self.output_0_1_0.enable_grid(False)
        self.output_0_1_0.enable_control_panel(True)
        
        if not True:
          self.output_0_1_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.output_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.output_0_1_0.set_line_label(i, labels[i])
            self.output_0_1_0.set_line_width(i, widths[i])
            self.output_0_1_0.set_line_color(i, colors[i])
            self.output_0_1_0.set_line_style(i, styles[i])
            self.output_0_1_0.set_line_marker(i, markers[i])
            self.output_0_1_0.set_line_alpha(i, alphas[i])
        
        self._output_0_1_0_win = sip.wrapinstance(self.output_0_1_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_grid_layout_5 .addWidget(self._output_0_1_0_win,  0,1)
        self.equilizer_0 = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.equilizer_0.set_update_time(0.10)
        self.equilizer_0.set_y_axis(-2, 2)
        self.equilizer_0.set_x_axis(-2, 2)
        self.equilizer_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.equilizer_0.enable_autoscale(False)
        self.equilizer_0.enable_grid(False)
        
        if not True:
          self.equilizer_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.equilizer_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.equilizer_0.set_line_label(i, labels[i])
            self.equilizer_0.set_line_width(i, widths[i])
            self.equilizer_0.set_line_color(i, colors[i])
            self.equilizer_0.set_line_style(i, styles[i])
            self.equilizer_0.set_line_marker(i, markers[i])
            self.equilizer_0.set_line_alpha(i, alphas[i])
        
        self._equilizer_0_win = sip.wrapinstance(self.equilizer_0.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_grid_layout_3 .addWidget(self._equilizer_0_win,  0,0)
        self.equilizer = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.equilizer.set_update_time(0.10)
        self.equilizer.set_y_axis(-2, 2)
        self.equilizer.set_x_axis(-2, 2)
        self.equilizer.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.equilizer.enable_autoscale(False)
        self.equilizer.enable_grid(False)
        
        if not True:
          self.equilizer.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.equilizer.set_line_label(i, "Data {0}".format(i))
            else:
                self.equilizer.set_line_label(i, labels[i])
            self.equilizer.set_line_width(i, widths[i])
            self.equilizer.set_line_color(i, colors[i])
            self.equilizer.set_line_style(i, styles[i])
            self.equilizer.set_line_marker(i, markers[i])
            self.equilizer.set_line_alpha(i, alphas[i])
        
        self._equilizer_win = sip.wrapinstance(self.equilizer.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_grid_layout_2 .addWidget(self._equilizer_win,  0,0)
        self.digital_pfb_clock_sync_xxx_0 = digital.pfb_clock_sync_ccf(sps, timing_loop_bw, (rrc_taps), nfilts, nfilts/2, 1.5, 2)
        self.digital_map_bb_0 = digital.map_bb(([0,1,2,3]))
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(phase_bw, arity, False)
        self.digital_cma_equalizer_cc_0 = digital.cma_equalizer_cc(15, 1, eq_gain, 2)
        self.clock = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.clock.set_update_time(0.10)
        self.clock.set_y_axis(-2, 2)
        self.clock.set_x_axis(-2, 2)
        self.clock.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.clock.enable_autoscale(False)
        self.clock.enable_grid(False)
        
        if not True:
          self.clock.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.clock.set_line_label(i, "Data {0}".format(i))
            else:
                self.clock.set_line_label(i, labels[i])
            self.clock.set_line_width(i, widths[i])
            self.clock.set_line_color(i, colors[i])
            self.clock.set_line_style(i, styles[i])
            self.clock.set_line_marker(i, markers[i])
            self.clock.set_line_alpha(i, alphas[i])
        
        self._clock_win = sip.wrapinstance(self.clock.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_grid_layout_1 .addWidget(self._clock_win,  0,0)
        self.channel = qtgui.const_sink_c(
        	1024, #size
        	"", #name
        	1 #number of inputs
        )
        self.channel.set_update_time(0.10)
        self.channel.set_y_axis(-2, 2)
        self.channel.set_x_axis(-2, 2)
        self.channel.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.channel.enable_autoscale(False)
        self.channel.enable_grid(False)
        
        if not True:
          self.channel.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.channel.set_line_label(i, "Data {0}".format(i))
            else:
                self.channel.set_line_label(i, labels[i])
            self.channel.set_line_width(i, widths[i])
            self.channel.set_line_color(i, colors[i])
            self.channel.set_line_style(i, styles[i])
            self.channel.set_line_marker(i, markers[i])
            self.channel.set_line_alpha(i, alphas[i])
        
        self._channel_win = sip.wrapinstance(self.channel.pyqwidget(), Qt.QWidget)
        self.qtgui_tab_widget_1_grid_layout_0 .addWidget(self._channel_win,  0,0)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(2, 8, "", False, gr.GR_MSB_FIRST)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_file_sink_0 = blocks.file_sink(gr.sizeof_char*1, "/home/sudhir/Desktop/EE340_Project/Output/output.png", False)
        self.blocks_file_sink_0.set_unbuffered(True)
        self.blocks_char_to_float_0_0_1_0 = blocks.char_to_float(1, 1)
        self.blks2_packet_decoder_0_0 = grc_blks2.packet_demod_b(grc_blks2.packet_decoder(
        		access_code=code1,
        		threshold=-1,
        		callback=lambda ok, payload: self.blks2_packet_decoder_0_0.recv_pkt(ok, payload),
        	),
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_packet_decoder_0_0, 0), (self.blocks_char_to_float_0_0_1_0, 0))    
        self.connect((self.blks2_packet_decoder_0_0, 0), (self.blocks_file_sink_0, 0))    
        self.connect((self.blocks_char_to_float_0_0_1_0, 0), (self.output_0_1_0, 0))    
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.blks2_packet_decoder_0_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))    
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.digital_costas_loop_cc_0, 0))    
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.equilizer, 0))    
        self.connect((self.digital_cma_equalizer_cc_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.equilizer_0, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_freq_sink_x_0_0, 0))    
        self.connect((self.digital_costas_loop_cc_0, 0), (self.tutorial_my_qpsk_demod_cb_1, 0))    
        self.connect((self.digital_map_bb_0, 0), (self.blocks_repack_bits_bb_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.clock, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.digital_cma_equalizer_cc_0, 0))    
        self.connect((self.digital_pfb_clock_sync_xxx_0, 0), (self.qtgui_freq_sink_x_2, 0))    
        self.connect((self.tutorial_my_qpsk_demod_cb_1, 0), (self.digital_map_bb_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.channel, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.digital_pfb_clock_sync_xxx_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_1, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_nfilts(self):
        return self.nfilts

    def set_nfilts(self, nfilts):
        self.nfilts = nfilts
        self.set_rrc_taps(firdes.root_raised_cosine(self.nfilts, self.nfilts, 1.0/float(self.sps), 0.35, 11*self.sps*self.nfilts))

    def get_timing_loop_bw(self):
        return self.timing_loop_bw

    def set_timing_loop_bw(self, timing_loop_bw):
        self.timing_loop_bw = timing_loop_bw
        self.digital_pfb_clock_sync_xxx_0.set_loop_bandwidth(self.timing_loop_bw)

    def get_taps(self):
        return self.taps

    def set_taps(self, taps):
        self.taps = taps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.output_0_1_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_0_0.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_2.set_frequency_range(0, self.samp_rate)

    def get_rrc_taps(self):
        return self.rrc_taps

    def set_rrc_taps(self, rrc_taps):
        self.rrc_taps = rrc_taps
        self.digital_pfb_clock_sync_xxx_0.update_taps((self.rrc_taps))

    def get_phase_bw(self):
        return self.phase_bw

    def set_phase_bw(self, phase_bw):
        self.phase_bw = phase_bw
        self.digital_costas_loop_cc_0.set_loop_bandwidth(self.phase_bw)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.uhd_usrp_source_0.set_center_freq(self.frequency, 0)

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw

    def get_eq_gain(self):
        return self.eq_gain

    def set_eq_gain(self, eq_gain):
        self.eq_gain = eq_gain
        self.digital_cma_equalizer_cc_0.set_gain(self.eq_gain)

    def get_code1(self):
        return self.code1

    def set_code1(self, code1):
        self.code1 = code1

    def get_arity(self):
        return self.arity

    def set_arity(self, arity):
        self.arity = arity


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
