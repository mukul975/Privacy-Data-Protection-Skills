# Age Verification Methods Workflows

## Workflow 1: Age Assurance Method Selection

```
Service requires age assurance for child protection
│
├─ Step 1: Classify service risk level
│  ├─ HIGH RISK: Age-restricted content, social features with strangers,
│  │   direct messaging, user-generated content visible to public,
│  │   monetisation features, special category data
│  │
│  ├─ MEDIUM RISK: Content personalisation, in-app purchases,
│  │   community features with moderation, educational services,
│  │   interactive features with known users
│  │
│  └─ LOW RISK: Static content, informational, no social features,
│     no data sharing, no profiling, single-player
│
├─ Step 2: Select minimum verification level
│  ├─ HIGH RISK → Document-based OR facial estimation + liveness
│  │   Recommended: document-based with digital identity as alternative
│  │
│  ├─ MEDIUM RISK → Facial age estimation (on-device) OR
│  │   self-declaration + risk signals
│  │   Recommended: facial estimation with escalation path
│  │
│  └─ LOW RISK → Self-declaration + neutral prompt
│     Recommended: self-declaration with cookie-based re-entry detection
│
├─ Step 3: Proportionality assessment
│  ├─ Is the selected method necessary to protect children? [Document]
│  ├─ Could a less intrusive method achieve same protection? [Document]
│  ├─ What safeguards minimise the privacy impact? [Document]
│  ├─ How does it handle accessibility? [Document]
│  └─ DPIA required for the age assurance processing itself? [Assess]
│
├─ Step 4: Implementation
│  ├─ Select technology provider (or build in-house)
│  ├─ Integrate into user registration/access flow
│  ├─ Test with users in target age groups
│  ├─ Configure data retention (delete verification data immediately after use)
│  └─ Deploy with monitoring
│
└─ Document selection rationale and DPIA outcome
```

## Workflow 2: Self-Declaration Age Screening

```
User accesses service requiring age screening
│
├─ Display neutral age prompt:
│  "Enter your date of birth" [scrollable date picker]
│  - No default date selected
│  - No indication of threshold age
│  - No age-related messaging ("must be 13+")
│
├─ User enters date of birth
│
├─ Calculate age from DOB
│
├─ Apply jurisdiction-specific threshold
│  (determined by user's declared country or IP geolocation)
│
├─ Age >= threshold?
│  ├─ YES → Allow access; route to standard registration
│  └─ NO → Route to child experience or parental consent flow
│
├─ Anti-circumvention measures:
│  ├─ Set persistent cookie recording the age gate attempt
│  ├─ If user re-attempts within 24 hours: present same DOB result
│  ├─ If user clears cookies and re-attempts: device fingerprint check
│  ├─ If DOB results in age exactly at threshold: flag for review
│  └─ Log all age gate attempts for anomaly detection
│
└─ Log age screening result (DOB hash, threshold applied, outcome, timestamp)
```

## Workflow 3: Facial Age Estimation

```
Service implements facial age estimation (medium/high risk)
│
├─ Step 1: User consent
│  ├─ Display notice: "We'd like to estimate your age using your camera.
│  │   We don't store your photo — it's processed on your device and deleted immediately."
│  ├─ User consents [Proceed] or declines [Offer alternative method]
│  └─ If declined: offer document-based verification or parental confirmation
│
├─ Step 2: Image capture
│  ├─ Activate device front-facing camera
│  ├─ Guide user to position face in frame
│  ├─ Capture single frame
│  └─ Perform liveness check (blink detection, head movement) to prevent spoofing
│
├─ Step 3: On-device processing
│  ├─ Run age estimation ML model locally on device
│  ├─ Model outputs: estimated age ± confidence interval
│  │   Example: "Estimated age: 14, confidence interval: 12-16 (95%)"
│  ├─ Delete facial image from device memory immediately after processing
│  └─ No image data transmitted to server
│
├─ Step 4: Age determination
│  ├─ Apply threshold with confidence buffer:
│  │   - If lower bound of confidence interval >= threshold: user is over threshold
│  │   - If upper bound of confidence interval < threshold: user is under threshold
│  │   - If threshold falls within confidence interval: UNCERTAIN
│  │
│  ├─ OVER threshold → Allow standard access
│  ├─ UNDER threshold → Route to child experience or parental consent
│  └─ UNCERTAIN → Escalate to higher-assurance method:
│     ├─ Document-based verification
│     ├─ Digital identity verification
│     └─ Or treat as under-threshold (conservative approach)
│
├─ Step 5: Record result
│  ├─ Record: binary age category (over/under threshold), timestamp, method used
│  ├─ Do NOT record: facial image, estimated exact age, confidence interval
│  └─ Retain result for session or account duration only
│
└─ Step 6: Audit
   ├─ Monthly accuracy audit against known-age test accounts
   ├─ Quarterly bias audit across demographic groups
   └─ Annual provider audit for data protection compliance
```

