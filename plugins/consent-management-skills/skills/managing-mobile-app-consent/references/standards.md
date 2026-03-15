# Regulatory Standards — Managing Mobile App Consent

## Primary Regulations

### GDPR and ePrivacy Directive

- **ePrivacy Directive Article 5(3)**: Applies to mobile apps — accessing device storage (cookies, local storage, device identifiers) requires consent unless strictly necessary for the service.
- **GDPR Article 7**: All conditions for consent apply to in-app consent flows: freely given, specific, informed, unambiguous, clear affirmative action, equal ease of withdrawal.
- **GDPR Article 25**: Data protection by design and by default — mobile apps must implement privacy-protective default settings.

### Apple App Tracking Transparency (ATT)

- Mandatory since iOS 14.5 (April 2021)
- Apps must call `ATTrackingManager.requestTrackingAuthorization()` before tracking
- IDFA returns all zeros without user permission
- Apple defines "tracking" as linking data from your app with third-party data for advertising or data broker sharing
- Pre-permission screens allowed but must not mimic or replace the system dialog
- App Store Review Guideline 5.1.2 requires compliance

### Google Play Developer Policy

- **User Data Policy**: Apps must be transparent about data access, collection, use, handling, and sharing
- **Advertising ID Policy**: Apps must respect user's ad personalization settings
- **Families Policy**: Apps targeting children must not transmit GAID
- **Data Safety Section**: Required disclosure of data types collected, shared, and security practices

## Supervisory Authority Guidance

### CNIL Recommendation on Mobile Applications (2023)

The French supervisory authority published guidance specific to mobile apps:
- Consent must be obtained before any non-essential SDK initializes and begins data collection
- SDK initialization must be "gated" by consent — the default state must be no-collection
- In-app consent flows must follow the same equal prominence and ease requirements as web consent banners
- App developers are responsible for the data collection activities of third-party SDKs they include

### German Federal Court (BGH) on Mobile Consent (2022)

Confirmed that in-app consent must meet the same GDPR standards as web consent:
- Pre-ticked toggles are prohibited
- Each purpose must be separately consented to
- Withdrawal must be accessible within the app (not only through OS settings)

### Italian Garante Guidelines on Cookies and Mobile (2021)

Extended cookie consent guidelines to mobile applications, confirming that:
- Device storage access via SDKs constitutes "cookie-like" technology under ePrivacy
- First-party analytics SDKs may still require consent depending on the data collected
- Cross-app tracking always requires explicit consent
