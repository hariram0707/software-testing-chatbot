from flask import Flask, render_template, request
import os

app = Flask(__name__)

responses = {


"what is software testing": "Software testing is the process of checking whether software works correctly. It helps find errors and improve quality. Testing ensures the application meets user requirements. Real-World Example: Testing an online shopping website before customers use it.",

"what is manual testing": "Manual testing is testing software without using automation tools. Testers execute test cases manually and verify results. It helps identify usability and functional issues. Real-World Example: A tester checks whether a login page accepts valid credentials.",

"what is automation testing": "Automation testing uses tools and scripts to test software automatically. It reduces manual effort and saves time. It is useful for repetitive testing tasks. Real-World Example: Selenium automatically tests a website's login page.",

"what is a bug": "A bug is an error in software that causes incorrect results. Bugs can affect functionality and user experience. Testers report bugs to developers for fixing. Real-World Example: A payment page crashes when the Pay button is clicked.",

"what is a defect": "A defect is a difference between expected and actual results. Defects are found during software testing. They can impact software performance and reliability. Real-World Example: A login page allows access with an incorrect password.",

"what is black box testing": "Black box testing checks software functionality without viewing the source code. Testers focus on inputs and outputs. It ensures the software meets user requirements. Real-World Example: Using an ATM without knowing its internal code.",

"what is white box testing": "White box testing examines the internal code and program logic. It is usually performed by developers. It helps identify coding errors and security issues. Real-World Example: Testing all conditions in a banking application.",

"what is smoke testing": "Smoke testing verifies that important features work correctly. It is performed after receiving a new software build. It ensures the build is stable for testing. Real-World Example: Checking login and homepage functions after deployment.",

"what is sanity testing": "Sanity testing checks whether a specific bug fix works correctly. It is performed after small changes are made. It ensures the updated feature works as expected. Real-World Example: Verifying a fixed payment issue in an online store.",

"what is regression testing": "Regression testing ensures that new changes do not affect existing features. It is performed after updates or bug fixes. It helps maintain software stability. Real-World Example: Testing old payment methods after adding a new one.",

"what is unit testing": "Unit testing checks individual components of software. It helps identify issues early in development. Developers usually perform unit testing. Real-World Example: Testing a function that calculates the total bill amount.",

"what is integration testing": "Integration testing verifies that multiple modules work together correctly. It checks communication between components. It is performed after unit testing. Real-World Example: Testing communication between order and payment modules.",

"what is system testing": "System testing evaluates the complete application as a whole. It verifies that all requirements are met. It is performed before release. Real-World Example: Testing a complete online shopping website.",

"what is acceptance testing": "Acceptance testing verifies whether software meets business requirements. It is usually performed by clients or users. It confirms readiness for release. Real-World Example: A client testing a project before approval.",

"what is functional testing": "Functional testing checks whether software features work correctly. It focuses on business requirements and expected behavior. It ensures proper functionality. Real-World Example: Verifying that a login page works correctly.",

"what is non functional testing": "Non-functional testing evaluates performance, security, and usability. It focuses on how the system behaves. It ensures software quality beyond functionality. Real-World Example: Measuring website loading speed.",

"what is performance testing": "Performance testing measures the speed and responsiveness of software. It ensures the application performs well under expected conditions. It improves user experience. Real-World Example: Testing response time of a ticket booking website.",

"what is load testing": "Load testing checks application behavior under expected user traffic. It helps determine system capacity. It ensures stable performance. Real-World Example: Testing a website with 5000 users simultaneously.",

"what is stress testing": "Stress testing evaluates software beyond normal limits. It helps identify breaking points. It ensures system reliability under extreme conditions. Real-World Example: Testing a website with 50000 users at once.",

"what is selenium": "Selenium is an automation testing tool used for web applications. It supports multiple browsers and languages. It reduces manual testing effort. Real-World Example: Automating login testing for a shopping website."


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
   