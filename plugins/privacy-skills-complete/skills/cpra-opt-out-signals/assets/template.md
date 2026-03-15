# GPC Implementation Technical Specification

## Server-Side Middleware Configuration

### Nginx Example

```nginx
# Detect GPC header and set variable for downstream processing
map $http_sec_gpc $gpc_opt_out {
    "1"     "true";
    default "false";
}

# Pass GPC status to application
location / {
    proxy_set_header X-GPC-Opt-Out $gpc_opt_out;
    proxy_pass http://upstream;
}
```

### Application Middleware (Python/Flask)

```python
from functools import wraps
from flask import request, g

def detect_gpc(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        gpc_header = request.headers.get("Sec-GPC", "0")
        g.gpc_opt_out = gpc_header == "1"
        if g.gpc_opt_out:
            g.sale_sharing_consent = False
            # Log detection for compliance audit
            log_gpc_detection(
                timestamp=datetime.utcnow().isoformat(),
                authenticated=current_user.is_authenticated if hasattr(current_user, 'is_authenticated') else False,
                consumer_id=getattr(current_user, 'id', None),
            )
        return f(*args, **kwargs)
    return decorated_function
```

## Client-Side Detection (JavaScript)

```javascript
(function() {
    'use strict';

    // Detect GPC before loading ANY third-party scripts
    var gpcEnabled = navigator.globalPrivacyControl === true;

    if (gpcEnabled) {
        // Set consent state to opted-out
        window.__meridian_privacy = window.__meridian_privacy || {};
        window.__meridian_privacy.saleSharing = 'opted_out';
        window.__meridian_privacy.gpcDetected = true;

        // Block third-party tracking scripts
        // This must execute before any tag manager or advertising scripts load
        window.__meridian_privacy.blockTracking = true;

        // Log for compliance
        fetch('/api/privacy/gpc-detection', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                gpc: true,
                timestamp: new Date().toISOString(),
                userAgent: navigator.userAgent
            })
        }).catch(function() {
            // Silent fail - do not block page load
        });
    }
})();
```

## CMP Integration Configuration

### OneTrust Example

```json
{
    "gpc_settings": {
        "honor_gpc": true,
        "gpc_applies_to": ["sale_of_data", "sharing_for_cross_context_advertising"],
        "conflict_resolution": "gpc_takes_precedence",
        "notify_on_conflict": true,
        "notification_text": "Your browser is sending a Global Privacy Control signal. We have applied this as an opt-out of the sale and sharing of your personal information."
    }
}
```

## Compliance Verification Script

Run this monthly to verify GPC handling:

```bash
# Test 1: Server-side GPC detection
curl -s -o /dev/null -w "%{http_code}" \
  -H "Sec-GPC: 1" \
  https://app.meridiananalytics.co.uk/ \
  | grep 200

# Test 2: Verify no tracking cookies set with GPC
curl -s -c cookies.txt \
  -H "Sec-GPC: 1" \
  https://app.meridiananalytics.co.uk/ && \
  grep -c "_fbp\|_gcl_au\|IDE" cookies.txt | grep 0

echo "GPC compliance tests complete"
```
