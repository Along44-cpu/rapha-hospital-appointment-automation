# Rapha Hospital Appointment Automation

> Automated appointment booking workflow for Rapha Hospital with form processing, data persistence, and email notifications.

## Overview

This n8n workflow automates the appointment booking process for Rapha Hospital by capturing patient information from multiple sources, validating and processing the data, and notifying the hospital staff via email.

## Features

- **Multi-Source Form Handling**: Accepts appointment requests from both Tally forms and website forms
- **Intelligent Data Extraction**: Automatically detects source and extracts relevant fields
- **Patient Information Capture**: Collects name, phone, age, gender, visit reason, and preferred time
- **Data Persistence**: Appends all appointment requests to a Google Sheets spreadsheet for record-keeping
- **Real-Time Notifications**: Sends formatted HTML email notifications to hospital staff
- **Timezone Support**: Timestamps in IST (Asia/Kolkata timezone) for local context
- **Error Handling**: Graceful fallback values for missing or malformed data

## Workflow Architecture

```
Webhook (Multi-source input)
    ↓
Code Node (Data extraction & transformation)
    ↓
Google Sheets (Append row with patient data)
    ↓
Gmail (Send notification email)
```

### Step 1: Webhook
- Receives POST requests from both Tally forms and website forms
- Acts as the single entry point for appointment requests
- Validates incoming webhook data

### Step 2: Code Node (JavaScript)
- Detects request source (website vs Tally form)
- Extracts patient information with fallback handling
- Normalizes dropdown values from Tally forms
- Generates IST timestamp for all appointments
- Outputs standardized JSON with fields:
  - `timestamp` - Booking time (IST)
  - `patientName` - Full name
  - `phoneNumber` - Contact number
  - `age` - Patient age
  - `gender` - Gender information
  - `reasonForVisit` - Medical reason for appointment
  - `preferredTime` - Preferred appointment slot
  - `source` - Form source (Website/Tally)
  - `status` - Initial status (Pending)

### Step 3: Google Sheets Integration
- Appends appointment record to "Rapha Hospital - Appointments" spreadsheet
- Stores the following columns:
  - Timestamp
  - Full Name
  - Phone Number
  - Age
  - Gender
  - Reason for visit
  - Time (preferred)
  - Status
- Maintains audit trail of all appointment requests

### Step 4: Gmail Notification
- Sends professionally formatted HTML email to hospital staff
- Includes complete appointment details
- Color-coded header (Rapha Hospital branding)
- Call-to-action reminder to confirm appointment

## Setup Instructions

### Prerequisites
- n8n instance (self-hosted or cloud)
- Google Sheets API credentials
- Gmail account with OAuth2 credentials
- Access to Tally forms and/or website

### Installation

1. **Import the Workflow**
   - Copy the workflow JSON file
   - In n8n, go to Workflows → Import from File
   - Select `rapha-hospital-appointment-automation.json`

2. **Configure Credentials**
   - **Google Sheets**: Set up OAuth2 credentials for your Google account
   - **Gmail**: Configure Gmail OAuth2 credentials
   - Update the spreadsheet ID in the workflow to your target sheet

3. **Update Configuration**
   - Replace `alongdecor@gmail.com` with your hospital's notification email address
   - Update Google Sheet document ID if using a different sheet

4. **Enable Forms**
   - Tally Form: Connect your Tally form to the webhook URL provided by n8n
   - Website Form: Integrate the webhook URL into your appointment form submission handler

### Webhook URL Format
The webhook URL will be provided by n8n after workflow creation:
```
https://your-n8n-instance.com/webhook/9c3c3ccd-2eb4-46aa-be71-20d149305b71
```

## Form Input Specifications

### Website Form Fields
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

### Tally Form Fields
The workflow expects Tally form data with fields in this order:
1. Full Name (text)
2. Phone Number (text)
3. Age (text)
4. Gender (dropdown)
5. Reason for Visit (dropdown)
6. Preferred Time (dropdown)

## Email Notification Template

The workflow sends a branded HTML email containing:
- Hospital header with branding
- Complete patient information table
- Appointment details (date, time, reason)
- Call-to-action for staff to confirm appointment
- Professional footer

## Data Flow & Security

- **No sensitive data storage**: Credentials stored securely in n8n
- **GDPR compliant**: Patient data only stored in Google Sheets (encrypted at rest by Google)
- **Audit trail**: All requests logged with timestamp
- **Error resilience**: Missing data fields show "Not provided" instead of failing

## Troubleshooting

### Email not sending
- Verify Gmail OAuth2 credentials are active
- Check that the email address in the workflow is correct
- Ensure Gmail account has API access enabled

### Data not appearing in Google Sheets
- Verify Google Sheets OAuth2 credentials
- Check that the spreadsheet ID is correct
- Ensure the sheet columns match the workflow mapping

### Webhook not receiving data
- Verify webhook URL is correctly configured in form
- Check n8n logs for incoming requests
- Ensure webhook is not in "test" mode

## Future Enhancements

- SMS notifications to patient for appointment confirmation
- Automated appointment reminder emails
- Integration with hospital management system
- Payment gateway integration for appointment booking
- Calendar availability synchronization
- Automated appointment cancellation/rescheduling

## Support

For workflow issues or customization requests:
- Review the JavaScript code in the "Code in JavaScript" node
- Modify column mappings in the Google Sheets node
- Adjust email template in the Gmail node as needed

## License

This workflow is provided as-is for Rapha Hospital operations.

---

**Version**: 2.0  
**Last Updated**: May 2026  
**Status**: Production
