# Found Bugs Report

This document contains a list of bugs found during exploratory testing of the SauceDemo application.

## 📋 Legend and Definitions

To ensure consistency, we use the following definitions for bug Severity and Status.

### Severity
Determines how significantly the bug impacts the application's functionality from a user perspective.

| Value | Description | Example |
| :--- | :--- | :--- |
| **Critical** | Application crashes, data loss, or the main process (e.g., Checkout) cannot be completed. No workaround available. | Clicking "Finish" causes the app to crash (Error 500). |
| **High** | Important functionality is malfunctioning, but a difficult workaround exists. | Filtering items by price does not work correctly. |
| **Medium** | Minor functional error that does not block the main process. | The "Back" button on the product detail page requires a double-click to work. |
| **Low** | Cosmetic issue, typo, UI misalignment. No impact on functionality. | Typo in the product description, wrong button color. |

### Status
Current state of the bug in the lifecycle.

| Value | Description |
| :--- | :--- |
| **Open** | The bug has been reported and is waiting for verification or assignment. |
| **In Progress**| A developer is currently working on the fix. |
| **Fixed** | The developer has marked the bug as fixed (waiting for re-test by QA). |
| **Closed** | QA has verified the fix works, and the issue is closed. |

---

## 1. Login Error Message Text Clipping
**ID:** BUG_UI_01
**Severity:** Low (Visual)
**Status:** Open
**Date Found:** 2023-10-27

**Description:**
The error message text overlaps the container boundaries when displayed on the screen. The text appears vertically aligned improperly, causing the top and bottom lines to be partially cut off by the red container box.

**Steps to Reproduce:**
1. Navigate to `https://www.saucedemo.com/`.
2. Enter a valid username (e.g., `standard_user`) into the "Username" field.
3. Enter an incorrect password (e.g., `wrong_pass`) into the "Password" field.
4. Click the "Login" button.

**Expected Result:**
The error message should be fully contained within the red alert box with appropriate padding, ensuring the text is fully legible. 

**Actual Result:**
An error message appears in a red box. The text is wrapped into 3 lines, but the font size or line height causes the text to exceed the box boundaries, making it difficult to read (clipping occurs at top/bottom).


### 2. Item Description Text

**ID:** BUG_UI_02
**Severity:** Low (Visual)
**Status:** Open
**Date Found:** 2023-12-16

**Description:**
The description for the item "Sauce Labs Backpack" contains text that appears to be an internal function call or placeholder (`carry.allTheThings()`) instead of standard descriptive text.

**Steps to Reproduce:**
1. Navigate to `https://www.saucedemo.com/`.
2. Log in with valid credentials (e.g., `standard_user`).
3. Observe the description text for the first item "Sauce Labs Backpack" on the inventory page.

**Expected Result:**
The description should contain grammatically correct text describing the product features, without any visible code snippets.

**Actual Result:**
The description text starts with a code-like string: `carry.allTheThings() with the sleek...`.

**Evidence:**
*(See attached screenshot: assets/bug_backpack_text.png)*