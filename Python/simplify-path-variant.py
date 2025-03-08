class Solution:
    def simplifyPathVariant(self, cwd: str, cd: str) -> str:
      if not cd:
        return cwd
      if cd.startswith("/"):
        cwd = ""
      cwd_tokens = cd.split("/")
      tokens = [token for token in cwd_tokens if token]

      for token in cd.split("/"):
        if not token:
            continue
        if token == '.':
            continue
        if token == '..':
            if tokens:
                tokens.pop()
        else:
            tokens.append(token)

      if not tokens:
          return "/"

      result = "/" + "/".join(tokens)
      return result


def test_simplifyPathVariant():
    cwd = "/a/b/c", 
    cd = "/d/./e"  
    assert Solution().simplifyPathVariant(cwd, cd) == "/d/e"

    cwd = ""
    cd = "/d/./e" 
    assert Solution().simplifyPathVariant(cwd, cd)== "/d/e"

    cwd = "/a/b/c"
    cd = "" 
    assert Solution().simplifyPathVariant(cwd, cd)== "/a/b/c"

    cwd = "/a/b"
    cd = ".//c/../../d/f"
    assert Solution().simplifyPathVariant(cwd, cd) == "/a/d/f"
