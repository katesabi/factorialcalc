🧮 factorial calculator  

a minimalist desktop app that calculates factorials with a sleek black-and-white design. 🌑✨  

🔢 what it does:  
- asks the user to enter a positive integer  
- calculates the factorial using python’s math library  
- shows the result right in the app  
- handles errors for non-numeric or negative inputs  
- keeps a history of recent calculations (up to 50 entries)  
- adds a timestamp to every history entry (yyyy-mm-dd hh:mm:ss)  
- lets you clear the history or export it to a .txt file  

🎨 design notes:  
- fullscreen mode on launch for an immersive feel  
- dark theme with crisp white text and subtle accents  
- clean layout, no clutter, just the essentials  
- escape key to exit fullscreen  

🛠️ tech stack:  
- python 3  
- tkinter for the gui  
- math for factorial calculations  
- datetime for timestamps  
- filedialog for file exports  

🚀 how to run:  
1. make sure you have python 3 installed  
2. save the code as factorial_calculator.py  
3. run it with: python factorial_calculator.py  

💡 tips:  
- very large factorials are shortened in the ui to keep things readable  
- history is stored in memory and lost when you close the app (that’s why exporting is handy)  

📂 files:  
- factorial_calculator.py – main application code  
- (optional) history.txt – exported calculation history 
