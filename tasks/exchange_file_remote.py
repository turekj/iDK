import core.task
import urllib2


class ExchangeFileWithRemoteTask(core.task.Task):
	def execute_task(self, parameters=None):
		self._check_mandatory_parameters(['path', 'remote_path'], parameters)
		path = parameters['path']
		remote_path = parameters['remote_path']

		with open(path, 'w') as file_handle:
			response = urllib2.urlopen(remote_path)
			contents = response.read()
			file_handle.write(contents)
