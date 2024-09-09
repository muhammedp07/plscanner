 # Phishing Link Scanner

 Check the web application here: https://phishinglinkcanner.lol

A simple yet effective phishing link scanner built with Python and Flask. This tool provides a web-based interface for users to check if a URL might be a phishing attempt. The application uses a custom phishing detection algorithm and features a modern neon-themed design. Phishing Link Scanner is a web application designed to identify and analyze potentially malicious phishing links. The primary goal of this project is to provide users with a tool to enhance their online security by checking links against known phishing databases.

# Note

The site is not yet hosted online. However, you can clone this repository and run the application locally to test it.

## Features

- **Web Interface**: Enter URLs through an easy-to-use web form.
- **Instant Analysis**: Real-time detection and results.
- **Link Analysis**: Scans provided URLs to detect potential phishing threats.
- **Safe Browsing Integration**: Uses Google’s Safe Browsing API to cross-check links against a comprehensive threat database.
- **Secure Hosting**: Deployed on AWS EC2 with a custom domain and SSL certification to ensure secure communication.
- **Neon-Themed Design**: A sleek, cyber-inspired look with dark mode and neon accents.
- **Customizable**: Easy to adapt and extend the detection algorithms.

## Hosting

- **AWS EC2:** The project is hosted on an AWS EC2 instance, providing scalable and reliable cloud infrastructure.
- **Domain Name:** The application is accessible via the custom domain [phishinglinkscanner.lol](https://phishinglinkscanner.lol).
- **SSL Certificate:** An SSL certificate has been configured to enable secure HTTPS connections, ensuring encrypted communication between users and the server.

## Setup and Configuration

- **SSH Access:** PuTTY was used to connect to the EC2 instance securely and manage files. Detailed steps for connecting and managing the instance can be found [here](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html).
- **Nginx Configuration:** Nginx is configured to handle both HTTP and HTTPS requests. The configuration includes:
  - SSL setup for secure connections.
  - Redirection from HTTP to HTTPS to ensure all traffic is encrypted.

## Running the Application

- **Flask:** The application is built using Flask, a lightweight web framework for Python. Flask must be running for the application to function properly.
- **Gunicorn:** Plans are in place to set up Gunicorn for production deployment to efficiently serve the Flask application.

## Installation

To get started with the Phishing Link Scanner, follow these steps:

1. **Clone the Repository**

   ```bash
   git clone https://github.com/USERNAME/REPOSITORY_NAME.git
   cd REPOSITORY_NAME
   ```
## Set up environemnt (Optional but recommended)

   ```bash
      python -m venv venv
      source venv/bin/activate # On Windows, use `venv\Scripts\activate
      pip install -r requirements.txt # Install dependencies
      python app.py # Run the Application
```


### Customization
- **Replace `USERNAME` and `REPOSITORY_NAME`**: Update with your GitHub username and repository name.
- **Screenshot**: Add a real screenshot link or remove the screenshot section if not applicable.
- **Contact Links**: Replace placeholders with your actual LinkedIn and Discord profiles.

This `README.md` provides a clear overview of your project, installation instructions, usage details, and contact information.

## Usage

- Open the application in your web browser.
- Enter the URL you want to check in the input field.
- Click the "Scan" button.
- Click the "Scan" button.
- View the results below the form.

## Demo screenshots

Here’s how the application looks when running locally:

![Homepage Screenshot](images/Homepage.png)
*Homepage*


![Scan Results Screenshot](images/non_sus_link.png)
*Scan Results Screenshot non sus link*


![Scan Results Screenshot](images/sus_link.png)
*Scan Results Screenshot sus link*

## Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request. You can also open an issue to discuss any bugs or feature requests.

## Acknowledgements

- Flask: For the lightweight web framework.
- Jinja2: For the templating engine.
- Python: For the programming language.
- Google Cloud Console API Safe Browsing: For checking phishing links against Google's Safe Browsing database.

## Contact

For any questions or inquiries, please contact me via:

- **LinkedIn**: [Connect](https://www.linkedin.com/in/muhammedpatel007/)

