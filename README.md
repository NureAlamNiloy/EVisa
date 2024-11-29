# **E-Visa Management System**

The **E-Visa Management System** is an efficient and scalable solution for managing online visa applications. It simplifies visa processing through features such as user authentication, visa application tracking, interview scheduling, and admin reports. Built with Django Rest Framework (DRF), the system ensures secure and seamless interaction between users and administrators.

---

## **Features**

### **User Features**
1. **Online Visa Application**:
   - Users can submit visa applications online by providing required details and uploading necessary documents.

2. **Visa Application Tracking**:
   - Users receive a **unique tracking ID** via email upon submission.
   - The tracking ID allows users to monitor their application status.

3. **Interview Scheduling**:
   - If required, users can book interview slots from available dates.

4. **Email Notifications**:
   - Automatic email notifications are sent to users for application updates, including tracking IDs and status changes.

---

### **Admin Features**
1. **Manage Visa Applications**:
   - Admins can view, approve, reject, or update visa applications.

2. **Reports and Analytics**:
   - View visa statistics with **weekly, monthly, and yearly reports**.

3. **Manage Interview Slots**:
   - Admins can create and manage interview slots, including setting limits on the number of interviews per day.

4. **Advanced Filters**:
   - Filter visa applications by:
     - **Date Range**
     - **Visa Type**
     - **Interview Status**

5. **Edit Application Details**:
   - Admins can modify visa application fields like status, message, and visa type without resubmitting the form.

---

## **Technology Stack**
- **Backend**: Django Rest Framework (DRF)
- **Authentication**: JWT Authentication
- **Database**: MySQL
- **Payment Gateway**: Stripe Integration
- **Other Tools**: 
  - CORS for handling cross-origin requests.
  - Email services for notifications.

### Other Tools
- **CORS**: For handling cross-origin requests.  
- **Email Services**: For notifications.
---

## Additional Information

This project was developed to address the growing need for online visa processing systems. By leveraging Django Rest Framework, the system ensures a robust backend and a seamless user experience.

Some key highlights of the implementation include:
- Scalable design for handling multiple user requests.
- Security features, such as JWT Authentication, for secure access.
- Easy-to-use admin interface for managing visa applications.

---

###### Backend: https://evisa-z93n.onrender.com/account/register/
###### Frontend: https://visa-frontend-five.vercel.app/
---
## **Installation Guide**

#### **1. Clone the Repository**
```bash
git clone https://github.com/NureAlamNiloy/EVisa.git
cd EVisa
```

#### **2. Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
#### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **4. Configure the Database**
Update the database credentials in the settings.py file:
```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '<database_name>',
        'USER': '<database_user>',
        'PASSWORD': '<database_password>',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
#### **5. Apply Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```
#### **6. Run the Development Server**
```bash
python manage.py runserver
```
#### **7. Access the Application**
Open your browser and navigate to:
```bash 
http://127.0.0.1:8000/
```
---


## **Usage**

### **User Actions**
1. **Sign Up and Login**:
   - Users can register and log in to submit visa applications.

2. **Submit Visa Application**:
   - Provide required personal information and upload supporting documents.

3. **Track Visa Status**:
   - Use the tracking ID received via email to check the application status.

4. **Book Interview Slots**:
   - If approved for an interview, book available slots directly from the application.

---

### **Admin Actions**
1. **View and Manage Applications**:
   - Admin dashboard allows filtering and updating applications.

2. **Approve or Reject Applications**:
   - Update visa statuses (e.g., Approved, Rejected, In Review).

3. **Generate Reports**:
   - View visa application reports by day, week, or year.

4. **Schedule Interviews**:
   - Set dates and limits for interviews.

---

## **API Endpoints**

### **Authentication**
- **User Registration**: `/api/auth/register/`
- **Login**: `/api/auth/login/`
- **Logout**: `/api/auth/logout/`

### **Visa Application**
- **Submit Application**: `/api/visa/apply/`
- **View Applications**: `/api/visa/view/`
- **Update Application**: `/api/visa/update/<id>/`
- **Track Application**: `/api/visa/track/<tracking_id>/`

### **Admin**
- **View All Applications**: `/api/admin/visa/view/`
- **Update Application Status**: `/api/admin/visa/update/`
- **Reports**: `/api/admin/visa/reports/`

---

## **Project Workflow**

### **1. Application Submission**
- Users submit visa applications, including personal details and necessary documents.
- Application details are saved in the database.

### **2. Admin Processing**
- Admins review applications, approve or reject them, and notify users.

### **3. Status Tracking**
- Users can track the status of their application using the unique tracking ID.

### **4. Interview Scheduling**
- If approved for an interview, users select a slot from available dates.

---
