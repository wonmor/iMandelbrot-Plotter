# iMandelbrot: An Interactive Module
**iMandelbrot** is a **learning aid** purely made out of **PyGame** that visualizes the nature of a **Mandelbrot** fractal!

![logo](https://user-images.githubusercontent.com/35755386/161361789-583ccb1e-7786-4b43-a7b3-f1d0503d7e75.png)

---

## Public Release 1.2.0
**Developed** and **Maintained** by **John Seong** • **MIT** License

[Download for **macOS**](https://github.com/wonmor/iMandelbrot-Plotter/raw/main/installer/iMandelbrot_Mac.dmg)

[Download for **Windows**](https://github.com/wonmor/iMandelbrot-Plotter/raw/main/installer/iMandelbrot_Windows.zip)

---

## Why Our Product Is Sexier Than Others

1. For the sake of **optimization**, **iMandelbrot** only generates the coordinates above the x-axis — basically duplicating to the corresponding coordinates below the horizontal line.
2. The user interface is very ***intuitive*** that even a kindergardener can immediately tell which is which — the program additionally displays what is going on **behind the scenes** to validate that the Mandelbrot set equation indeed works perfectly in real life.

<img width="800" alt="Screen Shot 2022-04-02 at 1 26 37 PM" src="https://user-images.githubusercontent.com/35755386/161394343-fbd4086c-8990-4091-a175-37a529f15bf5.png">

<img width="800" alt="Screen_Shot_2022-04-06_at_2 09 54_PM" src="https://user-images.githubusercontent.com/35755386/162040744-22220e57-149f-4706-a123-998801676992.png">

<p float="left">
  
  <img width="400" alt="Screen Shot 2022-04-03 at 8 03 51 PM" src="https://user-images.githubusercontent.com/35755386/161455118-ec4e5ec3-3572-448d-9ab1-d9beae77ab64.png">
  
  <img width="400" alt="Screen Shot 2022-04-02 at 12 36 55 AM" src="https://user-images.githubusercontent.com/35755386/161366481-94a21a58-4b4b-4c26-81f8-26fd9cd4a3c1.png">
</p>

---

## Dependencies
- **PyGame** Cross-Platform Set of Modules
- **PyObjC** Bidirectional Bridge *(Only if you would like to run on macOS)*

<img width="800" alt="Project Mockup" src="https://user-images.githubusercontent.com/35755386/162789619-dc009f44-5494-4983-9f96-26d2765991bb.jpg">

---

## How to Run

Either open one of the precompiled macOS or Windows setup utility in the ```installer``` folder, or go to the ```src``` folder and open the ```mandelbrot.py``` file directly.

---

## Version Guide

### **Alpha Release 0.1.0**

- [x] Create a class that plots the Mandelbrot fractal using the traditional method of plotting both over and under the x-axis

---

### **Public Release 1.0.0**

- [x] Add a console window that displays information regarding the equation and coordinates
- [x] Revamp the GUI and make it more visually appealing

---

### **Public Release 1.1.0**

- [x] Add a macOS installer for the sake of convenience
- [x] Improve the time complexity by only plotting the top half of the set and copying to the bottom

---

### **Public Release 1.2.0**

- [x] Add a Windows installer for users who are obsessed with Bill Gates' janky operating system
