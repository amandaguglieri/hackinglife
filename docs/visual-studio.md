

## Compiling C/C++ Code Using `cl.exe` in Visual Studio 2019

### **Steps to Compile a C/C++ Program**

#### **1. Open the Developer Command Prompt for VS 2019**
- Click **Start** and search for **"Developer Command Prompt for VS 2019"**.
- Open it.

#### **2. Navigate to Your Source Code Directory**
```sh
cd path\to\your\source\code
```

#### **3. Compile a Single C/C++ File**
- **For a C file:**
  ```sh
  cl /EHsc my_program.c
  ```
- **For a C++ file:**
  ```sh
  cl /EHsc my_program.cpp
  ```
- If the compilation is successful, an **executable (.exe) file** will be generated.

#### **4. Compile Multiple Files**
```sh
cl /EHsc file1.cpp file2.cpp
```
- This will produce an `a.exe` (default name) or `file1.exe` (if `file1.cpp` contains `main()`).

#### **5. Specify an Output Executable Name**
```sh
cl /EHsc my_program.cpp /Feoutput_name.exe
```

#### **6. Run the Compiled Executable**
```sh
output_name.exe
```

---

## **Additional Compiler Options**

### **Enable Optimization (`/O2`)**
```sh
cl /EHsc /O2 my_program.cpp
```

### **Enable Debugging (`/Zi`)**
```sh
cl /EHsc /Zi my_program.cpp
```

### **Compile Without Linking (`/c`)**
```sh
cl /EHsc /c my_program.cpp
```
- This creates an `.obj` file without producing an `.exe`.

### **Link Multiple Object Files**
```sh
link file1.obj file2.obj /OUT:final_program.exe
```

---

**Happy Coding! 🚀**
