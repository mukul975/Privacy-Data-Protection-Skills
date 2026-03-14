# Children's Privacy Notice Workflows

## Workflow 1: Privacy Notice Development Process

```
New or updated service requiring children's privacy notice
│
├─ Step 1: Determine audience segments
│  ├─ Identify age groups likely to use the service
│  ├─ Segment into notice tiers:
│  │  ├─ Tier 1: Under 8 (pre-literate / early readers)
│  │  ├─ Tier 2: 8-11 (primary school)
│  │  ├─ Tier 3: 12-15 (secondary school)
│  │  ├─ Tier 4: 16-17 (young adults)
│  │  └─ Tier P: Parents/guardians (full legal notice)
│  │
│  └─ Determine which tiers are required based on service audience
│
├─ Step 2: Content inventory per Art. 13
│  ├─ For each Art. 13 element, draft content at each tier:
│  │  ├─ Controller identity (13(1)(a)): child-friendly and full legal versions
│  │  ├─ DPO contact (13(1)(b)): "If you're worried, tell your parent" (child) / full details (parent)
│  │  ├─ Purposes (13(1)(c)): plain language per tier
│  │  ├─ Lawful basis (13(1)(c)): omit for under-12 / simplified for 12-15 / included for parents
│  │  ├─ Recipients (13(1)(e)): "only you and your parent" (child) / named recipients (parent)
│  │  ├─ Retention (13(2)(a)): "while you have an account" (child) / specific periods (parent)
│  │  ├─ Rights (13(2)(b)): age-appropriate descriptions
│  │  ├─ Withdrawal (13(2)(c)): practical instructions per tier
│  │  ├─ Complaint (13(2)(d)): "tell your parent" (child) / SA details (parent)
│  │  └─ Automated decisions (13(2)(f)): concrete explanation if applicable
│  │
│  └─ Ensure no mandatory element is omitted from the parent notice
│
├─ Step 3: Design and format
│  ├─ Tier 1 (Under 8):
│  │  ├─ Illustrated walkthrough with character guide
│  │  ├─ Maximum 5-7 words per frame
│  │  ├─ Animated or interactive format
│  │  └─ Audio narration option
│  │
│  ├─ Tier 2 (8-11):
│  │  ├─ Illustrated text with icons per section
│  │  ├─ Short paragraphs (2-3 sentences)
│  │  ├─ Interactive expandable sections
│  │  └─ Quiz element for comprehension check
│  │
│  ├─ Tier 3 (12-15):
│  │  ├─ Layered summary + expandable detail
│  │  ├─ Key facts table at top
│  │  ├─ Infographics for data flow
│  │  └─ Privacy settings controls embedded
│  │
│  ├─ Tier 4 (16-17):
│  │  ├─ Plain language standard notice
│  │  ├─ Glossary for technical terms
│  │  └─ Direct links to privacy controls
│  │
│  └─ Tier P (Parents):
│     ├─ Full Art. 13 legal notice
│     ├─ PDF downloadable format
│     └─ Parental dashboard access instructions
│
├─ Step 4: Readability testing
│  ├─ Run automated readability analysis:
│  │  ├─ Flesch-Kincaid Grade Level
│  │  ├─ Flesch Reading Ease
│  │  ├─ Gunning Fog Index
│  │  └─ Average sentence length and passive voice percentage
│  │
│  ├─ Compare against targets:
│  │  ├─ Tier 1: FK Grade 1, FRE 90+
│  │  ├─ Tier 2: FK Grade 4, FRE 80+
│  │  ├─ Tier 3: FK Grade 8, FRE 60+
│  │  ├─ Tier 4: FK Grade 10, FRE 50+
│  │  └─ Tier P: FK Grade 12, FRE 40+ (acceptable for legal audience)
│  │
│  └─ Revise content until targets are met
│
├─ Step 5: User testing with children
│  ├─ Recruit 10+ children per tier from the target age range
│  ├─ Conduct comprehension test:
│  │  ├─ "In your own words, what information does [Service] collect about you?"
│  │  ├─ "Why does [Service] collect your information?"
│  │  ├─ "Who can see your information?"
│  │  ├─ "What can you do if you want to delete your information?"
│  │  └─ Target: 80% correct answers
│  │
│  ├─ Conduct findability test:
│  │  ├─ "Can you find how to delete your account?"
│  │  ├─ "Can you find out who to contact if you're worried?"
│  │  └─ Target: 90% find answer within 30 seconds
│  │
│  ├─ Collect feedback on emotional response:
│  │  ├─ "How does this notice make you feel?"
│  │  ├─ "Do you feel like you understand what happens with your information?"
│  │  └─ Target: children report feeling informed and in control
│  │
│  └─ Revise based on testing outcomes
│
├─ Step 6: Legal review
│  ├─ DPO verifies all Art. 13 elements are covered across all tiers
│  ├─ Legal counsel confirms parent notice meets full legal requirements
│  ├─ Confirm COPPA Section 312.4 compliance (if US-applicable)
│  └─ Confirm UK AADC Standard 4 compliance
│
├─ Step 7: Publication
│  ├─ Version number and date assigned
│  ├─ Notice deployed across all platforms (web, app, email)
│  ├─ Just-in-time notices configured at each collection point
│  ├─ Parent notice sent as part of parental consent flow
│  └─ Accessibility: screen reader compatible, alt text for images, sufficient contrast
│
└─ Step 8: Ongoing review
   ├─ Review notice quarterly for accuracy
   ├─ Update when processing activities change
   ├─ Re-test with children annually
   └─ Maintain version history
```

