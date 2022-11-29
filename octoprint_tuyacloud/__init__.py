# coding=utf-8
from __future__ import absolute_import

### (Don't forget to remove me)
# This is a basic skeleton for your plugin's __init__.py. You probably want to adjust the class name of your plugin
# as well as the plugin mixins it's subclassing from. This is really just a basic skeleton to get you started,
# defining your plugin as a template plugin, settings and asset plugin. Feel free to add or remove mixins
# as necessary.
#
# Take a look at the documentation on what other plugin mixins are available.

import octoprint.plugin
from tuya_connector import TuyaOpenAPI

class TuyacloudPlugin(
    octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.SimpleApiPlugin,
    octoprint.plugin.RestartNeedingPlugin
):

    ##~~ SettingsPlugin mixin

    def get_settings_defaults(self):
        return dict(
            api_endpoint="https://openapi.tuyaus.com", 
            access_id="-",
            access_key="-",
            device_id="-",
        )

    ##~~ AssetPlugin mixin

    def get_assets(self):
        return {
            "js": ["js/tuyacloud.js"],
            "css": ["css/tuyacloud.css"]
        }

    ##~~ TemplatePlugin mixin

    def get_template_configs(self):
        return [
            dict(type="settings", custom_bindings=False)
        ]

    ##~~ SimpleApiPlugin mixin

    def get_api_commands(self):
        return dict(on=[], off=[])

    def on_api_command(self, command, data):
        if command != "on" and command != "off":
            return

        api_endpoint = self._settings.get(["api_endpoint"])
        access_id = self._settings.get(["access_id"])
        access_key = self._settings.get(["access_key"])
        device_id = self._settings.get(["device_id"])

        body = dict({
            "commands": [
                {
                    "code": "switch_1",
                    "value": command == "on"
                }
            ]
        })

        openapi = TuyaOpenAPI(api_endpoint, access_id, access_key)
        openapi.connect()
        openapi.post("/v1.0/iot-03/devices/" + device_id + "/commands", body)

# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "TuyaCloud Plugin"


# Set the Python version your plugin is compatible with below. Recommended is Python 3 only for all new plugins.
# OctoPrint 1.4.0 - 1.7.x run under both Python 3 and the end-of-life Python 2.
# OctoPrint 1.8.0 onwards only supports Python 3.
__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = TuyacloudPlugin()