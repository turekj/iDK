import core.task
import os


class ExportIPATask(core.task.Task):	
	def execute_task(self, parameters=None):
		self._check_mandatory_parameters(['project_path', 'scheme', 'archive_path', 'ipa_path', 'provisioning_profile'], parameters)
		project_path = parameters['project_path']
		scheme = parameters['scheme']
		archive_path = parameters['archive_path']
		ipa_path = parameters['ipa_path']
		provisioning_profile = parameters['provisioning_profile']

		os.system('xcodebuild -project "%s" -scheme "%s" archive -archivePath "%s"' % (project_path, scheme, archive_path))
		os.system('xcodebuild -exportArchive -exportFormat ipa -archivePath "%s" -exportPath "%s" -exportProvisioningProfile "%s"' % (archive_path, ipa_path, provisioning_profile))
