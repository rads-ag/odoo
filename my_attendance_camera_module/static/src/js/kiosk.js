/** @odoo-module **/
import kiosk from "@hr_attendance/public_kiosk/public_kiosk_app";
import { patch } from "@web/core/utils/patch";
import { _t } from "@web/core/l10n/translation";


patch(kiosk.kioskAttendanceApp.prototype, {
    async onManualSelection(employeeId, enteredPin) {
        console.log('hhi');
        await super.onManualSelection(employeeId, enteredPin);
        debugger;
        console.log("Overridden onManualSelection function called.");
        
    }
         
});

