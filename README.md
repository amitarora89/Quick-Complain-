📱 Quick Complaint App

A simple yet powerful offline tool to register customer complaints — fast, reliable, and fully guided in Hindi.


---

🔍 Introduction

Quick Complaint App is a lightweight, user-friendly application designed to help local shops, field technicians, small service providers, and solo business operators digitally register customer complaints — without relying on the internet, external databases, or complex systems.

Built with Python and Kivy, the app works seamlessly on Android (via Pydroid3) or desktop environments, providing a fully offline, step-by-step flow that captures all essential customer information in a structured and repeatable way.


---

🎯 Purpose

In many parts of the world — especially in small towns, rural areas, or informal businesses — complaints are often handled verbally or recorded on paper. This leads to miscommunication, lost data, and poor customer service.

Quick Complaint App addresses this problem by:

Providing a digital workflow for complaint intake

Eliminating dependency on paper forms

Requiring no internet or advanced hardware

Offering a clean, consistent, and culturally relevant UI (Hindi support)



---

🧠 How It Works

The app follows a guided five-step question flow, one input at a time:

1. Customer Name – Displayed respectfully with “Ji” (e.g., "Amit Ji")


2. Product Name – For example, "AC", "Phone", "Inverter"


3. Problem Description – A brief note about the issue


4. Address – Where the technician may visit


5. Phone Number – For callback or updates



After collecting this information, the app presents a summary screen where users can review all their answers. They can either confirm and generate a complaint number or choose to restart the form.

Once confirmed, the app displays a polite thank-you message along with a Complaint ID (e.g., C4872), and the process ends cleanly.


---

🧩 Features

Fully Offline Operation: No database, no cloud — ideal for remote locations or simple setups.

Hindi Language Support: Entire UI is written in formal, polite Hindi, accessible to a wide audience.

Step-by-Step UX: The app presents one question at a time to avoid confusion and guide the user intuitively.

Auto-Formatted Inputs: Capitalizes names and entries for consistency and professionalism.

Complaint Summary Screen: Final screen allows review before submission to prevent mistakes.

Random Complaint Number: A simple unique ID (like “C3581”) helps in tracking the complaint.

Custom UI Styling: Uses bold maroon headers, large fonts, and high-contrast colors for easy readability.

Cross-Platform: Works on any system with Python + Kivy installed, including Android (via Pydroid3).



---

🎨 UI/UX Design Decisions

Yellow Background: Selected to be soothing to the eyes and improve readability in both daylight and low-light environments.

Large Bold Text: Ensures clarity for users of all age groups and literacy levels.

Color Psychology:

Red for primary action ("Continue")

Green for positive confirmation ("Yes")

Maroon for headlines — authoritative but soft


Minimalist Layout: Each screen focuses on a single question, reducing visual clutter and increasing focus.



---

⚙️ Technical Overview

Language: Python 3.x (Recommended: 3.9 or newer)

Framework: Kivy — used for building cross-platform GUI interfaces

Single File Application: All logic is contained in quick_complain_app.py for simplicity and portability

State Tracking: The app uses a self.stage variable to control the progression of the complaint flow

User Data Handling: All inputs are temporarily stored in a simple dictionary (self.user_data)

Helper Functions:

capitalize_words() ensures uniform case formatting

bold_maroon() wraps text in Kivy markup for stylized display


Random Module: Used to generate a pseudo-unique complaint number for reference



---

📌 Use Cases

This app is suitable for:

Mobile service centers (AC repair, phone repair, home appliances)

Local grocery shops taking customer feedback

Electricians, plumbers, and freelancers collecting issue reports

NGO field agents collecting issues in rural areas

Internal use at warehouses, clinics, or small offices


Wherever there's no structured CRM system, Quick Complaint App fills the gap with a no-frills, reliable interface.


---

🚧 Current Limitations

No Persistent Storage: Data is lost on app exit. Currently designed for single-use complaints.

Basic ID System: Complaint numbers are randomly generated; there's a theoretical chance of repetition over time.

Single Complaint at a Time: No multi-entry or list views are implemented yet.

Language Restriction: Currently available only in Hindi.



---

🚀 Future Improvements

Several enhancements are planned for future versions:

Data Export: Save complaints to Excel/CSV files for record-keeping or analysis

Cloud Integration: Optional Google Sheets or Firebase sync for multi-device use

Admin Dashboard: View, search, and filter complaint records in-app

Improved ID System: Use timestamp or UUID-based complaint identifiers for uniqueness

Voice Input: Allow voice-based answers for accessibility

Multilingual Support: Add English and other regional languages



---

🎯 Why This Project Matters

The Quick Complaint App directly addresses everyday challenges in non-digitized, offline business environments. It improves customer service, minimizes forgetfulness, and eliminates messy paperwork.

Increases accountability by providing a digital trail

Builds trust with customers via acknowledgment and confirmation

Empowers small businesses to step into digital systems — one step at a time

Acts as a stepping stone for developing larger CRM workflows in the future



---

🧪 Summary for Reviewers & Recruiters

This project demonstrates:

User-Centric Thinking: UI and flow optimized for real-world use

Practical Problem Solving: Designed around an actual use case common across industries

Technical Simplicity with Logical Design: Clear stage-based flow, structured code, modular logic

Desire to Learn and Build: Built independently as a self-driven initiative using open frameworks

Adaptability: The codebase is lightweight and can be easily extended for professional applications



---

📄 License

This project is licensed under the MIT License — free to use, modify, and redistribute.


---

📫 Contact

To suggest improvements, request features, or report issues, feel free to:

Open an issue on this repository

Fork the project and contribute directly
