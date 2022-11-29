# OctoPrint-TuyaCloud

A plugin to control Tuya Cloud switches.

## Setup

This is not published. Zip the repo content and install manually on Octoprint's plugin manager.

## Configuration

In the plugin settings setup:

* API Endpoint: the Tuya api endpoint depending on the project region:
    | Region      | API Endpoint |
    | ----------- | ----------- |
    | China Data Center             | https://openapi.tuyacn.com |
    | Western America Data Center	| https://openapi.tuyaus.com |
    | Eastern America Data Center	| https://openapi-ueaz.tuyaus.com
    | Central Europe Data Center	| https://openapi.tuyaeu.com
    | Western Europe Data Center	| https://openapi-weaz.tuyaeu.com
    | India Data Center	| https://openapi.tuyain.com

* Access Id: the Tuya cloud project access id.
* Access Key: the Tuya cloud project access key.
* Device Id: the device id of the switch/outlet setup in the tuya cloud project.
