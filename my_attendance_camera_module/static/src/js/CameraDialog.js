/** @odoo-module */

import { Dialog } from "@web/core/dialog/dialog";
import { useService } from "@web/core/utils/hooks";
import { useRef, onMounted, useState, Component, onWillUnmount } from "@odoo/owl";
export class CameraDialog extends Component {
    setup() {
        super.setup();
        this.video = useRef('video');
        this.image = useRef('image');
        this.rpc = useService("rpc");
        this.state = useState({
            img: false
        })
        onMounted(async () => {
            this.video.el.srcObject = await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
        });
        onWillUnmount(() => {
            this.stopCamera();
        })
    }
     /**
     * Closes the camera
     */
    _cancel() {
        (this.env.dialogData).close()
        this.stopCamera();
    }
    /**
     * Saves the Image
     */
    _confirm() {
        let video = this.video.el
        let image = this.image.el
        const canvas = document.createElement("canvas");
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        const canvasContext = canvas.getContext("2d");
        canvasContext.drawImage(video, 0, 0);
        this.state.img = canvas.toDataURL('image/jpeg');
        //this.img_binary = this.state.img.split(',')[1]
        console.log('Captured Image Data:', this.state.img);
        video.classList.add('d-none');
        image.classList.remove('d-none');
        image.src = this.state.img
      
        this._save()
    }

    
    
    async _save(){
       
        //this.state.img = "data:image/jpeg;base64," + this.img_binary;
        const img_binary = this.state.img.split(',')[1];
        try {
            // RPC call to save the image in the backend
            await this.rpc("/attendance/save_image", { image_data:img_binary });
            console.log("Image successfully sent to the backend.");
        } catch (error) {
            console.error("Error saving the image:", error);
        }
        (this.env.dialogData).close()
        this.stopCamera();
    }
    _close(){
        this.stopCamera();
    }
   
    stopCamera(){
        this.video.el.srcObject.getVideoTracks().forEach((track) => {
            track.stop();
        });
    }
}
CameraDialog.template = "my_attendance_camera_module.camera_dialog";
CameraDialog.components = { Dialog };
