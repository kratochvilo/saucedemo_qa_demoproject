# Found Bugs Report

This document contains a list of bugs found during manual testing of the SauceDemo application.

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