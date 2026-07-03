import { Upload } from "lucide-react";

interface UploadCardProps {

    title: string;

    description: string;

    buttonText: string;

    onFileSelect?: (file: File) => void;

}

export default function UploadCard({

    title,

    description,

    buttonText,

    onFileSelect

}: UploadCardProps) {

    return (

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-8 shadow-lg hover:border-cyan-500 transition">

            <Upload
                size={50}
                className="text-cyan-400 mb-6"
            />

            <h2 className="text-2xl font-bold text-white">

                {title}

            </h2>

            <p className="text-slate-400 mt-3">

                {description}

            </p>

            <input

                id={title}

                hidden

                type="file"

                accept=".pdf"

                onChange={(e) => {

                    if (

                        e.target.files &&
                        e.target.files[0]

                    ) {

                        onFileSelect?.(

                            e.target.files[0]

                        );

                    }

                }}

            />

            <label

                htmlFor={title}

                className="block mt-8 bg-cyan-500 hover:bg-cyan-600 text-center text-white py-3 rounded-xl cursor-pointer"

            >

                {buttonText}

            </label>

        </div>

    );

}