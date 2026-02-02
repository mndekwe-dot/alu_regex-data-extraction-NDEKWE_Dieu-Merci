# 🏫 School Management System - Data Extraction

**ALU Regex Data Extraction Assignment**  
A security-aware text processing system for extracting student records, fee information, and schedule data from school registration forms.

---

## 📌 What I Did

Built a **regex-based data extraction tool** for a school management system that:

1. **Extracts 7 data types** from school forms:
   - Emails (student, parent, staff)
   - Phone numbers (Rwanda format only)
   - URLs (school portals, online classrooms)
   - Credit cards (fee payments)
   - Time schedules (class times, meetings)
   - Currency (school fees in RWF)
   - Hashtags (events, campaigns)

2. **Validates input for security**:
   - Rejects malicious patterns (XSS, SQL injection)
   - Enforces size limits (prevents DoS attacks)
   - Masks sensitive data (emails, cards, phones)

3. **Handles real-world variations**:
   - Different spacing and punctuation
   - Mixed formats (12h/24h time, card separators)
   - Case-insensitive matching

4. **Generates structured output**:
   - JSON format with metadata
   - Privacy-protected results
   - Timestamp and summary statistics

---

## ⚠️ CRITICAL FORMAT REQUIREMENTS

### 📱 Phone Numbers (Rwanda Only)
```
✅ VALID:
- 0788123456  (MTN - starts with 078)
- 0721234567  (Airtel - starts with 072)
- 0739123456  (Airtel - starts with 073)

❌ INVALID:
- 0777123456  (Wrong prefix)
- +250788123456  (Country code not supported)
- 0788 123 456  (Spaces not allowed)
```

**Pattern:** `\b07[89]\d{7}\b`  
**Must** start with `078` (MTN) or `079` (Airtel), exactly 10 digits.

### 💰 Currency (Rwanda Francs)
```
✅ VALID:
- RWF 50,000
- RF 125,000.00
- rwf 1,000 (case-insensitive)

❌ INVALID:
- 50,000 RWF (Currency code must come first)
- 50000 (Missing RWF/RF prefix)
- $50,000 (Wrong currency)
```

**Pattern:** `(?i)(?:RWF|RF)\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})?`  
**Must** start with `RWF` or `RF`, supports comma-separated thousands.

---

## 🚀 Usage

### Run the Main Program
```bash
python school_data_extraction.py
```
Paste school data, type `END` when finished.

### Instructor Testing Interface
```bash
python instructor_test_interface.py
```
Two modes:
1. **Quick Test** - Test individual patterns
2. **Form Test** - Fill complete registration form

---

## 📁 Files Included

| File | Purpose |
|------|---------|
| `school_data_extraction.py` | Main extraction program |
| `student_sample.txt` | Basic test data |
| `instructor_sample.txt` | Comprehensive test scenarios (11 scenarios)(Customizedable) |
| `school_output.json` | Sample output |
| `README.md` | This file |

---

## 🔒 Security Features

### Input Validation
- Size limit: 50,000 characters
- Scans for: `<script>`, `javascript:`, `DROP TABLE`, `eval()`, `../`
- Rejects malicious input immediately

### Data Privacy
All sensitive data is masked in output:

| Original | Masked |
|----------|--------|
| `student@example.com` | `st***@example.com` |
| `1234-5678-9012-3456` | `****-****-****-3456` |
| `0788123456` | `078***3456` |

---

## 📝 Test Scenarios Included

1. Student registration forms
2. Fee collection reports
3. Parent communications
4. Mixed format edge cases
5. Security attack attempts (rejected)
6. School event announcements
7. Teacher schedules
8. Realistic data entry
9. Graduation information
10. Phone number edge cases
11. Currency format edge cases

---

## 🎯 Key Technical Implementations

### Regex Patterns
- **Email:** Standard RFC 5322 format
- **Phone:** Rwanda-specific `07[2389]\d{7}`
- **URL:** HTTP/HTTPS with paths
- **Card:** 16-digit with flexible separators
- **Time:** Both 12h and 24h formats
- **Currency:** RWF/RF prefix required
- **Hashtag:** Alphanumeric + underscore

### Security
- Pattern-based malicious input detection
- Input sanitization
- Sensitive data masking
- Error handling for edge cases

---

## 👨‍💻 Author

**[NDEKWE Dieu Merci]**  
ALU - Junior Frontend Developer Program  
Regex Data Extraction Assignment - 2025

---

## 📞 Contact

For questions about this implementation:
- Email: [m.ndekwe@alustudent.com]
- Repository: [https://github.com/mndekwe-dot/alu_regex-data-extraction-NDEKWE_Dieu-Merci]

---

**⚠️ Remember:**
- Phone numbers **MUST** start with `078` or `079`
- Currency **MUST** start with `RWF` or `RF`
- All dangerous patterns are rejected automatically
- Sensitive data is always masked in output