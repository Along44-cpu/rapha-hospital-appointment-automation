## Rapha Hospital Appointment Automation

Automated appointment booking system that captures patient requests from multiple form sources, validates data in real-time, and notifies hospital staff instantly.

![n8n](https://img.shields.io/badge/n8n-Automation-orange)
![JavaScript](https://img.shields.io/badge/JavaScript-Logic-yellow)
![Google Sheets](https://img.shields.io/badge/Google_Sheets-Database-green)
![Gmail](https://img.shields.io/badge/Gmail-Notifications-red)
![Webhooks](https://img.shields.io/badge/Webhooks-Integration-blue)

### What It Does

- Receives appointment requests from Tally forms and website forms via webhook
- Automatically detects request source and extracts patient information
- Validates and standardizes data (name, phone, age, gender, visit reason, preferred time)
- Appends appointment record to Google Sheets for permanent storage
- Sends formatted HTML email notification to hospital staff with full appointment details
- Handles missing data gracefully with fallback values

### Tech Stack

- n8n (Workflow Automation)
- JavaScript (Code Nodes)
- Google Sheets (Database & Audit Trail)
- Gmail (Email Notifications)
- Webhooks (Multi-source Integration)
- IST Timezone Support

### Business Value

- **Eliminates manual data entry** – Appointment data flows directly from forms to spreadsheet
- **Faster staff response** – Instant email notifications ensure no appointment requests are missed
- **Multi-channel support** – Accepts appointments from both Tally and web forms through single workflow
- **Complete audit trail** – Every appointment logged with timestamp for compliance and analytics
- **Reduced errors** – Automated validation prevents incomplete or malformed bookings
- **24/7 availability** – Captures appointments anytime without manual intervention

## Workflow File

[View Workflow JSON](./workflow.json)

## Proof of Implementation

<img width="1887" height="863" alt="new scrr1" src="https://github.com/user-attachments/assets/c83a0fd1-ebb6-4fcb-9468-a6cc5dc96005" />



*Google Sheets audit trail with all appointment records*

## Setup Instructions

### Prerequisites


- n8n instance (self-hosted or cloud)
- Google Sheets API credentials
- Gmail account with OAuth2 credentials
- Tally form and/or website form setup

### Installation Steps

1. **Import the Workflow**
   - Download `workflow.json` from this repository
   - In n8n, go to **Workflows → Import from File**
   - Select the workflow JSON file

2. **Configure Credentials**
   - Add Google Sheets OAuth2 credentials
   - Add Gmail OAuth2 credentials
   - Update the spreadsheet ID in the Google Sheets node

3. **Customize Settings**
   - Replace notification email with your hospital address
   - Update spreadsheet name if needed

4. **Connect Form Sources**
   - Copy the webhook URL from n8n
   - Connect Tally form to send data to webhook
   - Connect website form to webhook endpoint

### Expected Data Format

**Website Form:**
```json
{
  "source": "website",
  "patientName": "John Doe",
  "phoneNumber": "9876543210",
  "age": "35",
  "gender": "Male",
  "reasonForVisit": "General Checkup",
  "preferredTime": "10:00 AM"
}
```

**Tally Form:** Fields should be ordered as: Name → Phone → Age → Gender → Reason → Time

---

**Version**: 2.0  
**Last Updated**: May 2026  
**Status**: Production Ready
