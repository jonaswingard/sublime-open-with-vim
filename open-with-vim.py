import sublime
import sublime_plugin
import os

class OpenwithvimCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		os.system("gvim " + self.view.file_name())