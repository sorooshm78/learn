The `diff` command is a powerful tool in Unix and Linux systems used to compare files line by line. It helps you find the differences between two files or directories. Here's a basic guide to using the `diff` command:

### Basic Syntax:
```
diff [options] file1 file2
```

### Common Usage:

1. **Compare Two Files:**
   ```
   diff file1.txt file2.txt
   ```
   This will output the differences between the two files line by line.

2. **Output Format:**
   The typical output looks like this:
   ```
   3c3
   < line from file1
   ---
   > line from file2
   ```
   - `3c3` means change on line 3.
   - `<` indicates the content in `file1`.
   - `>` indicates the content in `file2`.
   - The `---` separates the differences between the files.

3. **Unified Format (`-u`):**
   The `-u` (unified) option shows changes in a more concise format:
   ```
   diff -u file1.txt file2.txt
   ```
   Example output:
   ```
   @@ -1,3 +1,3 @@
   -line from file1
   +line from file2
   ```
   - `@@ -1,3 +1,3 @@` tells which lines are affected in the files.
   - Lines starting with `-` are from `file1`.
   - Lines starting with `+` are from `file2`.

4. **Side-by-Side Comparison (`-y`):**
   The `-y` option gives a side-by-side comparison:
   ```
   diff -y file1.txt file2.txt
   ```
   Example output:
   ```
   line 1 from file1   | line 1 from file2
   line 2 from file1     line 2 from file2
   ```

5. **Ignore White Space Changes (`-w`):**
   If you want to ignore differences in white spaces (tabs, spaces):
   ```
   diff -w file1.txt file2.txt
   ```

6. **Compare Directories:**
   To compare all files in two directories:
   ```
   diff -r dir1/ dir2/
   ```
   The `-r` option enables recursive comparison of subdirectories.

7. **Only Show if Files Differ (`-q`):**
   To simply check if the files are different, without showing details:
   ```
   diff -q file1.txt file2.txt
   ```

### Useful Options:

- `-i`: Ignore case differences.
- `-B`: Ignore blank lines.
- `--suppress-common-lines`: Used with `-y`, it only shows differences.

### Example:
Let's say you have two files: `file1.txt` and `file2.txt`.

#### file1.txt:
```
Hello
This is file one.
Goodbye
```

#### file2.txt:
```
Hello
This is file two.
Goodbye!
```

Command:
```
diff file1.txt file2.txt
```

Output:
```
2c2
< This is file one.
---
> This is file two.
3c3
< Goodbye
---
> Goodbye!
```

This output tells us that line 2 is different in both files, and line 3 has been slightly modified.

---

Let me know if you'd like to dive deeper into any specific `diff` options or use cases!