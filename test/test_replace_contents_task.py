import os
import shutil
import tasks.replace_contents_task


class TestReplaceContentsTask(object):
	task = tasks.replace_contents_task.ReplaceContentsTask()

	def test_execute_task(self):
		shutil.copy('test/res/CodeSample.m', 'test/res/CodeSampleCp.m')
		task_parameters = {'path': 'test/res/CodeSampleCp.m', 'to_replace': 'application\\w+', 'replace_with': 'frustration'}
		self.task.execute_task(task_parameters)

		code_sample = ''

		with open('test/res/CodeSampleCp.m', 'r') as code_sample_file:
			code_sample = code_sample_file.read()

		os.remove('test/res/CodeSampleCp.m')

		assert code_sample == '#import "AppDelegate.h"\n@implementation AppDelegate\n- (BOOL)application:(UIApplication *)frustration didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {\nreturn YES;\n}\n@end'
