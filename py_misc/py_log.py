import time
import getpass
def log(func): 
	def inner1(*args, **kwargs):
		# before
		begin = time.time()

		return_value_method = func(*args, **kwargs)

		# after
		end = time.time() 
		time_elapse = end - begin
		# method_name =  " ".join([word.capitalize() for word in func.__name__.replace("_", " ").split()])
		method_name =  func.__name__ + "()"
		user = getpass.getuser()
		if time_elapse < 1: 
			message = "(" + user + ")Running:\t%s\t[ exec-time = %.3f ms ]\n" % (method_name, time_elapse * 1000)
		else:
			message = "(" + user + ")Running:\t%s\t[ exec-time = %.3f s ]\n" % (method_name, time_elapse)
		file = open(" machine.log","a")
		file.write(message)
		file.close()
		return return_value_method
	return inner1