# Simplify Path Variant

## Question
You are provided with an absolute path representing the current working directory ``cwd`` in a Unix-style file system.  Additionally, you are given a relative path, devoted as ``cd``, which instructs a change to the current
working directory.  Your task is to determine and output the **simplified canonical path** that results from applying the relative path, ``cd``, to the initial cwd.  

Return the **simplified canonical path**.  

## Examples

### Example 1:
  Input: cwd = "/a/b/c", cd = "/d/./e"
  Output: "/d/e"

### Example 2:
  Input: cwd = "", cd = "/d/./e"
  Output: "/d/e"

### Example 3:
  Input: cwd = "/a/b/c", cd = ""
  Output: "/a/b/c"  

### Example 4:
  Input: cwd = "/a/b", cd = ".//c/../../d/f"
  Output: "/a/d/f"  
