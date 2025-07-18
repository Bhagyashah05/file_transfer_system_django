IUDX Backend Task – File Ownership Transfer System

This project implements a Django REST API that allows users to transfer and revoke file ownership. It supports file uploads and maintains a full audit log of all transfer actions.

1. API Functionality Overview
File Transfer: Owner A can transfer a file to User B

Transfer Revocation: Original owner A can revoke the transfer

History Tracking: All transfers and revocations are timestamped and logged


2. Postman Testing Screenshots


a. Generate Token
Endpoint: POST /api/token/

Body:

json

{
  "username": "user_a",
  "password": "user12345678"
}
Screenshot: 

![alt text](<Screenshot 2025-07-19 002726.png>)

b. Upload File (via Django Admin)
Upload a file using the Django Admin panel

Screenshot: 

![alt text](<Screenshot 2025-07-19 001700.png>)

c. Transfer File Ownership
Endpoint: POST /api/transfer/

Body:

json

{
  "file_id": 1,
  "to_user_id": 3
}
Screenshot:

![alt text](<Screenshot 2025-07-19 004438.png>)

d. Revoke File Transfer
Endpoint: POST /api/revoke/

Body:

json

{
  "file_id": 1
}
Screenshot:

![alt text](<Screenshot 2025-07-19 003920.png>)

e. View Transfer History
Endpoint: GET /api/history/1/

Screenshot: 

![alt text](<Screenshot 2025-07-19 004918.png>)

3. Database State Screenshots


a. File Ownership Before Transfer
Screenshot: 

![alt text](<Screenshot 2025-07-19 001700-1.png>)

b. File Ownership After Transfer
Screenshot: 

![alt text](<Screenshot 2025-07-19 004425.png>)

c. File Ownership After Revoke
Screenshot:

![alt text](<Screenshot 2025-07-19 004501.png>)

d. Transfer History Log
Screenshot: 

![alt text](<Screenshot 2025-07-19 004518.png>)