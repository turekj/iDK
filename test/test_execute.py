import collections
import core.config
import core.executor
import test.res.execution_task

class TestTaskExecutor(object):
	task_one = test.res.execution_task.TaskOne()
	task_two = test.res.execution_task.TaskTwo()
	executor = core.executor.TaskExecutor({'task_one': task_one, 'task_two': task_two})

	def test_execute_tasks(self):
		task_one_parameters = collections.OrderedDict([('param1', 't1p1'), ('param2', 't1p2')])
		task_two_parameters = collections.OrderedDict([('param1', 't2p1'), ('param2', 't2p2')])
		tasks = [core.config.TaskConfiguration('task_one', task_one_parameters), core.config.TaskConfiguration('task_two', task_two_parameters)]
		self.executor.execute_tasks(tasks)

		assert self.task_one.order == 1
		assert self.task_one.parameters == task_one_parameters
		assert self.task_two.order == 2
		assert self.task_two.parameters == task_two_parameters
