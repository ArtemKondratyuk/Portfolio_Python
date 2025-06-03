<a name="top"></a>

<div align="center">
  <h3 align="center"> File Renamer by Template</h3>

  <p align="center">
   A simple yet powerful script to rename your files in seconds — just set the template and go!
    <br />
    <br />
    <a href="#about-the-script">About The Script</a>  |
    <a href="#how-to-run">How to Run</a>  |
    <a href="#how-to-use">How to Use</a> |
    <a href= "#example">Example</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Script

This Python script helps you quickly rename all files in a selected folder using a template. 
You define the filename pattern, and the script numbers each file automatically.

Perfect for organizing photos, documents, or any set of files with a consistent naming scheme.

<p align="right"><a href="#top">Scroll up</a>

<!-- GETTING STARTED -->
## How to Run

1. Make sure Python 3 is installed.

2. Download rename_files.py.

3. Open a terminal or command prompt.

4. Run the script:

```
python rename_files.py
```

<br />

##  How to Use

When prompted:

  1. Select the folder where your files are located.

  2. Enter a filename template using # as placeholders for numbers.

<p align="right"><a href="#top">Scroll up</a>

## Example:

  ```
  photo_##.jpg
  ```
...your files will be renamed like this:

  ```
  photo_01.jpg  
  photo_02.jpg  
  photo_03.jpg  
  ```
You can use as many # as needed:

* file_####.txt → file_0001.txt, file_0002.txt, etc.

* image-## → image-01, image-02

<br />
If you don’t include a file extension in the template, the script will keep each file's original extension.

<p align="right"><a href="#top">Scroll up</a>

