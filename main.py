from tasks import *

import argparse
import core.config
import core.discovery
import core.executor


def main():
	parser = argparse.ArgumentParser(description='Execute automated deploy for iOS platform')
	parser.add_argument('config_file', type=str)
	args = parser.parse_args()

	execute_config(args.config_file)


def execute_config(config_file):
	print "Executing %s..." % config_file

	discovered_tasks = core.discovery.TaskDiscoverer().discover_tasks()
	configuration = core.config.TaskConfigurationLoader().load_configuration(config_file)
	core.executor.TaskExecutor(discovered_tasks).execute_tasks(configuration)

	print "Finished %s execution!" % config_file


if __name__ == '__main__':
	main()
