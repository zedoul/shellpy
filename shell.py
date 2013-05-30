import new
import traceback
import __builtin__
import sys

class PrintHook(object):
	def __init__(self):
		sys.stdout.flush()
		sys.stderr.flush()
		sys.stdout = self
		sys.stderr = self
	def write(self,t):
		self.text = t
		sys.stdout = sys.__stdout__
		sys.stderr = sys.__stderr__
	def getText(self):
		return self.text

class ShellPy(object):
	def __init__(self, order_num=3):
		pass

	def run(self, statement):
		try:
			compiled = compile(statement, '<string>', 'single')
			statement_module = new.module('__main__')
			statement_module.__builtins__ = __builtin__
			hooker = PrintHook()
			exec compiled in statement_module.__dict__
			return hooker.getText()
		except:
			return traceback.format_exc()

if __name__ == '__main__':
	obj = ShellPy()
	det = obj.run("a=3;b=5;a+b")
	print det
	det = obj.run("import sys;dir(sys)")
	print det