## Workflow 2: Just-in-Time Notice Implementation

```
Data collection point identified in the service
│
├─ Determine what data is collected at this point
│  ├─ Data element(s): [list]
│  ├─ Purpose(s): [list]
│  └─ Is this a new collection the user has not been informed about? [Y/N]
│
├─ If new collection → Design just-in-time notice:
│  ├─ Maximum 2 sentences
│  ├─ State: what is collected, why, who sees it
│  ├─ Include [Learn more] link to full notice section
│  ├─ Use age-appropriate language for the user's tier
│  └─ Display without requiring user action to dismiss
│
├─ Display notice:
│  ├─ Position: directly above or adjacent to the collection point
│  ├─ Visibility: visible without scrolling
│  ├─ Timing: before the user provides data (not after)
│  └─ Persistence: remains visible until the user takes action
│
└─ Example notices by tier:
   ├─ Under 8: [Icon: camera] "We'll save your drawing so you can find it later!"
   ├─ 8-11: "We save your quiz answers so you can see how you improve over time. Only you and your parent can see them."
   ├─ 12-15: "Your progress data is saved to personalise your learning path. You can download or delete it from your privacy settings."
   └─ 16-17: "We process your assessment results to adapt content difficulty. Legal basis: consent (Art. 6(1)(a) via parental authorisation). Manage in Privacy Centre."
```

## Workflow 3: Privacy Notice Change Management

```
Material change to data processing practices
│
├─ Step 1: Assess materiality
│  ├─ Is the change likely to affect children's expectations? [Y/N]
│  ├─ Does it involve new data collection? [Y/N]
│  ├─ Does it change who can see children's data? [Y/N]
│  ├─ Does it change how long data is retained? [Y/N]
│  ├─ Does it introduce new profiling or automated decisions? [Y/N]
│  │
│  ├─ If ANY YES → Material change. Update notice. Notify users.
│  └─ If ALL NO → Minor change. Update notice. No user notification needed.
│
├─ Step 2: Update notice content
│  ├─ Draft updated content for each affected tier
│  ├─ Run readability analysis
│  ├─ Highlight what has changed (use "What's new" or change summary)
│  └─ Legal review and DPO sign-off
│
├─ Step 3: Notify users (material changes only)
│  ├─ In-app notification to children (age-appropriate):
│  │  "We've updated how we use your information. Here's what changed: [summary]"
│  ├─ Email to parents:
│  │  "We've updated our privacy notice for [Service]. Here's what changed and why."
│  ├─ Provide 30-day notice period before changes take effect
│  └─ If consent is the lawful basis and the change is material to consent:
│     obtain fresh consent before implementing changes
│
├─ Step 4: Publish updated notice
│  ├─ Increment version number
│  ├─ Update date
│  ├─ Archive previous version (accessible for reference)
│  └─ Update consent text version hash in consent records
│
└─ Step 5: Record the change
   ├─ Document: what changed, why, when, who approved
   ├─ Record notification method and reach
   └─ File in compliance records
```
