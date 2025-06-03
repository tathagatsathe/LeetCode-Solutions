class Solution:
    def lengthLongestPath(self, input: str) -> int:
        arr = input.split('\n')
        temp = []
        st = []
        mx = 0
        for i in arr:
            t_c = i.count('\t')
            sr = i.replace('\t','')
            temp.append({'t':t_c, 's': sr})


        st.append({'c': 0, 't': -1})
        for i in temp:
            while(st[-1]['t']>=i['t']):
                st.pop()
            ln = st[-1]['c']+len(i['s'])
            if(len(st)>1):
                ln+=1
            if("." in i['s'] and ln>mx):
                mx = ln
            st.append({'c': ln, 't': i['t']})

        return mx