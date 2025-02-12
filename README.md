<<<<<<< HEAD
# เว็บไซต์ MBTI Checker ส่วนบุคคล

## ภาพรวมของโปรเจกต์

**ชื่อโปรเจกต์:** เว็บไซต์ MBTI Checker ส่วนบุคคล

**แนวคิด:** สร้างเว็บไซต์ส่วนตัวที่แสดงผลงาน บล็อก แกลเลอรี และข้อมูลติดต่อ โดยใช้ Flask เป็นเบ็คเอนด์เฟรมเวิร์ก ใช้ CSS เฟรมเวิร์ก (เช่น Bootstrap) เพื่อออกแบบหน้าตาให้สวยงาม และบันทึกข้อมูลสำคัญ (เช่น ข้อมูลบทความหรือข้อความจากฟอร์มติดต่อ) ลงในฐานข้อมูล

### โครงสร้างไฟล์โปรเจกต์
=======
# mbti-checker-web-app/mbti-checker-web-app/README.md

# MBTI Checker Web App

This is a simple web application that allows users to check their MBTI personality type through a series of questions.

## Project Structure

```
mbti-checker-web-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── templates
│   │   └── index.html
│   └── static
│       ├── css
│       │   └── styles.css
│       └── js
│           └── scripts.js
├── run.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd mbti-checker-web-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the application, execute the following command:
```
python run.py
```

The application will be accessible at `http://0.0.0.0:5000`.

## Usage

Once the application is running, navigate to the home page to start the MBTI Checker. Follow the on-screen instructions to complete the questionnaire and discover your MBTI personality type.

## License

This project is licensed under the MIT License.
>>>>>>> bf289e4 (Updated quiz.html to navigate to results page and store MBTI result)
