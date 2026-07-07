import Webcam from "react-webcam";
import { forwardRef } from "react";

const Camera = forwardRef<Webcam>(({}, ref) => {

    return (

        <Webcam
            ref={ref}
            audio={false}
            mirrored
            screenshotFormat="image/jpeg"
            className="rounded-xl w-full h-full"
        />

    );

});

export default Camera;