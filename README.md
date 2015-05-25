# iDK

**iDK** (iOS Deployment Kit) is a project aimed to assist building iOS applications with complex setup. It offers multiple ways of altering the app's configuration before the build including:

- modifying propertly list (`.plist`) files,
- downloading and replacing the content from the web,
- regex find & replace file's contents.

## Why it was created?

The project was created to ease the process of creating multiple build configurations for the same app. Each configuration required altering a few parts of the build to work properly:

- exchange splash screen according to the build variant,
- exchange the configuration package according to the build variant,
- redefine constants,
- redefine property list contents.

In order to shorten a list of maintained build targets I decided to create a small utility which can handle all of the tasks outside the project itself.

## Before you start

Remember **iDK** is in the alpha stage right now. Although it can be functional it lacks in a lot of departments, such as error handling. You are using the application at your own risk!

## Quickstart

1. Download and install the latest version of Xcode and Xcode Command Line Tools from [Apple Developer webpage](https://developer.apple.com/downloads/index.action).
2. Install [pip](https://pip.pypa.io/en/stable/installing.html) (package installer for Python).
3. Clone repository contents, open the Terminal and `cd` to the clone directory.
4. Run `pip install -r requirements.txt` to install required dependencies.
5. Create the task configuration based on `example.yaml` file.
6. Run `python main.py configuration_name.yaml` command.

## Tasks

| Name | Description | Parameters |
| ---- | ----------- | ---------- |
| `clone` | Exports repository contents to the local drive. | <ul><li>`repository_type` - type of the repository. **Currently only `svn` is supported.**</li><li>`repository_path` - remote path to the repository.</li><li>`clone_path` - local path to export the repository contents to.</li></ul> |
| `create_dir` | Creates directory in the local file system. It fails if the directory already exists. | <ul><li>`path` - path to create.</li></ul>
| `exchange_file_remote` | Overrides (or creates) file in the local file system with contents downloaded from the web. | <ul><li>`path` - path to the file to create/override.</li><li>`remote_path` - path to the remote file which contents will be downloaded.</li></ul> |
| `export_ipa` | Archives the project and exports the archive to the `.ipa` file. | <ul><li>`project_path` - path to the `.xcodeproj` file.</li><li>`scheme` - name of the scheme to build. It has to be set shared inside *Manage Schemes...* in Xcode.</li><li>`archive_path` - path to the "temporary" archive file that will be created. It has to finish with non-existing file of `.xcarchive` type.</li><li>`ipa_path` - path under which the `.ipa` file will be exported in the local file system.</li><li>`provisioning_profile` - name of the provisioning profile that will be used to archive and export the `.ipa` file.</li></ul> |
| `plist_replace` | Replaces contents of property list files with given values. | <ul><li>`path` - local path to the property list file.</li><li>`contents` - dictionary of contents to replace property list with. The method will replace recursively only the keys matched in existing property list.</li></ul> |
| `remove_dir` | Removes directory from the local file system. It files if the directory does not exist. **Use the task with care cause it might lead to data loss!** | <ul><li>`path` - path of the directory to remove. All directory's contents will be erased as well.</li></ul> |
| `replace_contents` | Replaces contents of the file based on regular expressions. | <ul><li>`path` - path to the file which contents will be replaced.</li><li>`to_replace` - content to replace (regular expression lookup).</li><li>`replace_with` - content to be placed in place of matched one. It supports group references as documented in [re.sub()](https://docs.python.org/2/library/re.html#re.sub).</li></ul> |

## Configuration

To be added.
