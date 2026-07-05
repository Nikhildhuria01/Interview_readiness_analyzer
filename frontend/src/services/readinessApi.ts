import api from "./api";

export const predictReadiness = async (

    fluency: number,

    correctness: number,

    eye_contact: number,

    posture: number,

    head_stability: number,

) => {

    const response = await api.post(

        "/readiness/predict",

        {

            fluency,

            correctness,

            eye_contact,

            posture,

            head_stability,

        }

    );

    return response.data;

};