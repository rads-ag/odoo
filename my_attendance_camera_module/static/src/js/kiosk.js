/** @odoo-module **/
import kiosk from "@hr_attendance/public_kiosk/public_kiosk_app";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";
import { CameraDialog } from "./CameraDialog.js";
import { useService } from "@web/core/utils/hooks";

const { Component } = owl;

const originalSelection = kiosk.kioskAttendanceApp.prototype.kioskConfirm;
const originalSetup = kiosk.kioskAttendanceApp.prototype.setup;

patch(kiosk.kioskAttendanceApp.prototype, {
    setup() {
        this.dialogService = useService('dialog');
        this.rpcService = useService('rpc'); // Use the RPC service
        originalSetup.call(this);
    },
    
    async kioskConfirm(employeeId) {
        console.log('Attempting to open camera dialog');
        try {
           
                // Open the camera dialog only if the field is true
                this.dialogService.add(CameraDialog, { parent: this });
           

            // Call the original function after camera check
            await super.kioskConfirm(employeeId);

        } catch (error) {
            console.error("Error during camera dialog open: ", error);
            
        }
    }
});
