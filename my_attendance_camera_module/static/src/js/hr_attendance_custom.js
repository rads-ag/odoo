
//  /** @odoo-module **/
//  import { ActivityMenu } from "@hr_attendance/components/attendance_menu/attendance_menu";
//  import { patch } from "@web/core/utils/patch";
//  import { CameraDialog } from "./CameraDialog.js";
//  import { useService } from "@web/core/utils/hooks";
//  import { Component, useState } from "@odoo/owl";

//  console.log('ActivityMenu:', ActivityMenu);

// //  Preserve a reference to the original method
//  const originalSignInOut = ActivityMenu.prototype.signInOut;
//  const originalSetup = ActivityMenu.prototype.setup;
//  patch(ActivityMenu.prototype, {
//           setup(){
//              this.dialogService = useService('dialog')
//           originalSetup.call(this);
//           },
   
//      async signInOut() {
//          // Custom logic before calling the original method
//           this.dialogService.add(CameraDialog, {parent: this},);
//         console.log('Custom logic before calling the original method');
//          // Call the original method explicitly
//         await originalSignInOut.call(this);
       
//      },
//  });
/** @odoo-module **/
import { ActivityMenu } from "@hr_attendance/components/attendance_menu/attendance_menu";
import { patch } from "@web/core/utils/patch";
import { CameraDialog } from "./CameraDialog.js";
import { useService } from "@web/core/utils/hooks";

const { Component } = owl;

const originalSignInOut = ActivityMenu.prototype.signInOut;
const originalSetup = ActivityMenu.prototype.setup;

patch(ActivityMenu.prototype, {
    setup() {
        this.dialogService = useService('dialog');
        this.rpcService = useService('rpc'); // Use the RPC service
        originalSetup.call(this);
    },

    async signInOut() {
        // Fetch the boolean field value from the server
        const isCameraEnabled = await this.rpcService('/web/dataset/call_kw', {
            model: 'res.config.settings',
            method: 'get_camera_enabled', 
            args: [[]],
            kwargs: {},
        });


        if (isCameraEnabled) {
            // Open the camera dialog only if the field is true
            this.dialogService.add(CameraDialog, { parent: this });
        } else {
            console.log('Camera is disabled by configuration.');
        }

        // Call the original method
        await originalSignInOut.call(this);
    },
});

