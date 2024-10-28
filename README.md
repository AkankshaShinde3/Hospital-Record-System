# Blockchain Healthcare Management System

This project is a Blockchain-based Healthcare Management System developed using Python and Tkinter. It allows the secure storage of patient records by using blockchain principles, ensuring data immutability and tamper resistance. Each patient's data is saved as a block within the blockchain, linked to the previous block, making the data chain secure and verifiable.

## Features

- **Patient Data Storage:** Input patient information, which is securely added to the blockchain.
- **Immutable Records:** Each patient record is linked to the previous record through cryptographic hashes, creating an unalterable chain.
- **Tkinter GUI:** A user-friendly interface built with Tkinter for adding and viewing patient records.
- **Blockchain Visualizer:** View the blockchain to see stored patient records and their associated hashes.

## Technologies Used

- **Python 3**
- **Tkinter:** For creating the GUI.
- **Hashlib:** For generating SHA-256 hashes.
- **JSON:** For structuring patient data.

## How It Works

1. **Genesis Block Creation:** A genesis block is created upon initializing the blockchain.
2. **Adding a Patient Record:** Users can enter patient details through the GUI, which are added as a new block in the blockchain.
3. **Viewing the Blockchain:** Each block in the blockchain, including patient data and hashes, can be viewed in a new window.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/blockchain-healthcare-system.git
2. **Install Required Packages Ensure you have Python 3 installed. This program uses Tkinter and hashlib, which are included with standard Python installations.

3. **Run the Application
   ```bash
     python main.py
