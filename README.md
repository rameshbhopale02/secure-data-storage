# Secure Data Storage

A web-based platform for secure data storage and retrieval, utilizing advanced cryptography to ensure privacy, data integrity, and robust authentication. This project leverages SHA-256 hashing to keep user data encrypted and secure.

## Features

- **Data Encryption**: SHA-256 hashing to securely store user data in an irreversible format.
- **Private Key Authentication**: Users are provided an encrypted private key for authentication and data access.
- **User Authentication**: Secure login mechanism implemented with session handling via Python Flask.
- **Encrypted Data Storage**: Data is saved in `.zip` files protected with the user's private key.
- **Secure Data Retrieval**: Data can only be accessed by authenticated users with the correct private key.
- **Cross-Platform Support**: Accessible across devices to ensure flexibility and scalability.

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Cryptographic Methods**:
  - **SHA-256**: Secure hash algorithm for data integrity.
  - **Symmetric Encryption**: Ensures data protection with a single key.
- **Data Storage**: YAML for data serialization and `.zip` for secure file storage.

## Usage

### Sign Up:
1. Register by creating an account with a username, password, and email.
2. Receive an encrypted private key provided in both QR code and text format for secure data authentication.

### Log In:
1. Use your credentials and private key to log in securely.

### Data Storage:
1. Upload sensitive information such as bank details and personal data.
2. Data is encrypted using SHA-256 and stored in a secured `.zip` file format.

### Data Retrieval:
1. Enter your private key to fetch and download your stored data securely.

## Architecture

- **Frontend**: User-facing interface developed using HTML, CSS, and JavaScript for interactive design.
- **Backend**: Python Flask handles encryption processes, user authentication, and session management.
- **Data Storage**: YAML serialization for user data and `.zip` encryption for secure file management.


## Security Standards

- **Encryption**: Implements SHA-256 hashing for robust data encryption.
- **Authentication**: Uses private keys to ensure secure user identity verification.
- **Data Integrity**: Hashing prevents unauthorized modifications to stored data.
- **Scalability**: Engineered to support growing user data and ensure high performance under load.

## Results

### Example Screenshots:
1. **Home Page**:
   ![Home-Page](/static/screenshots/home_page.png)
   
2. **Home Page 2**:
   ![Home-Page](/static/screenshots/home_page2.png)

3. **User Registration**:
   ![User Registration](/static/screenshots/user_registration.png)

4. **Login User**:
   ![Login User](/static/screenshots/create_user.png)

5. **Services Section**:
   ![Data Retrieval](/static/screenshots/services-available.png)

6. **Services Available**:
   ![Data Retrieval](/static/screenshots/services.png)
   
7. **Store Personal Details**:
   ![Data Retrieval](/static/screenshots/personal_details.png)

8. **Store Bank Details**:
   ![Data Retrieval](/static/screenshots/store_bank_details.png)
   
9. **Fetch Details**:
   ![Data Retrieval](/static/screenshots/fetch_details.png)

10. **Download Fetch Data**:
   ![Data Retrieval](/static/screenshots/download_fetch_data.png)


### Steps for Deployment
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/organ-donation-system.git
   cd organ-donation-system
2. **Setup Virtualenvironment**:
    ```bash
    pip install virtualenv
    virtualenv venv
    venv\Scripts\Activate
3.  **Install the Required Libraries**:
      ```bash
      pip install -r requirements.txt
4.  **Run the Application**:
      ```bash
       python app.py
