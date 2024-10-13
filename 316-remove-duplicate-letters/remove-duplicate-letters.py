class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if len(s)<2:return s
        def present(char,s,i):
            for ii in range(i+1,len(s)):
                if s[ii]==char:
                    return True
            return False




        vis=[False]*26
        stack=[]
        for i in range(len(s)):
            char=s[i]
            if vis[ord(char)-ord('a')]:continue
            if not stack:
                stack.append(char)
                vis[ord(char)-ord('a')]=True

            else:
                if ord(stack[-1])<ord(char):
                    vis[ord(char)-ord('a')]=True
                    stack.append(char)
                else:
                    print('q',char,i,stack)
                    print(ord(stack[-1]),ord(char))
                    while stack and  ord(stack[-1])>ord(char):
                        if present(stack[-1],s,i):
                            print(char)
                            
                            vis[ord(stack[-1])-ord('a')]=False
                            stack.pop()
                            # stack.append(char)
                            # vis[ord(char)-ord('a')]=True
                        else:
                            stack.append(char)
                            vis[ord(char)-ord('a')]=True
                    else:
                        if vis[ord(char)-ord('a')]==False:
                            stack.append(char)
                            vis[ord(char)-ord('a')]=True

        return ''.join(stack)



        