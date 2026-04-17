# Tower of Hanoi – Visual ASCII Simulation

An interactive and visually enhanced implementation of the **Tower of Hanoi** problem using **Python**, featuring:

* 🎯 Recursive problem-solving
* 🔁 Iterative rendering (ASCII graphics)
* 🌈 Colored terminal visualization
* 🧠 Step-by-step execution clarity

---

## 📌 Overview

This project demonstrates the classic **Tower of Hanoi** problem using recursion, enhanced with a **real-time ASCII-based visualization** in the terminal.

Each move is clearly displayed with:

* Step number
* Disk movement description
* Animated tower state

---

## 🧠 Concepts Demonstrated

### 1. Recursion

The core logic uses recursion to break the problem into smaller subproblems:

* Move `n-1` disks to auxiliary rod
* Move the largest disk to target
* Move `n-1` disks to target

### 2. Iteration

Loops are used to:

* Render the towers visually
* Display each level of disks

---

## 🎮 Features

* 🌈 **Colored disks** using ANSI escape codes
* 🪜 **ASCII tower visualization**
* 📊 **Step counter for each move**
* ⚡ **Smooth animation using time delay**
* 🧾 **Clear step-by-step descriptions**

---

## 🖥️ Demo Output

```
==================================================
                    Step 3
==================================================

👉 Move disk 2 from A ➝ C

   *        |        |
  ***       |        |
 *****      |       ***
------------------------------
   A        B        C
```

---

## ⚙️ Requirements

* Python 3.x
* Terminal that supports ANSI colors (Mac/Linux/VS Code terminal recommended)

---

## 🚀 How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/tower-of-hanoi-demo.git
```

2. Navigate to the project folder:

```
cd tower-of-hanoi-demo
```

3. Run the program:

```
python hanoi.py
```

4. Enter number of disks (recommended: 3–5)

---

## 📂 Project Structure

```
tower-of-hanoi-demo/
│
├── hanoi.py        # Main program
├── README.md       # Documentation
```

---

## 📊 Example

For `n = 3`, total steps:

```
2^n - 1 = 7 steps
```

---

## 🎯 Learning Outcomes

* Understand recursion deeply
* Visualize algorithm execution
* Improve problem-solving approach
* Learn terminal-based UI representation

---

## 🔥 Why This Project?

This project goes beyond a basic algorithm implementation by:

* Adding **visual clarity**
* Improving **user experience**
* Demonstrating **clean coding practices**

---

## 📌 Future Improvements

* 🎨 Add more advanced animations
* 🎥 Export simulation as GIF
* 🌐 Web-based visualization (React / Canvas)
* 🎮 Interactive controls

---
