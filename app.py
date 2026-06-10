from flask import Flask, render_template, request
import os

app = Flask(__name__)

responses = {
    "how many testing levels are there in software testing":
"There are 4 testing levels in software testing. They are Unit Testing, Integration Testing, System Testing, and Acceptance Testing. Each level checks the software from a different perspective to ensure quality and reliability. These levels help find defects early and improve the final product. Real-World Example: An online shopping app is tested module by module before releasing it to customers.",

"how many types of software testing are there":
"There are 2 main types of software testing: Manual Testing and Automation Testing. Manual testing is done by testers, while automation testing uses tools and scripts. Both methods help ensure software quality and performance. Real-World Example: A tester manually checks a login page while Selenium automates the same task.",

"what is python":
"Python is a high-level programming language that is easy to learn and use. It is widely used for web development, data science, machine learning, and automation. Python has simple syntax, making it beginner-friendly. Real-World Example: Netflix and Instagram use Python in many parts of their applications.",

"what is html":
"HTML stands for HyperText Markup Language. It is used to create the structure of web pages. HTML uses tags to display text, images, forms, and links. Every website uses HTML as its foundation. Real-World Example: The login page of Facebook is built using HTML.",

"what is css":
"CSS stands for Cascading Style Sheets. It is used to design and style web pages. CSS controls colors, fonts, layouts, and spacing. It makes websites attractive and user-friendly. Real-World Example: The colors and design of Amazon's website are controlled using CSS.",

"what is javascript":
"JavaScript is a programming language used to make web pages interactive. It can respond to user actions like clicks and form submissions. JavaScript runs inside the browser. Real-World Example: Showing a popup message when you click a button.",

"what is flask":
"Flask is a lightweight Python web framework. It helps developers create websites and web applications quickly. Flask is simple and easy to learn. Real-World Example: Your Hari Chatbot is built using Flask.",

"how many phases are there in sdlc":
"There are 6 main phases in SDLC: Requirement Gathering, Design, Development, Testing, Deployment, and Maintenance. These phases guide the software development process. Following SDLC improves project quality and management. Real-World Example: Building a banking application from planning to maintenance.",

"how many phases are there in stlc":
"There are 6 phases in STLC: Requirement Analysis, Test Planning, Test Case Development, Environment Setup, Test Execution, and Test Closure. These phases help testers perform organized testing. Real-World Example: Testing an online ticket booking system before launch.",

"what is selenium":
"Selenium is an automation testing tool used to test web applications. It supports multiple browsers and programming languages. Selenium helps reduce manual testing effort. Real-World Example: Automatically testing a website's login page every day.",

"what is a bug":
"A bug is an error or defect in software that causes incorrect results. Bugs can affect functionality, performance, or usability. Testers identify bugs and developers fix them. Real-World Example: A payment page that crashes after clicking Pay.",

"what is a defect":
"A defect is a problem found in software when the actual result differs from the expected result. Defects are reported to developers for fixing. Real-World Example: A login page accepting invalid passwords.",

"what is manual testing":
"Manual testing is the process of testing software manually without using automation tools. Testers execute test cases and verify results themselves. Real-World Example: Checking whether a shopping cart works correctly.",

"what is automation testing":
"Automation testing uses scripts and tools to execute test cases automatically. It is faster and useful for repetitive testing. Real-World Example: Running automated tests on an e-commerce website every night.",

"what is black box testing":
"Black box testing checks software functionality without looking at the source code. The tester focuses on inputs and outputs. Real-World Example: Using an ATM without knowing its internal programming.",

"what is white box testing":
"White box testing checks the internal code and logic of an application. It is usually performed by developers. Real-World Example: Testing all conditions and loops inside a program.",

"what is smoke testing":
"Smoke testing is a basic test performed to verify that major features work correctly. It is usually done after a new build is received. Real-World Example: Checking whether login and homepage functions work after deployment.",

"what is regression testing":
"Regression testing ensures that new changes have not affected existing features. It is performed after bug fixes or enhancements. Real-World Example: Testing old payment methods after adding a new one.",

"what is unit testing":
"Unit testing tests individual components or functions separately. It helps identify issues early in development. Real-World Example: Testing a function that calculates the total bill amount.",

"what is integration testing":
"Integration testing checks whether different modules work together properly. It focuses on interactions between components. Real-World Example: Testing communication between order and payment modules.",

"what is system testing":
"System testing evaluates the complete application as a whole. It ensures all requirements are met before release. Real-World Example: Testing a complete online shopping website.",

"what is acceptance testing":
"Acceptance testing verifies whether the software meets business requirements. It is usually performed before final release. Real-World Example: A client testing a project before approval.",

"what is performance testing":
"Performance testing measures the speed and responsiveness of an application. It ensures the software performs well under expected conditions. Real-World Example: Measuring response time of a ticket booking website.",

"what is load testing":
"Load testing checks application behavior under expected user traffic. It helps determine system capacity. Real-World Example: Testing a college portal with 5000 users simultaneously.",

"what is stress testing":
"Stress testing evaluates application behavior beyond normal limits. It helps identify breaking points. Real-World Example: Testing a website with 50000 users at once.",

"what is severity":
"Severity indicates how serious a defect is and how much it impacts the system. It is decided based on technical impact. Real-World Example: A payment failure is a high-severity defect.",

"what is priority":
"Priority indicates how quickly a defect should be fixed. It is decided based on business needs. Real-World Example: A spelling mistake on the homepage may have high priority.",

"what is api":
"API stands for Application Programming Interface. It allows different software applications to communicate with each other. APIs simplify data exchange between systems. Real-World Example: A weather app getting weather information from a weather service.",

"what is database":
"A database is a structured collection of data used for storing and managing information. Databases help applications retrieve data quickly. Real-World Example: A bank storing customer account details.",

"what is sql":
"SQL stands for Structured Query Language. It is used to store, retrieve, and manage data in databases. SQL is widely used in software applications. Real-World Example: Retrieving customer details from a banking database.",

"how many data types are there in python":
"Python has several data types. Common ones are int, float, string, list, tuple, dictionary, and boolean. Data types determine the kind of data stored. Real-World Example: Storing a customer's name as a string and age as an integer.",

"what is machine learning":
"Machine Learning is a branch of Artificial Intelligence that enables computers to learn from data and make predictions. It improves performance without explicit programming. Real-World Example: Netflix recommending movies based on viewing history.",

"what is artificial intelligence":
"Artificial Intelligence is the ability of machines to perform tasks that normally require human intelligence. AI can learn, reason, and make decisions. Real-World Example: Voice assistants like Siri and Alexa.",

"what is cloud computing":
"Cloud computing provides computing services over the internet. Users can access storage, servers, and software without owning physical hardware. Real-World Example: Storing files on Google Drive.",

"what is github":
"GitHub is a platform used to store, manage, and share code using Git version control. It helps developers collaborate on projects. Real-World Example: Uploading your Hari Chatbot project to GitHub."
}


@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""

    if request.method == "POST":
        question = request.form["question"].lower().strip()
        answer = responses.get(
            question,
            "Sorry, I don't know the answer to that question."
        )

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
   port = int(os.environ.get("PORT", 5000))
   app.run(host = "0.0.0.0", port = port)
   