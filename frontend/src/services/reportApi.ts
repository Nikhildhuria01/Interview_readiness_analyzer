import api from "./api";

export const downloadInterviewReport = async (data: any) => {

    const response = await api.post(

        "/report/report/generate",

        data,

        {
            responseType: "blob",
        }

    );

    return response.data;

};
