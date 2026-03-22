# Assignment-1_AWS_CE
To ensure your assignment report looks professional and meets the criteria for a Cloud Architect's documentation, you can use the following structured format. It combines the technical requirements of the UniEvent system with the specific implementation steps you have successfully completed.

***

# Technical Report: Deployment of UniEvent Management System

## 1. Executive Summary
This report details the initial deployment phase of **UniEvent**, a scalable university event management platform. The architecture is designed on AWS to ensure high availability, security, and fault tolerance. This phase focuses on the successful provisioning of the core computing infrastructure and web server environment.

## 2. Infrastructure & Network Configuration
The backbone of the UniEvent system relies on a custom Virtual Private Cloud (VPC) and specific networking components to facilitate public access while maintaining administrative security.

* **VPC and Subnetting:** The instance was launched within a dedicated VPC, associated with **Subnet C**.
* **Internet Connectivity:** An **Internet Gateway (IGW)** was attached to the VPC, and the **Route Table** was updated with an active route (`0.0.0.0/0`) pointing to the IGW to enable external traffic flow.
* **Static Addressing:** An **Elastic IP (18.221.134.209)** was allocated and associated with the EC2 instance to provide a persistent entry point for the web application.

## 3. Security Group Specification
Inbound traffic is strictly regulated through a stateful firewall (Security Group) to align with security best practices:

* **Administrative Access (SSH):** Port 22 is restricted to the administrator's specific source IP to prevent unauthorized remote access.
* **Web Traffic (HTTP):** Port 80 is open to `0.0.0.0/0` (Anywhere) to allow students and the university community to browse events.

## 4. Instance Provisioning & Web Server Deployment
The application environment was built using an **Amazon Linux 2023** AMI on a `t2.micro` instance type. The following procedural steps were executed via the command-line interface to prepare the web host:

1.  **System Optimization:** Updated all core packages to ensure the latest security patches.
    ```bash
    sudo yum update -y
    ```
2.  **Service Installation:** Installed the Apache HTTP Server (`httpd`) to handle web requests.
    ```bash
    sudo yum install -y httpd
    ```
3.  **Service Initialization:** Started the web service and configured it to persist across system reboots.
    ```bash
    sudo systemctl start httpd
    sudo systemctl enable httpd
    ```
4.  **Application Hosting:** Deployed a preliminary landing page to the document root (`/var/www/html/`) to verify successful architecture deployment.
    ```bash
    echo "<h1>Success! My Cloud Architecture is Working</h1>" | sudo tee /var/www/html/index.html
    ```

## 5. Implementation Verification
The deployment was verified by accessing the public Elastic IP via a web browser using the HTTP protocol. The successful render of the test page confirms that the VPC, Route Table, Internet Gateway, Security Group, and EC2 instance are correctly integrated.

***

**Next Phase Objectives:**
* Migrate EC2 instances to **private subnets** for enhanced security.
* Configure an **Elastic Load Balancer (ELB)** to ensure fault tolerance and system availability.
* Implement **S3 buckets** for secure storage of event posters and media.