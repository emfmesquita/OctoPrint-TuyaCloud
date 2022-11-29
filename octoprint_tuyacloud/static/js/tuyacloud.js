/*
 * View model for OctoPrint-TuyaCloud
 *
 * Author: Edson Mesquita
 * License: AGPLv3
 */
$(function() {
    function TuyacloudViewModel() {
        var self = this;
        const sendCommand = command => OctoPrint.postJson(OctoPrint.getSimpleApiUrl('tuyacloud'), { command })
        self.on = () => sendCommand('on');
        self.off = () => sendCommand('off');
    }

    /* view model class, parameters for constructor, container to bind to
     * Please see http://docs.octoprint.org/en/master/plugins/viewmodels.html#registering-custom-viewmodels for more details
     * and a full list of the available options.
     */
    OCTOPRINT_VIEWMODELS.push({
        construct: TuyacloudViewModel,
        // ViewModels your plugin depends on, e.g. loginStateViewModel, settingsViewModel, ...
        dependencies: [ "settingsViewModel" ],
        // Elements to bind to, e.g. #settings_plugin_tuyacloud, #tab_plugin_tuyacloud, ...
        elements: [ "#navbar_plugin_tuyacloud" ]
    });
});
