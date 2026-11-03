def wildCardRec(txt, pat, n, m):
    
    # Empty pattern can match with an empty text only
    if m == 0:
        return n == 0

    # Empty text can match with a pattern consisting
    # of '*' only.
    if n == 0:
        for i in range(m):
            if pat[i] != '*':
                return False
        return True

    # Either the characters match or pattern has '?'
    # move to the next in both text and pattern
    if txt[n - 1] == pat[m - 1] or pat[m - 1] == '?':
        return wildCardRec(txt, pat, n - 1, m - 1)

    # if the current character of pattern is '*'
    # first case: It matches with zero character
    # second case: It matches with one or more characters
    if pat[m - 1] == '*':
        return wildCardRec(txt, pat, n, m-1) or \
               wildCardRec(txt, pat, n-1, m)

    return False

def wildCard(txt, pat):
    n = len(txt)
    m = len(pat)
    return wildCardRec(txt, pat, n, m)

if __name__ == "__main__":
    txt = "abcde"
    pat = "a?c*"
    print("true" if wildCard(txt, pat) else "false")