import core.task
import pytest

class TestTask(object):
	task = core.task.Task()

	def test_check_mandatory_parameters_raises_if_no_mandatory_parameter_given(self):
		parameters = {'param1': 'hello', 'param3': 'something'}
		mandatory_parameters = ['param1', 'param2', 'param3']

		with pytest.raises(core.task.TaskParameterException):
			self.task._check_mandatory_parameters(mandatory_parameters, parameters)

	def test_check_mandatory_parameters_does_not_raise_if_mandatory_parameters_supplied(self):
		parameters = {'a': 'b', 'c': 'd'}
		mandatory_parameters = ['a', 'c']

		self.task._check_mandatory_parameters(mandatory_parameters, parameters)

		assert True
