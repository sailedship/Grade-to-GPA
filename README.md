# 🎓 GPA Calculator

This is a simple Python script that allows users to convert their **letter grades** or **percentages** into a **GPA**.

---

## 💡 Features

* Convert **letter grades** (e.g., A+, B-) into GPA values.
* Convert **percentage scores** into GPA based on a user-defined scale (e.g., out of 4 or 5).
* Supports GPA scales like 4.0 or 5.0 depending on your academic system.

---

## 🚀 How to Use

1. Run the script:

   ```bash
   python GPA_calculator.py
   ```

2. You'll be asked:

   ```
   Enter your grade in the form of a capital letter. e.g. (A+, B- etc. Type N to convert a percentage instead.)
   ```

3. Choose either:

   * A letter grade (e.g., `B+`, `A-`, `F`, etc.)
   * Or type `N` if you want to convert a **percentage** to GPA.

---

## 🧠 Examples

### 1. Letter Grade Input

```
Enter your grade: B+
Output: 3.3
```

### 2. Percentage Input

```
Enter your grade: N
What is the highest achievable GPA? e.g 4 or 5: 4
What percentage did you get? Do not type symbols, only numbers: 80
Output: 3.2
```

---

## ⚠️ Notes

* Input **must be capital letters** for letter grades (e.g., `A-`, not `a-`).
* The script **does not handle invalid input** — future versions may include input validation.
* Percentage conversion assumes linear scaling (e.g., 80% of a 4.0 scale gives 3.2 GPA).

---

## 🛠️ Requirements

* Python 3.x

---

## 📌 Future Improvements

* Add error handling for incorrect inputs.
* Support lowercase inputs.
* Add GUI support or web-based version.

---

## 📄 License

Do whatever you want

---
