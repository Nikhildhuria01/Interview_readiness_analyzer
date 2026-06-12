QUESTION_BANK = {

    "Python": [

        "What are Python decorators?",

        "Difference between list and tuple?",

        "Explain Python generators.",

        "What is GIL in Python?"

    ],

    "Java": [

        "Explain JVM, JRE and JDK.",

        "What is method overloading?",

        "Difference between abstract class and interface?",

        "Explain Java memory management."

    ],

    "Docker": [

        "What is Docker?",

        "Difference between Docker and VM?",

        "What is a Docker image?",

        "Explain Docker volumes."

    ],

    "AWS": [

        "What is EC2?",

        "Difference between EC2 and ECS?",

        "What is S3?",

        "Explain Auto Scaling."
    ]
}
def generate_questions(missing_skills):

    questions = []

    for skill in missing_skills:

        if skill in QUESTION_BANK:

            questions.extend(
                QUESTION_BANK[skill]
            )

    return questions