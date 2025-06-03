class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # input.replace('\n','\n/')
        # print('input: ',input)
        arr = input.split('\n')
        temp = []
        st = []
        mx = 0
        for i in arr:
            t_c = i.count('\t')
            sr = i.replace('\t','')
            temp.append({'t':t_c, 's': sr})

        # print('temp: ',temp)
        # return 20
        st.append({'c': 0, 't': -1})
        for i in temp:
            # print(st)
            while(st[-1]['t']>=i['t']):
                st.pop()
            ln = st[-1]['c']+len(i['s'])
            if(len(st)>1):
                ln+=1
            if("." in i['s'] and ln>mx):
                mx = ln
            # print(ln)
            st.append({'c': ln, 't': i['t']})

        # [{'t': 0, 's': 'dir'}, {'t': 1, 's': 'subdir1'}, {'t': 1, 's': 'subdir2'}, {'t': 2, 's': 'file.ext'}]

        # print('st: ',st)
        
        return mx

        # ['dir', 'subdir1', 'file1.ext', 'subsubdir1', 'subdir2', 'subsubdir2']
        # ['dir', '\tsubdir1', '\t\tfile1.ext', '\t\tsubsubdir1', '\tsubdir2', '\t\tsubsubdir2', '\t\t\tfile2.ext']
        # 3 -> 10 -> 20
        # 0 ->  