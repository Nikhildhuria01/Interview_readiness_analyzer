import Webcam from "react-webcam";

export default function Camera() {

    return (

        <Webcam

            audio={false}

            mirrored

            className="rounded-xl w-full h-full"

        />

    );

}