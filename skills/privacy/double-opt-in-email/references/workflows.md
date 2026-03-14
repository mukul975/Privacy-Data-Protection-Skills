# Workflows — Implementing Double Opt-In Email

## Workflow 1: Double Opt-In Subscription Flow

```
START: User visits CloudVault SaaS Inc. newsletter sign-up page
  │
  ├─► Step 1: Collect email and consent
  │     ├─ Email input field
  │     ├─ Unticked checkbox: "I'd like to receive product updates, tips,
  │     │   and news from CloudVault SaaS Inc. (max 2 emails/month)"
  │     ├─ Text below: "You can unsubscribe at any time. See our Privacy Policy."
  │     └─ [Subscribe] button
  │
  ├─► Step 2: Server-side validation
  │     ├─ Validate email format (RFC 5322)
  │     ├─ Check suppression list → if suppressed, show generic "Check your email"
  │     │   (do NOT reveal suppression status to prevent enumeration)
  │     ├─ Check if already confirmed subscriber → show "Already subscribed"
  │     ├─ Check if pending confirmation exists → do NOT resend (rate limiting)
  │     └─ Rate limit: max 3 DOI requests per IP per hour
  │
  ├─► Step 3: Create pending record
  │     ├─ Record: email, IP, user_agent, timestamp, consent text version
  │     ├─ Generate 256-bit token (cryptographically random)
  │     ├─ Set expiry: current_time + 48 hours
  │     └─ Status: "pending_confirmation"
  │
  ├─► Step 4: Send confirmation email
  │     ├─ Subject: "Confirm your CloudVault newsletter subscription"
  │     ├─ Body: confirmation link with token
  │     ├─ Sender: CloudVault SaaS Inc. <noreply@cloudvault-saas.eu>
  │     ├─ Physical address: 42 Innovation Drive, Dublin, D02 YX88 (CAN-SPAM compliance)
  │     └─ This is a transactional email, NOT a marketing email
  │
  ├─► Step 5: User clicks confirmation link
  │     ├─ Validate token (exists, not expired, not used)
  │     ├─ If valid:
  │     │   ├─ Status → "confirmed"
  │     │   ├─ Record confirmation: timestamp, IP, user_agent
  │     │   ├─ Add to active mailing list
  │     │   └─ Send welcome email (first marketing email)
  │     └─ If invalid: show appropriate error message
  │
  └─► Display: "Thank you! Your subscription is confirmed."
```

## Workflow 2: One-Click Unsubscribe (RFC 8058)

```
TRIGGER: User wants to unsubscribe from marketing emails
  │
  ├─► Method A: Email client one-click (RFC 8058)
  │     ├─ Email header: List-Unsubscribe-Post: List-Unsubscribe=One-Click
  │     ├─ Email client shows "Unsubscribe" button in UI
  │     ├─ Client sends POST to unsubscribe URL
  │     └─ Server processes immediately:
  │           ├─ Remove from active mailing list
  │           ├─ Add to suppression list
  │           ├─ Record withdrawal: timestamp, method "rfc8058_one_click"
  │           └─ Cancel pending campaigns
  │
  ├─► Method B: Footer unsubscribe link
  │     ├─ User clicks unsubscribe link in email footer
  │     ├─ Landing page: "Unsubscribe from CloudVault emails?"
  │     │   [Unsubscribe] [Keep Receiving]
  │     ├─ User clicks [Unsubscribe]
  │     └─ Same server-side processing as Method A
  │
  └─► Confirmation:
        ├─ Web page: "You've been unsubscribed. You won't receive marketing emails."
        └─ Note: DO NOT send a "you've been unsubscribed" email
              (they just said they don't want emails)
```

## Workflow 3: Suppression List Management

```
TRIGGER: Email address needs to be suppressed
  │
  ├─► Adding to suppression list:
  │     ├─ Unsubscribe request → add immediately
  │     ├─ Hard bounce → add after first hard bounce
  │     ├─ Spam complaint → add immediately
  │     ├─ DSAR erasure request → add immediately
  │     └─ Record: email_hash, reason, timestamp, source
  │
  ├─► Checking suppression list:
  │     ├─ Before sending ANY marketing email
  │     ├─ Before sending DOI confirmation email
  │     ├─ Before importing email lists
  │     └─ During re-engagement campaigns
  │
  ├─► Handling re-subscription of suppressed email:
  │     ├─ User submits suppressed email on sign-up form
  │     ├─ Show generic "Check your email" (don't reveal suppression)
  │     ├─ Send DOI confirmation email with note:
  │     │   "You previously unsubscribed. Click to re-subscribe."
  │     ├─ If confirmed: remove from suppression, activate subscription
  │     └─ Record: re-subscription consent with full DOI trail
  │
  └─► Suppression list retention:
        ├─ Retain indefinitely (required to honor unsubscribe requests)
        ├─ Store only hashed email (data minimization)
        └─ This retention is lawful under GDPR Art. 17(3)(b) for legal obligation compliance
```
