import core.task
import os
import re


class ExportIPATask(core.task.Task):	
	def execute_task(self, parameters=None):
		self._check_mandatory_parameters(['project_path', 'scheme', 'archive_path', 'ipa_path', 'provisioning_profile'], parameters)
		project_path = parameters['project_path']
		scheme = parameters['scheme']
		archive_path = parameters['archive_path']
		ipa_path = parameters['ipa_path']
		provisioning_profile = parameters['provisioning_profile']
		provisioning_profile_uuid = None

		pattern_str = '\t<key>Name</key>\n\t<string>%s</string>' % provisioning_profile
		pattern = re.compile(pattern_str)

		for file_name in os.listdir(os.path.expanduser("~/Library/MobileDevice/Provisioning Profiles/")):
			if file_name.endswith(".mobileprovision"):
				file_path = '~/Library/MobileDevice/Provisioning Profiles/%s' % file_name
				with open(os.path.expanduser(file_path), 'r') as file_handle:
					file_contents = file_handle.read()
					search_result = pattern.search(file_contents)

					if search_result is not None:
						provisioning_profile_uuid = file_name[:-16]
						break

		os.system('xcodebuild -project "%s" -scheme "%s" archive -archivePath "%s" PROVISIONING_PROFILE="%s"' % (project_path, scheme, archive_path, provisioning_profile_uuid))
		os.system('xcodebuild -exportArchive -exportFormat ipa -archivePath "%s" -exportPath "%s" -exportProvisioningProfile "%s"' % (archive_path, ipa_path, provisioning_profile))