## Workflow 4: Document-Based Age Verification

```
High-risk service requires document-based age verification
│
├─ Step 1: Document selection
│  ├─ Present accepted document types:
│  │  ├─ Passport (any country)
│  │  ├─ National ID card (EU/EEA countries)
│  │  ├─ Driver's licence (with photo)
│  │  └─ Residence permit (with photo and DOB)
│  └─ User selects document type
│
├─ Step 2: Document capture
│  ├─ Guide user to photograph/scan document
│  ├─ Quality check: resolution, lighting, completeness
│  ├─ If NFC-enabled device and ePassport: offer NFC chip reading
│  └─ Capture front (and back if applicable)
│
├─ Step 3: Document verification
│  ├─ OCR extraction of date of birth and document details
│  ├─ MRZ validation (for passports and ID cards)
│  ├─ Document authenticity checks (security features, template matching)
│  ├─ Optional: NFC chip verification (highest assurance)
│  └─ Optional: liveness check (selfie compared to document photo)
│
├─ Step 4: Age calculation
│  ├─ Extract date of birth from verified document
│  ├─ Calculate age
│  ├─ Apply threshold determination
│  └─ Record binary result (over/under threshold)
│
├─ Step 5: Data minimisation
│  ├─ IMMEDIATELY DELETE: full document image, OCR-extracted text (name, address, ID number)
│  ├─ RETAIN ONLY: binary age verification result, document type, verification timestamp
│  ├─ Maximum retention of verification result: account duration
│  └─ No full identity data retained by the service
│
└─ Step 6: Fallback
   ├─ If document verification fails: offer retry (max 3 attempts)
   ├─ If all retries fail: offer alternative method (facial estimation, digital identity)
   └─ If no alternative available: deny access to age-restricted features
```

## Workflow 5: Digital Identity Verification

```
Service implements digital identity age verification
│
├─ Step 1: Identity provider selection
│  ├─ Present available identity providers:
│  │  ├─ EU Digital Identity Wallet (when available)
│  │  ├─ National eID (eIDAS-notified: Swedish BankID, Belgian eID, etc.)
│  │  ├─ UK DIATF-certified providers
│  │  ├─ Open Banking identity verification
│  │  └─ Mobile Network Operator verification
│  │
│  └─ User selects provider
│
├─ Step 2: Redirect to identity provider
│  ├─ Service sends OIDC4IDA request for age attribute only
│  ├─ Request specifies: "is_over_[threshold]" (not full identity)
│  ├─ User authenticates with identity provider (PIN, biometric, etc.)
│  └─ Identity provider verifies age from underlying identity data
│
├─ Step 3: Receive attestation
│  ├─ Identity provider returns signed assertion:
│  │  { "is_over_18": true } or { "age_bracket": "13-17" }
│  ├─ Service validates the assertion signature
│  ├─ Service does NOT receive: name, address, ID number, photo
│  └─ Double-blind: identity provider does not know which service was accessed
│
├─ Step 4: Apply age determination
│  ├─ Map attestation to service's age tiers
│  ├─ Route user to appropriate experience
│  └─ Record verification outcome (method, timestamp, result)
│
└─ Step 5: Privacy assurance
   ├─ No identity data stored by the service
   ├─ No service identity disclosed to the identity provider
   ├─ Attestation token retained only for session or account duration
   └─ User can re-verify at any time if they wish to change providers
```
