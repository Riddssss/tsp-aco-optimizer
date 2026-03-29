# TSP Route Optimizer using Ant Colony Optimization

## Overview
This project solves the Traveling Salesman Problem (TSP) using Ant Colony Optimization (ACO).

Two algorithms are implemented:
- Ant System (AS)
- Max-Min Ant System (MMAS)

A simple web interface is used to run both algorithms and visualize the results.

---

## Features
- Compare Ant System and Max-Min AS
- Displays shortest path (tour)
- Shows total distance
- Highlights the better algorithm
- Graph visualization with nodes and arrows
- Simple animation of traversal

---

## Tech Stack
- Frontend: React, Vite, Tailwind CSS
- Backend: Flask (Python)
- Visualization: react-konva

---

## Project Structure
TSP-ACO-Project  
├── backend  
├── frontend  
└── README.md  

---

## How to Run

### Backend
cd backend  
pip install -r requirements.txt  
python app.py  

### Frontend
cd frontend  
npm install  
npm run dev  

Open in browser:  
http://localhost:5173  

---

## Output
- Shows optimized route  
- Displays distance  
- Compares both algorithms  
- Visual graph with direction  

---

## Basic Idea
Ant Colony Optimization is inspired by how ants find the shortest path using pheromones.

- Ant System uses all ants to update paths  
- Max-Min AS limits pheromone values to improve performance  

---

## Conclusion
This project helped in understanding optimization algorithms and how they can be visualized using a web-based interface.

---

## Author
Riddhima Shah
