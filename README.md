# 🚀 Job Automation Tool (Python)

A CLI-based job aggregation tool that fetches job listings from multiple sources, applies filters, and saves results as structured text files.

---

## 📌 Features

- 🔍 Fetch jobs from multiple providers:
  - RemoteOK
  - Remotive

- 🎯 Advanced filtering:
  - Keyword (role/title)
  - Location
  - Company
  - Source

- 📧 Email validation with retry logic (3 attempts)

- 🔁 Dynamic provider selection (switch-case logic)

- 📁 Auto-save results:
  - Unique file naming
  - Timestamp-based history
  - No empty file creation

---

## 🧱 Project Structure

job-automation-python/
│
├── jobs/
│ ├── providers/
│ │ ├── remoteok.py
│ │ ├── remotive.py
│ │
│ ├── aggregator.py
│
├── utils/
│ ├── validator.py
│ ├── input_handler.py
│
├── output/
│
├── main.py
├── requirements.txt
├── .gitignore

---

## ⚙️ Installation

```bash
git clone <https://github.com/MRI-DHUL/job-automation-python.git>
cd job-automation-python

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

```
---

▶️ Run the Application

```bash
python main.py

```
---

🧪 Example Flow

1. Enter email (validated with retries)

2. Select provider:
    - remoteok
    - remotive
    - all

3. Apply filters (optional)

4. View results

5. File saved in '/output'

---

📄 Output Example

```bash
Job 1

Title     : DevOps Engineer
Company   : XYZ
Location  : Remote
Apply Link: https://...
Source    : RemoteOK
--------------------------------------------------

```

---

🧠 Concepts Used

1. Python CLI development
2. API integration (requests)
3. Input validation
4. Loop & conditional filtering
5. Match-case (switch logic)
6. File handling & persistence
7. Modular architecture

---

