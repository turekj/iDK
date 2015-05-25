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

