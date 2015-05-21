import core.config
import yaml

class TestTaskConfiguration(object):
	config = core.config.TaskConfigurationLoader()

	def test_load_configuration(self):
		configuration = self.config.load_configuration('test/res/test_task.yaml')

		assert len(configuration) == 3
		assert configuration[0].name == 'first_task'
		assert len(configuration[0].parameters) == 2
		assert configuration[0].parameters['some_parameter'] == 'Some parameter value'
		assert configuration[0].parameters['other_parameter'] == 'Other parameter value'
		assert configuration[1].name == 'second_task'
		assert len(configuration[1].parameters) == 0
		assert configuration[2].name == 'third_task'
		assert len(configuration[2].parameters) == 1
		assert configuration[2].parameters['stuff'] == 'This is stuff'
